import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_key = os.getenv("OpenAi_API_key")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a helpful assistance"},
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# Create the instructions
instructions = (
    "Determine the language of the given text and count the number of sentences it contains. "
    "If the text has more than one sentence, generate a suitable title for it. "
    "If the text has only one sentence, write 'N/A' for the title. "
    "The text will be provided inside triple backticks.\n\n"
)

# Create the output format
output_format = (
    "Output format:\n"
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:\n\n"
)
text = "ChatGPT is a helpful AI tool. It can answer questions and explain topics in simple ways. Many people use it for learning and coding help."
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)