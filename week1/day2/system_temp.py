import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API kaha h bhai?")

client=Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

# System role
sys_message = {
    "role": "system",
    # "content": "you are my loving girlfriend"
    # "content": "you are my strict office colleague who is also my manager."
    "content": "you are my brand manager who suggests names for my new food company."
}

# User role
message={
    "role": "user",
    # "content": "I love you"
    "content": "Suggest a name for my food company."
}

messages=[sys_message, message]

completion =client.chat.completions.create(model=model, messages=messages, temperature=0) # by default temperature is 0 and it range is 0-2 (randomness)

# print(completion)
answer= completion.choices[0].message.content

print(answer)
