import os
from dotenv import load_dotenv
import openai

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("The environment variable OPENAI_API_KEY is not set.")

# Initialize the OpenAI client with the API key
openai.api_key = api_key

# Call the OpenAI ChatCompletion endpoint with the ChatGPT model
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello World!"}]
    )
    
    # Extract and print the response
    print(response.choices[0].message['content'])
except Exception as e:
    print(f"An error occurred: {e}")

