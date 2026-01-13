"""
Exercício 01: Reajuste Salarial Simples

Objetivo: Criar um script que receba o nome e o salário atual de um funcionário e calcule um aumento fixo de 15%.

Autor: Gabriel Fernandes Blimbliem
"""


nome_fun = input(print("Digite o seu nome: "))
salario_fun = float(input(print("Digite seu salario: ")))

salario_novo_fun = salario_fun+(salario_fun * 0.15)

print(f"Novo salario {salario_novo_fun}")