"""
Exercicio 3: Modularização com Funções
 
Objetivo: Organizar o código criando uma função chamada aumento_salario que recebe os dados por parâmetro e realiza o processamento.

Autor: Gabriel Fernandes Blimbliem
"""
def aumento_salario (matricula,salario):
    if salario >= 5000:
        aumento = 0.10
    else: 
        aumento = 0.15
    novo_salario = salario+(salario*aumento)
    print(f"Olá Sr {matricula}, você recebeu um aumento de {aumento}, e seu novo salario é: {novo_salario}")


matricula_fun = input(print("Digite sua matricula: "))
salario_fun = float(input(print("Digite seu salario: ")))
aumento_salario(matricula_fun,salario_fun)
