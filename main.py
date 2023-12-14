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

LIMITE_VALOR_SAQUES = 500
LIMITE_QTD_SAQUES = 3
qtd_saques_realizados = 0
clientes = []
num_conta = 1

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
        clientes.append(cliente)
        num_conta+=1
    elif op == 2:
        if not isinstance(conta,ContaCorrente):
            print("Por favor, crie uma conta antes de realizar operações")
        else:
            valor = float(input("Digite o valor: "))
            res = conta.depositar(valor)
            print(f"Depósito realizado com sucesso!" if res else f"Depósito mal-sucedido")
    elif op == 3:
        if not isinstance(conta,ContaCorrente):
            print("Por favor, crie uma conta antes de realizar operações")
        else:
            valor = float(input("Digite o valor: "))
            res = conta.sacar(valor,qtd_saques_realizados)
            print(f"Saque realizado com sucesso!" if res else f"Saque mal-sucedido")
            qtd_saques_realizados = incrementar_qtd_saques(qtd_saques_realizados)
    elif op == 4:
         if not isinstance(conta,ContaCorrente):
            print("Por favor, crie uma conta antes de realizar operações")
         else:
            conta.imprimir_historico()
    elif op == 5:
        print("Obrigado por utilizar o sistema! Até mais!")
        break         
    else:
        print("Opção inválida!")
