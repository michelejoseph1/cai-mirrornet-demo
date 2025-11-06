from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def mirror_explain(text):
    prompt = f"Identify the key compression steps and meaning lost in the following text:\n{text}"
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL","gpt-4.1"),
        messages=[{"role":"user","content": prompt}]
    )
    return resp.choices[0].message.content
