from Cliente import Cliente
from ContaCorrente import ContaCorrente

menu = """
    ====== MENU ======
    (1) Criação de conta
    (2) Depósito
    (3) Saque
    (4) Extrato
    (5) Sair

"""

def incrementar_qtd_saques(qtd_saques_realizados:int) -> int:
    qtd_saques_realizados+=1
    return qtd_saques_realizados

def saque(*,limite_qtd_saques:int,limite_valor_saques:int,valor:float,qtd_saques_realizados:int,conta:dict,contas:list) -> tuple:
    if qtd_saques_realizados == limite_qtd_saques:
            print(f"Você não pode mais realizar saques, pois já atingiu o limite mensal de {limite_qtd_saques}")
    else:
        if valor > limite_valor_saques:
            print(f"Saques que ultrapassem R$ {limite_valor_saques:.2f} não são permitidos")
        elif valor < 0:
            print("Valores de saque negativos não são permitidos")
        else:
            conta["saldo"] -= valor
            conta["extrato"].append({
                "valor": valor,
                "tipo": "Saque"
            })
            for i,c in enumerate(contas):
                if c["número da conta"] == conta["número da conta"]:
                    contas[i] = conta            
        return contas,conta

def deposito(valor:float,conta:dict,contas:list) -> tuple:
    if valor <= 0:
        print("Não é possível depositar valores nulos ou negativos")
    else:
        conta["saldo"] += valor
        conta["extrato"].append({
            "valor": valor,
            "tipo": "Depósito"
        })
        for i,c in enumerate(contas):
            if c["número da conta"] == conta["número da conta"]:
                contas[i] = conta
    print("Depósito realizado com sucesso!")
    return contas,conta

def imprime_extrato(conta) -> None:
    for registro in conta["extrato"]:
            print(f"{registro['tipo']}, valor: R$ {registro['valor']:.2f}")
    print(f"O saldo é de R$ {conta['saldo']:.2f}")

LIMITE_VALOR_SAQUES = 500
LIMITE_QTD_SAQUES = 3
qtd_saques_realizados = 0
clientes = []
contas = []
num_agencia = "0001"
num_conta = 1
conta_ativa = {}

while True:
    print(menu)
    op = int(input("Opção: "))
    if op == 1:
        nome = input("Digite o nome: ")
        datansc = input("Digite a data de nascimento: ")
        cpf = int(input("Digite o CPF: "))
        end = input("Digite o endereço: ")
        cliente = Cliente([],nome=nome,cpf=cpf,datansc=datansc,endereco=end)
        conta = ContaCorrente(cliente,num_conta,LIMITE_VALOR_SAQUES,LIMITE_QTD_SAQUES)
        cliente.adicionar_conta(conta)
        num_conta+=1
        print(cliente)
    elif op == 2:
        if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
        else:
            valor = float(input("Digite o valor: "))
            retorno = deposito(valor,conta_ativa,contas)
            if retorno is not None:
                contas, conta_ativa = retorno
    elif op == 3:
        if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
        else:
            valor = float(input("Digite o valor: "))
            retorno = saque(conta=conta_ativa,limite_qtd_saques=LIMITE_QTD_SAQUES,limite_valor_saques=LIMITE_VALOR_SAQUES,valor=valor,qtd_saques_realizados=qtd_saques_realizados, contas=contas)
            if retorno is not None:
                contas, conta_ativa = retorno
                qtd_saques_realizados = incrementar_qtd_saques(qtd_saques_realizados)
    elif op == 4:
         if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
         else:
            imprime_extrato(conta_ativa)
    elif op == 5:
        print("Obrigado por utilizar o sistema! Até mais!")
        break         
    else:
        print("Opção inválida!")
