menu = """
    ====== MENU ======
    (1) Cadastro de usuário
    (2) Cadastro de conta
    (3) Depósito
    (4) Saque
    (5) Extrato
    (6) Sair

"""

def cadastrar_usuario(lista_usuarios:list,**usuario) -> list:
    if usuario not in lista_usuarios:
        lista_usuarios.append(usuario)
    return lista_usuarios

def incrementar_qtd_saques(qtd_saques_realizados:int) -> int:
    qtd_saques_realizados+=1
    return qtd_saques_realizados

def saque(*,limite_qtd_saques:int,limite_valor_saques:int,saldo:float,valor:float,extrato:list,qtd_saques_realizados:int) -> tuple:
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

def deposito(valor:float,saldo:int,extrato) -> tuple:
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

def imprime_extrato(saldo:float,/,*,extrato:list) -> None:
    for registro in extrato:
            print(f"{registro['tipo']}, valor: R$ {registro['valor']:.2f}")
    print(f"O saldo é de R$ {saldo:.2f}")

saldo = 0
LIMITE_VALOR_SAQUES = 500
LIMITE_QTD_SAQUES = 3
extrato = [] # Lista de dicts {"valor":300,"tipo":"Depósito"}
qtd_saques_realizados = 0
usuarios = []
contas = []

while True:
    print(menu)
    op = int(input("Opção: "))
    if op == 1:
        nome = input("Digite o nome: ")
        datansc = input("Digite a data de nascimento: ")
        cpf = int(input("Digite o CPF: "))
        end = input("Digite o endereço: ")
        usuarios = cadastrar_usuario(usuarios,nome=nome,datansc=datansc,cpf=cpf,end=end)
        print(usuarios)
    elif op == 2:
        cpf_dig = int(input("Digite o CPF que será associado a conta: "))
        usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf_dig]
        print(usuario)
    elif op == 3:
        valor = float(input("Digite o valor: "))
        retorno = deposito(valor,saldo,extrato)
        if retorno is not None:
            saldo, extrato = retorno
    elif op == 4:
        valor = float(input("Digite o valor: "))
        retorno = saque(extrato=extrato,limite_qtd_saques=LIMITE_QTD_SAQUES,limite_valor_saques=LIMITE_VALOR_SAQUES,saldo=saldo,valor=valor,qtd_saques_realizados=qtd_saques_realizados)
        if retorno is not None:
            saldo, extrato = retorno
            qtd_saques_realizados = incrementar_qtd_saques(qtd_saques_realizados)
    elif op == 5:
        imprime_extrato(saldo,extrato=extrato)
    elif op == 6:
        print("Obrigado por utilizar o sistema! Até mais!")
        break        
    else:
        print("Opção inválida!")
