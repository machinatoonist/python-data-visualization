import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead

# Use the ChatGPT model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")

# Set the maximum input length to the size of the model's input
max_input_length = tokenizer.max_model_input_sizes['microsoft/DialoGPT-medium']

# Create the main app UI
st.title("Chat with ChatGPT")
prompt = st.text_input("Enter your message:", max_characters=max_input_length)

# If the user entered a prompt, generate a response from ChatGPT
if prompt:
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    response = model.generate(input_ids=input_ids, max_length=128)
    response_text = tokenizer.decode(response[0])
    st.markdown(response_text)
