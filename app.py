import openai
import os
import configparser

api_key = os.environ.get("OPENAI_API_KEY")

print(api_key)


# Use the completion endpoint to get a response from the model
response = openai.Completion.create(
    model="curie",  # or other engines like "curie"
    prompt="Translate the following to French: 'Hello, how are you?'",
    max_tokens=50
)

# Print the response
print(response.choices[0].text.strip())