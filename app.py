import openai
# Set up your API key
openai.api_key = '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'

# Use the completion endpoint to get a response from the model
response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct-0914",  # or other engines like "curie"
    prompt="Translate the following English text to French: 'Hello, how are you?'",
    max_tokens=50
)

# Print the response
print(response.choices[0].text.strip())