"""
Exercício 01: Reajuste Salarial Simples
Objetivo: Receber nome e salário e aplicar 15% de aumento.
Autor: Gabriel

"""

def aumento_salario(salario_atual,nome):
    if salario_atual >= 5000:
                aumento = 0.10
    else:
        aumento = 0.15

    novo_salario = salario_atual +(salario_atual*aumento)
    print(f"Olá {nome}, seu novo salário é R$ {novo_salario:.2f}. "
                f"Seu aumento foi de {aumento*100}%!")

contador = 0 
while contador < 3:
    print(f"\n--- Funcionário {contador + 1} ---")
    nome = input("Digite o nome do funcionario: ")
    salario_atual = float(input("Digite seu salario: "))

    aumento_salario(salario_atual, nome)    

    contador = contador + 1

    print("Todos funcionarios foram processados!")

