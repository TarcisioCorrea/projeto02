from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("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")
groq_api_key = os.getenv("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")

client = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")


def gerar_resposta(prompt, temperature=0.2):
    resposta = client.responses.create(
        model="openai/gpt-oss-20b",
        temperature=temperature,
        input=prompt
    )

    return resposta.output_text
