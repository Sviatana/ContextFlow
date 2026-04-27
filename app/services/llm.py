from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_BASE_URL, CHAT_MODEL


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)


def generate_answer(question: str, context: list[str]) -> str:
    context_text = "\n".join(context)

    prompt = f"""
Use only the context below to answer the question.
If the context does not contain the answer, say that there is not enough information.

Context:
{context_text}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a concise technical assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
