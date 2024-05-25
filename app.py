menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(saldo, extrato):
    valor = float(input("Informe o valor do deposito: "))
    if valor <= 0:
        print("Informe um valor maior que 0")
    else:
        saldo += valor
        extrato = (
            f"Deposito realizado no valor de R$ {valor:.2f}, novo saldo: R$ {saldo:.2f}"
        )
        print(extrato)
        return extrato, saldo


def saque(saque, saldo, extrato, numero_saques):
    if saque <= saldo:
        if saque <= limite:
            saldo -= saque
            extrato += f"\nSaque realizado no valor de R$ {saque:.2f}"
            numero_saques += 1
            print(extrato)
            return saldo, extrato, numero_saques
        else:
            print(
                f"O saque de R$ {saque:.2f} é maior que o limite por operação de {limite}"
            )
            return saldo, extrato, numero_saques
    else:
        print(f"você não tem saldo suficiente: R$ {saque:.2f}")
        return saldo, extrato, numero_saques


while True:
    opcao = input(menu)

    if opcao == "d":
        extrato, saldo = deposito(saldo, extrato)

    elif opcao == "s":

        if not saldo:
            print("Sem saldo para saca")
        else:
            v_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                v_saque, saldo, extrato, numero_saques
            )
        if numero_saques > LIMITE_SAQUES:
            print("Você atingiu o limite de 3 saques")

    elif opcao == "e":
        print("\n-----------Extrato------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------------------")
    elif opcao == "q":
        break
    else:
        print("Operação invalida")
        break
