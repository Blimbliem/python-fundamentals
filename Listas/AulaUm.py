frutas = ["laranja", "banana", "maça"]

frutas_2 = []

letras = list("gabriel")

numeros = list(range(10))

carro  = ["hb20", 2027, "95km", "Manual"]

# indices normal 
print(frutas[1])

# indice negativo

print(frutas[-2])


# listas aninhadas - acesso direto

matriz = [
    [1,'a',2],
    [2,'b',3],
    [3,'c',4]
]

print(matriz [1])

print(matriz[0][2])

print(matriz [-2][-3])


#Fatiamento - passamos valor inicial ou final, e acessamos um conjunto de elementos.


lista = ['p','y','t','h','o','n']

print(lista[2:])

print(lista[:2])

print(lista[1:4])

print(lista[::])

print(lista[::2])

print(lista[::-1]) #espelhamento

# para verificar todos os valores dentro de uma lista?

carro = ["Gol", "Vectra", "Omega", "Corola"]

for i, carro  in enumerate(carro):
    print(f"{i}: {carro}")


# compressão de listas

# cria uma nova lista com base nos valores de uma lista existente ou gera uma nova lista aplicando alguma modificação nos elementos.

numeros = [1,39,20, 2,9,66,35]

pares = [i for i in numeros if i % 2 == 0]

print(pares)

numeros = [1,39,20, 2,9,66,35]

potenciaDois = [i ** 2 for i in numeros]

print(potenciaDois)