#A large customer support team receives many tickets related to different business areas, such as technical issues, billing inquiries, and product feedback. Your task is to create a prompt that automatically classifies incoming tickets into these three groups and routes them to the appropriate support specialists, reducing response times and enhancing customer satisfaction. You will test your prompt on a provided sample ticket.


import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
Api_key = os.getenv("OpenAi_API_key")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens = 100,
        messages = [{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

ticket = """Hello Support Team,

I was charged twice for my subscription this month, but I can only see one active plan in my account dashboard. I’ve already checked my payment history and bank statement, and the duplicate charge is still showing. Could you please look into this and help resolve the issue as soon as possible?

Thank you.
"""
# Craft a prompt to classify the ticket
prompt = f"""
classifies the ticket based on technical issue, billing inquiry, or product feedback, without providing anything else in the response.



```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

  