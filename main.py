menu = """
    ====== MENU ======

    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Sair

"""

def incrementar_qtd_saques(qtd_saques_realizados):
    qtd_saques_realizados+=1
    return qtd_saques_realizados

def saque(*,limite_qtd_saques,limite_valor_saques,saldo,valor,extrato,qtd_saques_realizados):
    if qtd_saques_realizados == limite_qtd_saques:
            print(f"Você não pode mais realizar saques, pois já atingiu o limite mensal de {limite_qtd_saques}")
    else:
        if valor > limite_valor_saques:
            print(f"Saques que ultrapassem R$ {limite_valor_saques:.2f} não são permitidos")
        else:
            if valor > 0 and valor <= saldo:
                saldo-=valor
                print("Saque realizado com sucesso!")
                extrato.append({
                    "valor": valor,
                    "tipo": "Saque"
                })
                return saldo,extrato
            else:
                print("Valor do saque não é permitido")

def deposito(valor,saldo,extrato):
    if valor <= 0:
        print("Não é possível depositar valores nulos ou negativos")
    else:
        saldo += valor
        extrato.append({
            "valor": valor,
            "tipo": "Depósito"
        })
    print("Depósito realizado com sucesso!")
    return saldo,extrato

def imprime_extrato(saldo,/,*,extrato):
    for registro in extrato:
            print(f"{registro['tipo']}, valor: R$ {registro['valor']:.2f}")
    print(f"O saldo é de R$ {saldo:.2f}")

saldo = 0
LIMITE_VALOR_SAQUES = 500
LIMITE_QTD_SAQUES = 3
extrato = [] # Lista de dicts {"valor":300,"tipo":"Depósito"}
qtd_saques_realizados = 0

while True:
    print(menu)
    op = int(input("Opção: "))
    if op == 1:
        valor = float(input("Digite o valor: "))
        retorno = deposito(valor,saldo,extrato)
        if retorno is not None:
            saldo, extrato = retorno
    elif op == 2:
        valor = float(input("Digite o valor: "))
        retorno = saque(extrato=extrato,limite_qtd_saques=LIMITE_QTD_SAQUES,limite_valor_saques=LIMITE_VALOR_SAQUES,saldo=saldo,valor=valor,qtd_saques_realizados=qtd_saques_realizados)
        if retorno is not None:
            saldo, extrato = retorno
            qtd_saques_realizados = incrementar_qtd_saques(qtd_saques_realizados)
    elif op == 3:
        imprime_extrato(saldo,extrato=extrato)
    elif op == 4:
        print("Obrigado por utilizar o sistema! Até mais!")
        break        
    else:
        print("Opção inválida!")
