from classifier import classificar_mensagem

mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado"
]

temperaturas = [0.0, 0.5, 1.0]

for temp in temperaturas:
    print(f"\n========== Temperatura: {temp} ==========\n")

    for i in range(10):
        print(f"--- Execução {i+1} ---")
        
        for mensagem in mensagens_cliente:
            resposta = classificar_mensagem(mensagem, temperature=temp)
            print(f"Cliente: {mensagem}")
            print(f"Resultado: {resposta}\n")
