from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def hallucination_risk(claim):
    prompt = f"Is the following claim likely hallucinated? Return reasoning and confidence only:\n{claim}"
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL","gpt-4.1"),
        messages=[{"role":"user","content": prompt}]
    )
    return resp.choices[0].message.content
