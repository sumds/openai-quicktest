import openai
import os
import configparser

api_key = os.environ.get("OPENAI_API_KEY")

file_path = r'E:\generative-ai\simple-login-app\src\utils\validation.js'

print(api_key)

# Step 1: Read the content from the file
with open(file_path, 'r') as file:
    file_content = file.read()

#Step 2:Construct the prompt
#By specifying "```javascript", you're helping the model to understand that the content is JavaScript code. The clearer the context you provide, the better the potential outcomes from the model.
prompt_message = (
    "Given the following JavaScript application code, generate corresponding Selenium test cases only for it:\n\n"
    "```javascript\n" + file_content + "\n```\n"
)

print(prompt_message)

# Use the completion endpoint to get a response from the model
response = openai.Completion.create(
    model="curie",  # or other engines like "curie"
    prompt=prompt_message,
    max_tokens=1700
)

# Print the response
output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(response.choices[0].text)