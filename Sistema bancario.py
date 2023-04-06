menu = '''MENU
(1) deposito 
(2) saque 
(3) extrato 
(4) saida
==> '''

saldo = 0 
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("indique o valor do seu deposito: "))

        if valor > 0: 
            saldo += valor
            extrato += f"deposito: R$ {valor: .2f} \n"
            print("deposito realizado com sucesso")
        
        else:
            print("por favor, deposite um valor valido")
        
    elif opcao == "2": 
        valor = float(input("Quanto você deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("você excedeu o seu saldo disponivel")

        elif excedeu_limite:
            print("você excedeu o seu limite")

        elif excedeu_limite_saque: 
            print("você excedeu o limite de saques diários")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f} \n"
            print("saque realizado com sucesso")
            numero_saques += 1

        else:
            print("por favor, deposite um valor valido")

    elif opcao == "3":
        print("############ extrato #######")
        print("não ocorreram movimentações" if not extrato else extrato)
        print(f"\n Saldo R$ {saldo: .2f}")
        print (" ###### fim ##### ")
        
    elif opcao == "4":
        print("até mais")
        break

    else:
        print("opcao invalida, tente outra vez")

   