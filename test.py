from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://litellm.deriv.ai/v1"
)

def ask_llm(prompt, model="claude-4-5-sonnet"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


market_data = """
XAUUSD exposure: +5.7m
Session PnL: +101k
Client sentiment: heavily long
"""

prompt = f"""
Summarize this exposure situation in a Slack-ready format:

{market_data}
"""

print(ask_llm(prompt))
