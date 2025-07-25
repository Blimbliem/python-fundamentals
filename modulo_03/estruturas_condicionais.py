
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

# If simples
if saldo >= saque:
    print("Realizando saque!")
if saldo <= saque:
    print("Saldo insuficiente!")

# IF/ELSE

saldo1 = 2000.0
saque1 = float(input("Informe o valor do saque: "))

if saldo1 >= saque:
    print("Realizado saque!")
else: print("Saldo insuficiente! ")

# IF/ELIF/ELSE

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao ==1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")