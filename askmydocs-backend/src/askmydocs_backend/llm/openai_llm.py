from typing import List
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(question: str, context_chunks: List[str], model: str = "gpt-3.5-turbo") -> str:
    context_text = "\n\n".join(context_chunks)

    system_prompt = (
        "Você é um assistente útil que responde com base exclusivamente no contexto abaixo. "
        "Se a resposta não estiver no contexto, diga 'Não sei'."
    )

    user_prompt = f"Contexto:\n{context_text}\n\nPergunta: {question}"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0
    )

    return response.choices[0].message.content.strip()
