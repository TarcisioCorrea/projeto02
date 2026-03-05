from openai import OpenAI
import numpy as np

client = OpenAI()

vetores = []
textos = []


def gerar_embedding(texto):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texto
    )
    return response.data[0].embedding


def carregar_conhecimento():
    global vetores
    global textos

    with open("conhecimento.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()

        if linha:
            emb = gerar_embedding(linha)

            vetores.append(emb)
            textos.append(linha)


def similaridade(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def buscar_contexto(pergunta):

    emb_pergunta = gerar_embedding(pergunta)

    melhor_score = -1
    melhor_texto = ""

    for i, vetor in enumerate(vetores):

        score = similaridade(emb_pergunta, vetor)

        if score > melhor_score:
            melhor_score = score
            melhor_texto = textos[i]

    return melhor_texto