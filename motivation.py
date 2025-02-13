import openai
import os

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found! Please run export OPENAI API_KEY=\"NEW_API_KEY\" in terminal.")

def generate_sentence(prompt):

    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create( 
        model = "gpt-3.5-turbo",
        messages=[ 
            {"role": "system", "content": "You are a motivational phrase generator. You should write motivating sentences about the subject entered by the user."}, 
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

prompt = input("What would you like to get motivated about?: ")

print(generate_sentence(prompt))