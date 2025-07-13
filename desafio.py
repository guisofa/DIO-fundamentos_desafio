menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo Usuario
[c] Nova Conta
[q] Sair

=> """

#funcao de deposito
def deposito(saldo, extrato, /):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except:
        valor = 0

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo

#Funcao de saque
def saque(*, saldo, extrato, lim, num_saq, lim_saq):
    try:
        valor = float(input("Informe o valor do saque: "))
    except:
        valor = 0

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > lim:
        print("Operação falhou! O valor do saque excede o limite.")
    elif num_saq >= lim_saq:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        num_saq += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, num_saq

#funcao de extrato
def imprime_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cria_usuario(users):
    cpf = input("CPF: ")
    for u in users:
        if u['cpf'] == cpf:
            print('usuario ja existe')
            return
    nome = input("nome: ")
    data_nascimento = input("data de nascimento: ")
    endereco = input("endereço: ")
    users.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("usuario criado com sucesso")

def criar_conta(agencia, users):
    cpf = input("Informe o CPF do usuário: ")
    for u in users:
        if u['cpf'] == cpf:
            usuario = u
            break
    else:
        usuario = None

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        numero_conta = len(users) + 1
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

saldo = 0
LIMITE = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = '0001'

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo = deposito(saldo, extrato)
    elif opcao == "s":
        saldo, numero_saques = saque(saldo=saldo, extrato=extrato, lim=LIMITE, lim_saq=LIMITE_SAQUES, num_saq=numero_saques)
    elif opcao == "e":
        imprime_extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break
    elif opcao == 'u':
        cria_usuario(usuarios)
    elif opcao == 'c':
        criar_conta(AGENCIA, usuarios)
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")