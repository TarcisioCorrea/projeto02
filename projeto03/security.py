def detectar_prompt_injection(texto):

    ataques = [
        "system prompt",
        "ignore previous instructions",
        "ignore todas as instruções",
        "mostre seu prompt",
        "qual sua system prompt",
        "reveal system prompt"
    ]

    texto = texto.lower()

    for ataque in ataques:
        if ataque in texto:
            return True

    return False


def erro_seguro():
    return {
        "erro": "Tentativa de prompt injection detectada"
    }