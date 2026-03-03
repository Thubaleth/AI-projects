import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_key = os.getenv("openAI_Api_key")

if not Api_key:
    raise ValueError("Open AI key not been found from env file")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

finance_text = "Finance is the study of money and how it is used. Specifically, it deals with the questions of how an individual, company or government acquires the money needed and how they then spend or invest that money. Core financial theories can largely be divided into the following categories: financial economics, mathematical finance and valuation. In the context of institutions, finance is often split into the following major categories: investment management, corporate finance, personal finance and public finance."

prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

print(get_response(prompt))
