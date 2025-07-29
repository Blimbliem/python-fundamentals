# while normal

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao ==1:
        print("Sacando!")
    elif opcao==2:
        print("Exibindo o extrato!")

#while c/ else

opcao2 = -1

while opcao2 != 0:
    opcao2 = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao2 ==1:
        print("Sacando!")
    elif opcao2 ==2:
        print("Exibindo o extrato!")
else:
    print("Obrigado por usar nosso sistema bancário, até a próxima!")


# looping infinito

while True:
    opcao3 = int(input("Informe um número: "))

    if opcao3 == 10:
        break # cortar a execução do loop

    if opcao3 % 2 == 0:
        continue # é queremos pular a execução

    print(opcao3)



