saldo = 1000
saque = 200
limite = 100


print(saldo >= saque)
print(saque <= limite)

#operador E - todas as expressões precisam ser true para retornar true
print(saldo >= saque and saque <= limite)

#operador OU - apenas uma expressão precisa ser true para retornar true
print(saldo >= saque or saque <= limite)

#operador de negação - ele inverte o resultado da expressão
print(not 1000 > 1500)

#lista vazia em python, o valor booleano é falso, por isso o resultado da negação é true
contatos_emergencia = []
print(not contatos_emergencia)

conta_especial = True
print((saldo >= saque and saque <= limite)or(conta_especial and saldo >= saque))