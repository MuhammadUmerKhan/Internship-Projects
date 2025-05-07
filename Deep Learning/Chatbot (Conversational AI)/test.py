from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
    return tokenizer, model

def generate_response(tokenizer, model, user_input, history, max_length=150):
    # Enhanced prompt to encourage conversational variety
    prompt = "You are a friendly and engaging chatbot. Respond with enthusiasm and detail. Conversation history:\n"
    for entry in history:
        prompt += f"User: {entry['user']}\nBot: {entry['bot']}\n"
    prompt += f"User: {user_input}\nBot:"

    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    
    output_ids = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=input_ids.shape[1] + max_length,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=60,  # Increased top-k for more variety
        top_p=0.92,  # Slightly higher top-p for creativity
        temperature=0.8,  # Higher temperature for diverse responses
        no_repeat_ngram_size=3,  # Prevent repetition of 3-word phrases
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(output_ids[:, input_ids.shape[1]:][0], skip_special_tokens=True)
    return response.strip()

def main():
    tokenizer, model = load_model()
    history = []
    print("DialoGPT Terminal Chatbot (type 'exit' to quit)")
    print("-----------------------------------------")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if not user_input.strip():
            print("Please enter a message!")
            continue
        response = generate_response(tokenizer, model, user_input, history)
        history.append({"user": user_input, "bot": response})
        print(f"Bot: {response}")
        print("-----------------------------------------\n")

if __name__ == "__main__":
    main()