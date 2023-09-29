import openai
import os
import configparser

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables!")


file_path = r'E:\generative-ai\simple-login-app\src\utils\validation.js'

openai.api_key = api_key

# Step 1: Read the content from the file
with open(file_path, 'r') as file:
    file_content = file.read()

#Step 2:Construct the prompt
#By specifying "```javascript", you're helping the model to understand that the content is JavaScript code. The clearer the context you provide, the better the potential outcomes from the model.
prompt_message = (
    "Given the following test scenarios for a web login page, generate corresponding Selenium test cases written in Python:\n\n"
    + file_content + "\n"
    "Please use Chrome as the web driver and provide complete scripts."
)

messages = [
    {"role": "system", "content": "You are a helpful assistant that generates Selenium test cases based on given JavaScript code."},
    {"role": "user", "content": prompt_message}
]

# Use the completion endpoint to get a response from the model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Print and save the response


output_file_path = 'output.txt'
with open(output_file_path, 'w', encoding="utf-8") as output_file:
    output_file.write(response.choices[0].message['content'])