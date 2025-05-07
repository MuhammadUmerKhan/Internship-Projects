import gradio as gr
from chatbot import Chatbot


chatbot = Chatbot()

def chatbot_interface(user_input):
    return chatbot.generate_response(user_input)

iface = gr.Interface(
            fn=chatbot_interface, 
            inputs='text', 
            outputs='text', 
            title="OpenChatGPT2", 
            description="Conversational AI Using GPT-2"
        )

if __name__ == "__main__":
    iface.launch()