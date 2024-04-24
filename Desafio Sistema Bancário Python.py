print("""
    $$$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  
    $$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ 
    $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ /  $$ |
    $$$$$$$\ |$$$$$$$$ |$$ $$\$$ |$$ |      $$ |  $$ |
    $$  __$$\ $$  __$$ |$$ \$$$$ |$$ |      $$ |  $$ |
    $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |  $$ |
    $$$$$$$  |$$ |  $$ |$$ | \$$ |\$$$$$$  | $$$$$$  |
    \_______/ \__|  \__|\__|  \__| \______/  \______/
      """)

menu = """

Bem vindo(a)!
O que deseja fazer hoje?
--------------------------------------------------
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
--------------------------------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("==============================================")
            print("Operação falhou! O valor informado é inválido.")
            print("==============================================")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("===============================================")
            print("Operação falhou! Você não tem saldo suficiente.")
            print("===============================================")

        elif excedeu_limite:
            print("==================================================")
            print("Operação falhou! O valor do saque excede o limite.")
            print("==================================================")

        elif excedeu_saques:
            print("==================================================")
            print("Operação falhou! Número máximo de saques excedido.")
            print("==================================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("==============================================")
            print("Operação falhou! O valor informado é inválido.")
            print("==============================================")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "4":
        print("==========================================")
        print("     Obrigado por usar o nosso banco.")
        print("==========================================")
        break

    else:
        print("=====================================================================")
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("=====================================================================")
