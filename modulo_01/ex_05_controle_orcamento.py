"""
Ex 05: Controle de Orçamento (Acumuladores e Condição Dinâmica)

Objetivo: Criar um sistema de monitoramento financeiro que processe reajustes salariais de forma contínua, interrompendo a entrada de dados automaticamente assim que o somatório dos novos salários atingir o teto orçamentário de R$ 15.000,00.

Autor: Gabriel Fernandes Blimbliem

"""

def calcular_aumento(salario):
    if salario >= 5000:
                aumento = 0.10
    else:
        aumento = 0.15

    novo_salario = salario +(salario*aumento)
    return(novo_salario)

total_gasto = 0
qtd_funcionarios = 0

while total_gasto < 15000:
    nome = input("Nome: ")
    salario = float(input("Salário Atual: "))
    
    # Chama a função e guarda o resultado
    novo = calcular_aumento(salario)
    
    # Soma o novo salário ao total acumulado
    total_gasto += novo
    qtd_funcionarios += 1
    
    print(f"Salário com aumento: R$ {novo:.2f}")
    print(f"Total acumulado na folha: R$ {total_gasto:.2f}")

print(f"\nOrçamento esgotado!")
print(f"Total de funcionários cadastrados: {qtd_funcionarios}")