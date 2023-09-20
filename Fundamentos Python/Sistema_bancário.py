menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo += valor
        extrato += f'Depósito de R$ {valor}\n'

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
        excedeu_valor_saque = valor > limite
        excedeu_saldo = valor > saldo
        if excedeu_valor_saque:
            print(f"O valor do saque excede o limite de R${limite}.")
        elif excedeu_limite_saques:
           print(f"Você excedeu o limite de saques diários, que são {LIMITE_SAQUES}.")
        elif excedeu_saldo:
            print(f"Você não tem saldo suficiente para esta operação. Seu saldo é de R${saldo}.")    
        else:        
            saldo -= valor
            extrato += f'Saque de R$ {valor}\n'
            numero_saques += 1
            print(f"Saque de R${valor} realizado com sucesso")     
    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")