nome = "Gabriel Fernandes Blimbliem"

print(nome[0])

print(nome[:10]) #start vazio considera-se iniciar no indice 0

print(nome[8:]) # começa a partir do indice informado no stop e vai até o fim

#pegar pedaço da string
print(nome[8:17])

#pega a string por intervalos
print(nome[8:17:2])

nome2 = "Gabriel"
print(nome2)
#como espelhar uma string?
print(nome[::-1])
contrario = (nome2[::-1])
print(contrario)

print(contrario == nome2)

#GABRIEL
eu = "GABRIEL"
print(eu[0:4])


# Misturando o aprendizado:
frase = "Aprendendo Python é muito legal"
# Usamos o .split() para criar uma lista de palavras
palavras = frase.split() 
# ['Aprendendo', 'Python', 'é', 'muito', 'legal']

# Agora pegamos a primeira palavra (índice 0 da lista)
print(palavras[0]) # Saída: Aprendendo
# Ou a última
print(palavras[-1]) # Saída: legal

