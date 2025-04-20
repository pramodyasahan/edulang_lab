import openai
from dotenv import load_dotenv

load_dotenv()


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the following text and output as a string"
        f"Text: {text}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are an experience text summarizer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.0
    )
    result = response.choices[0].message.content.strip()
    return result
