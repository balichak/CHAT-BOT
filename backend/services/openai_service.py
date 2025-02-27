import openai
from config import openai_api_key

openai.api_key = openai_api_key

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI chatbot with advanced capabilities."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
