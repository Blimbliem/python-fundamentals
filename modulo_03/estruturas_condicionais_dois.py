MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade! Pode tirar a CNH.")
elif idade == 17:
    opcao = int(input("Já realizou aniversário esse ano? [1]- Sim [2]- Não"))
    if opcao == 1:
        print("Menor de idade! Volte no ano que vem!")
    else: print("Pode tirar a CNH. Entre em contato com nosso departamento.")
else: print("Menor de idade! Não pode tirar CNH")