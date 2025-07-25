saldo = 1200.0
saque = float(input("Quanto você deseja sacar?"))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque! Você sacou {saque}.")
