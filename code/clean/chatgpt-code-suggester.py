import streamlit as st
import openai


if __name__ == "__main__":
    st.title("ChatGPT Code Generator")
    st.write("Enter your ChatGPT API key and code prompt to generate Python code.")
    st.write("Note: Your API key is private and should not be shared with anyone.")

# Get API key from user
api_key = st.text_input("Enter your ChatGPT API key:")

# Get prompt from user
prompt = st.text_input("Enter your code prompt:")

# Set up request to ChatGPT API
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "prompt": prompt,
    "max_tokens": 2048
}

# Submit button
if st.button("Submit"):
    openai.api_key = api_key
    # Send request and get response
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n = 1,
    stop=None,
    temperature=0.5)
    
    # Display response
    st.code(response["choices"][0]["text"])
    
# To put a Streamlit app into production for public preview, follow these steps:

# Install Streamlit on the server where you want to run the app, using the command pip install streamlit.

# Run the Streamlit app on the server using the command streamlit run app.py, where app.py is the name of your app file.

# Expose the Streamlit app to the internet using a tunneling service like ngrok. Install ngrok on the server and run the command ngrok http 8501, where 8501 is the default port used by Streamlit. This will generate a public URL that you can share with others to preview your app.

# To make the app accessible at a custom URL, you can set up a custom domain and use a reverse proxy service like Nginx to route traffic to the app.

# To ensure the app stays running, you can use a process manager like PM2 to manage and monitor the app's process on the server.

# To improve the performance and scalability of the app, you can use a cloud service like AWS Elastic Beanstalk or Google Cloud Platform to deploy and run the app in a production environment.

# To monitor the app's performance and usage, you can set up logging and analytics tools like Elasticsearch, Kibana, and Grafana to track and visualize the app's metrics and logs.