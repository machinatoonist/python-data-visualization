import gradio as gr
import openai

# Define a function to get the code suggestions from ChatGPT
def writecode(chatgpt_api_key, prompt, temperature):
    openai.api_key = chatgpt_api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=temperature)
    return response["choices"][0]["text"] 

# Create the main app UI
gr.Interface(
    writecode,
    [
        gr.Textbox(label="Enter your ChatGPT API key:"),
        gr.Textbox(label="Code Prompt"),
        gr.Slider(label="Temperature", minimum=0, maximum=1, step=0.1, value=0.5)
    ],
    gr.Textbox(label="Generated Code"),
    title="ChatGPT Code Generator"
).launch(share=True)
