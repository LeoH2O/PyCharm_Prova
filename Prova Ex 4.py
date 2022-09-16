#Escreva um programa que apresente quatro opções: (1) consulta saldo,
#(2) saque e (3) depósito e (4) sair. O saldo deve iniciar em R$ 0,00. A
#cada saque ou depósito o valor do saldo deve ser atualizado.

saldo = 0.00

while True:
    print("Consulta de saldo: 1")
    print("Saque: 2")
    print("Depósito: 3")
    print("Sair: 4")

    banco_choice = int(input("O que deseja fazer: "))
    if banco_choice == 1:
        print("Seu saldo:", saldo, "reais")
    elif banco_choice == 2:
        saque = float(input("Quanto você quer sacar: "))
        if saque > saldo:
            print("Você não tem esse valor no saldo para poder sacar.")
        else:
            saldo = saldo - saque
            print("Você sacou:", saque, "reais")
    elif banco_choice == 3:
        deposito = float(input("Quanto você quer depositar: "))
        saldo = saldo + deposito
        print("Você depositou:", deposito, "reais")
    elif banco_choice == 4:
        break
