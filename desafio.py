menu = """

[d] Depositar
[s] Sacar
[e] Extrato
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
def extrato(saque, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

saldo = 0
LIMITE = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo = saldo(saldo, extrato)
    elif opcao == "s":
        saldo, numero_saques = saque(saldo=saldo, extrato=extrato, lim=LIMITE, lim_saq=LIMITE_SAQUES, num_saq=numero_saaques)
    elif opcao == "e":
        extrato(sque, extrato=extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
