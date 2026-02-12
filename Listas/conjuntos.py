# conjuntos são conhecidos como sets

# é uma coleção que não possui objetos repetidos, usamos o set para represnetar conjuntos matematicos ou para eliminar itens duplicados de um iteravel

conjunto = set([1,2,3,1,3,4,5,6,6,7])

print(conjunto)

# declaração implicita com "{}"
linguagens = {"python", "java", "c#", "python"}
print(linguagens)

# para acessar os dados de um conjunto (set), você precisa transforma-lo em uma lista

numeros = {0,1,2,4,6,7}

#TypeError: 'set' object is not subscriptable
# print(numeros[4])

numeros = list(numeros)

print(numeros)

# você pode percorrer um conjunto

carros = {"gol", "onix", "argo"}

for i in carros:
    print(i)

# provavlemente, dentro do metodo, ele transforma o set em lista
for indice, i in enumerate(carros):
     print(f"{indice}: {i}") 

#métodos

#union

conjuntoA = {'a','b'}
conjuntoB = {'c','d'}

print(conjuntoA.union(conjuntoB))

#intersection
conjuntoC = {1,3,5}
conjuntoD = {1,2,3}

print(conjuntoC.intersection(conjuntoD))

#difference
conjuntoE = {1,3,5}
conjuntoF = {1,2,3}

print(conjuntoE.difference(conjuntoF))
print(conjuntoF.difference(conjuntoE))