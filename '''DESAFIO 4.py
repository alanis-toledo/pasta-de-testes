transacoes = []

while True:
    print("1 - Adicionar transação")
    print("2 - Ver saldo atual")
    print("3 - Ver todas as transações")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        tipo = input("Tipo (entrada/saída): ").lower()
        transacoes.append({"descricao": descricao, "valor": valor, "tipo": tipo})

    elif opcao == "2":
        saldo = 0
        for t in transacoes:
            if t["tipo"] == "entrada":
                saldo += t["valor"]
            elif t["tipo"] == "saída":
                saldo -= t["valor"]
        print(f"Saldo atual: R${saldo: .2f}")

    elif opcao == "3":
        print("Transações:")
        for t in transacoes:
            print(f"{t['tipo']}: {t['descricao']} | R${t['valor']:.2f}")

    elif opcao == "4":
        print("Você esta saindo do programa! Até logo :D")
        break

    else:
        print("Opção inválida.")