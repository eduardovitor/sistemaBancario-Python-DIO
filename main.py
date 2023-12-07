menu = """
    ====== MENU ======
    (1) Cadastro de usuário
    (2) Cadastro de conta
    (3) Depósito
    (4) Saque
    (5) Extrato
    (6) Sair

"""

def cadastrar_conta(usuario:dict,num_agencia:str,/,*,num_conta:int,contas:list) -> tuple:
    conta = {
        "agência": num_agencia,
        "número da conta": num_conta,
        "usuário": usuario,
        "saldo": 0,
        "extrato": []
    }
    num_conta += 1
    contas.append(conta)
    print("Conta criada com sucesso!")
    return contas,num_conta,conta


def cadastrar_usuario(lista_usuarios:list,**usuario) -> list:
    cadastrado = False
    for u in lista_usuarios:
        if u["cpf"] == usuario["cpf"]:
            print("CPF já cadastrado")
            cadastrado = True
            break
    if not cadastrado:
        lista_usuarios.append(usuario)
    return lista_usuarios

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
usuarios = []
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
        usuarios = cadastrar_usuario(usuarios,nome=nome,datansc=datansc,cpf=cpf,end=end)
    elif op == 2:
        cpf_dig = int(input("Digite o CPF que será associado a conta: "))
        usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf_dig]
        if len(usuario) > 0:
            contas, num_conta, conta_ativa = cadastrar_conta(usuario[0],num_agencia,num_conta=num_conta,contas=contas)
        else:
            print("CPF inválido")
    elif op == 3:
        if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
        else:
            valor = float(input("Digite o valor: "))
            retorno = deposito(valor,conta_ativa,contas)
            if retorno is not None:
                contas, conta_ativa = retorno
    elif op == 4:
         if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
         else:
            valor = float(input("Digite o valor: "))
            retorno = saque(conta=conta_ativa,limite_qtd_saques=LIMITE_QTD_SAQUES,limite_valor_saques=LIMITE_VALOR_SAQUES,valor=valor,qtd_saques_realizados=qtd_saques_realizados, contas=contas)
            if retorno is not None:
                contas, conta_ativa = retorno
                qtd_saques_realizados = incrementar_qtd_saques(qtd_saques_realizados)
    elif op == 5:
         if len(conta_ativa) == 0:
            print("Por favor, crie uma conta antes de realizar operações")
         else:
            imprime_extrato(conta_ativa)
    elif op == 6:
        print("Obrigado por utilizar o sistema! Até mais!")
        break        
    else:
        print("Opção inválida!")
