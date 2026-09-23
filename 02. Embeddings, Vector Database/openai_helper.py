import os
import sys

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# __file__  # 当前执行文件的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
# print(BASE_DIR)  # D:\dev\ai\associate-ai-engineer-for-developer

sys.path.insert(0, BASE_DIR)

OPENAI_MODEL = "gpt-5.4-mini"

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def print_response_content(response):
    return print(response.choices[0].message.content)


def get_response(prompt, model=OPENAI_MODEL):
    # Create a request to the chat completions endpoint
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content


def get_response_system_user(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, temperature=0
    )

    return response.choices[0].message.content


# Define a create_embeddings function
def create_embeddings(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    response_dict = response.model_dump()

    return [data["embedding"] for data in response_dict["data"]]
