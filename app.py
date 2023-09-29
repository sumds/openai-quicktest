import openai
import os
import configparser

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables!")


file_path = r'E:\generative-ai\simple-login-app\src\utils\validation.js'

openai.api_key = api_key

# Step 1: Read the content from the file
try:
    with open(file_path, 'r') as file:
        file_content = file.read()
except FileNotFoundError:
    print(f"File {file_path} not found!")
    exit()

#Step 2:Construct the prompt
#By specifying "```javascript", you're helping the model to understand that the content is JavaScript code. The clearer the context you provide, the better the potential outcomes from the model.
prompt_messag_1 = (
    "Given the following test scenarios for a web login page, generate corresponding Selenium test cases written in Python:\n\n"
    + file_content + "\n"
    "Please use Chrome as the web driver and provide complete scripts."
)

prompt_message_2 = (
    "Given the following JavaScript functions from a web login page:\n"
    "```javascript\n"
    + file_content + "\n"
    "```\n"
    "Please generate corresponding all possible exact unit test cases using the Jest testing framework."
)

# messages = [
#     {"role": "system", "content": "You are a helpful assistant that generates e exact unit test cases based on given JavaScript code."},
#     {"role": "user", "content": prompt_message_2}
# ]

messages = [
    {"role": "system", "content": "You are a helpful assistant that generates unit test cases based on given JavaScript code."},
    {"role": "user", "content": prompt_message_2}
]

# messages = [
#     {"role": "system", "content": "You are a helpful assistant that generates Selenium test cases based on given JavaScript code."},
#     {"role": "user", "content": prompt_message_2}
# ]
# Use the completion endpoint to get a response from the model
try:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
except Exception as e:
    print(f"API Call failed: {e}")
    exit()

# Print and save the response
output_file_path = 'output-js.txt'
if 'choices' in response and 'message' in response.choices[0]:
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        output_file.write(response.choices[0].message['content'])
else:
    print("Unexpected response structure from OpenAI.")