from openai import OpenAI
from dotenv import load_dotenv
from tools import data_atual, calcular_idade, converter_celsius_para_fahrenheit
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "memory.json"
MAX_HISTORY = 10

# Persona do assistente
system_message = {
    "role": "system",
    "content": "Você é um assistente educado, amigável e responde de forma clara."
}

# Histórico de mensagens
historico_mensagens = []


# ---------------- MEMÓRIA ----------------

def carregar_historico():
    global historico_mensagens

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            historico_mensagens = json.load(f)
    else:
        historico_mensagens = [system_message]


def salvar_json():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(historico_mensagens, f, indent=4, ensure_ascii=False)


def salvar_historico(mensagem):
    historico_mensagens.append(mensagem)

    # limitar memória
    if len(historico_mensagens) > MAX_HISTORY:
        historico_mensagens[:] = [historico_mensagens[0]] + historico_mensagens[-MAX_HISTORY:]

    salvar_json()


def limpar_memoria():
    global historico_mensagens
    historico_mensagens = [system_message]
    salvar_json()
    print("Assistente: Memória da conversa apagada.")


# ---------------- CHAT ----------------

def chat(pergunta):
    salvar_historico({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico_mensagens
    )

    resposta_conteudo = resposta.choices[0].message.content
    salvar_historico({"role": "assistant", "content": resposta_conteudo})

    return resposta_conteudo


# ---------------- PROGRAMA ----------------

carregar_historico()

print("Assistente iniciado. Digite /limpar para apagar memória.")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    if pergunta == "/limpar":
        limpar_memoria()
        continue

    # exemplo usando função python
    if "data" in pergunta.lower():
        salvar_historico({"role": "user", "content": pergunta})
        resposta = "Hoje é " + str(data_atual())
        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente:", resposta)
        continue

    resposta = chat(pergunta)
    print("Assistente:", resposta)