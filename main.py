menu = """
    ====== MENU ======

    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Sair

"""

saldo = 0
LIMITE_VALOR_SAQUES = 500
LIMITE_QTD_SAQUES = 3
extrato = [] # Lista de dicts {"valor":300,"tipo":"d"}
qtd_saques_realizados = 0

while True:
    print(menu)
    op = int(input("Opção: "))
    if op == 1:
        valor = float(input("Digite o valor: "))
        if valor <= 0:
            print("Não é possível depositar valores nulos ou negativos")
        else:
            saldo += valor
            extrato.append({
                "valor": valor,
                "tipo": "Depósito"
            })
            print("Depósito realizado com sucesso!")
    elif op == 2:
        if qtd_saques_realizados == LIMITE_QTD_SAQUES:
            print(f"Você não pode mais realizar saques, pois já atingiu o limite mensal de {LIMITE_QTD_SAQUES}")
        else:
            valor = float(input("Digite o valor: "))
            if valor > LIMITE_VALOR_SAQUES:
                print(f"Saques que ultrapassem R$ {LIMITE_VALOR_SAQUES:.2f} não são permitidos")
            else:
                if valor > 0 and valor <= saldo:
                    saldo-=valor
                    qtd_saques_realizados+=1
                    print("Saque realizado com sucesso!")
                    extrato.append({
                        "valor": valor,
                        "tipo": "Saque"
                    })
                else:
                    print("Valor do saque não é permitido")
    elif op == 3:
        for registro in extrato:
            print(f"{registro['tipo']}, valor: R$ {registro['valor']:.2f}")
        print(f"O saldo é de R$ {saldo:.2f}")
    elif op == 4:
        print("Obrigado por utilizar o sistema! Até mais!")
        break        
    else:
        print("Opção inválida!")
