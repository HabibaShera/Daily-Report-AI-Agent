# Summarizes article content using LLM / transformers

import os
from groq import Groq
#from settings import groq_token

# Initialize Groq client
groq_token = os.getenv("GROQ_TOKEN")
client = Groq(api_key=groq_token)

def summarize_text(text: str) -> dict:
    """
    Summarize text using Groq LLM:
    - Generate a headline
    - Create simple bullet point summary
    """

    prompt = f"""
    I will give you some text. 
    Your task:
    1. Create a short and clear headline/title for the text.
    2. Summarize the text in bullet points, using simple words.

    NOTE: use emojis in the bullet points to make it more engaging.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        # model="llama-3.3-70b-versatile",  # you can change to smaller if needed
        model = "openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    result = response.choices[0].message.content

    return result

# Example usage
if __name__ == "__main__":
    with open("article_text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    result = summarize_text(text)
    print(result)