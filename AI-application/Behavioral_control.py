import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_Key = os.getenv("OpenAi_API_key")

def get_response(refined_system_prompt,prompt):
    client = OpenAI(api_key=Api_Key)
    response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages = [ 
                      {"role":"system","content":refined_system_prompt},
                      {"role":"user","content":prompt}
                    ]
    )  

    return response.choices[0].message.content

# Define the technical issue condition
technical_issue_condition = "I'm sorry to hear about your issue with ... if the user is reporting a technical issue."
base_system_prompt = """
You are a professional and polite customer support chatbot.
You help customers with orders, deliveries, refunds, and technical issues.
Your responses should be clear, concise, and helpful.
"""

order_number_condition = """
If a user asks about an order but does NOT provide an order number,
politely ask them to share their order number before proceeding.
"""

technical_issue_condition = """
If the user is reporting a technical issue,
start your response with:
"I'm sorry to hear about your issue with ..."
and then continue with helpful troubleshooting steps.
"""
# Create the refined system prompt
refined_system_prompt =f"""

```{base_system_prompt}```

```{order_number_condition}```
```{technical_issue_condition }```

"""

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)