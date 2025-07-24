def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado = ", valor )
        print("Saldo = ", saldo - valor)

sacar(200)