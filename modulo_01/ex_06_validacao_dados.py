"""
Ex 06: Validação de Dados e Tratamento de Exceções

Objetivo: Implementar uma camada de segurança no sistema para evitar que o programa "quebre" (crash) caso o usuário digite valores não numéricos no campo de salário. O programa deve identificar o erro, avisar o usuário e pedir o dado novamente até que um valor válido seja inserido.

Autor: Gabriel Fernandes Blimbliem

"""

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
    while True:
        try:
            salario = float(input("Digite o salário: "))
            break  # Se deu certo, sai do loop de validação
        except ValueError:
            print("Erro! Por favor, digite apenas números para o salário.")
       
    
    # Chama a função e guarda o resultado
    novo = calcular_aumento(salario)
    
    # Soma o novo salário ao total acumulado
    total_gasto += novo
    qtd_funcionarios += 1
    
    print(f"Salário com aumento: R$ {novo:.2f}")
    print(f"Total acumulado na folha: R$ {total_gasto:.2f}")

print(f"\nOrçamento esgotado!")
print(f"Total de funcionários cadastrados: {qtd_funcionarios}")