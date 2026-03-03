import os 
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
Api_key = os.getenv("OpenAi_API_key")

# Optional: check if key is loaded
if not Api_key:
    raise ValueError("There is no API key")

# Create OpenAI client
def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=[{"role":"user","content":prompt}]
    )

    return response

response = get_response("Explain AI in simple terms")
input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000


# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price) + (output_tokens * output_token_price)

print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Estimated cost: ${cost:.10f}")
