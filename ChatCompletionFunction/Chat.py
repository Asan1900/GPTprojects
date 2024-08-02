from dotenv import load_dotenv
import openai
import os

load_dotenv()

api_key = os.getenv('CHATGPT_API')

if not api_key:
    raise ValueError("The environment variable CHATGPT_API is not set.")

openai.api_key = api_key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a teacher."},
            {"role": "user", "content": "Are there other measures than time complexity for an algorithm?"},
            {"role": "assistant", "content": "Yes, there are other measures besides time complexity for an algorithm, such as space complexity."},
        ]
    )
    
    print(response.choices[0].message['content'])

except Exception as e:
    print(f"An error occurred: {e}")