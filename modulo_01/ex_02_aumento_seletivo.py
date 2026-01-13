"""
EXERCICIO: O Aumento Seletivo (Condicionais

OBJETIVO: Evoluir o exercício anterior para que o programa decida o percentual de aumento com base no valor do salário.
Salários até R$ 5.000,00 -> 15% de aumento.
Salários acima de R$ 5.000,00 -> 10% de aumento.

AUTOR: Gabriel Fernnades Blimbliem
"""
nome_fun = input(print("Digite o seu nome: "))

salario_fun = float(input(print("Digite seu salario: ")))

if salario_fun >= 5000:
    salario_novo_fun = salario_fun+(salario_fun * 0.10)
else:
    salario_novo_fun = salario_fun+(salario_fun * 0.15)

print(f"Novo salario {salario_novo_fun}")