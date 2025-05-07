from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class Chatbot:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.chat_history = ""
    
    def generate_response(self, user_input, max_length=100):
        self.chat_history += f"User: {user_input}\nBot:"
        input_ids = self.tokenizer.encode(self.chat_history, return_tensors='pt')
        
        with torch.no_grad():
            output = self.model.generate(
                input_ids, max_length = input_ids.shape[1] + max_length,
                pad_token_id = self.tokenizer.eos_token_id,
                do_sample=True, top_p=0.92, temperature=0.7
            )
        
        decode_output = self.tokenizer.decode(output[0], skip_special_tokens=True)
        reply = decode_output[len(self.chat_history):].split("User:")[0].strip()
        self.chat_history += f" {reply}\n"
        return reply