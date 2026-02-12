#  Método append.
lista = []

# a lista pode armazenar qualquer objeto
lista.append(1)
lista.append("python")
lista.append([40,30,20])

print(lista)

#método copy
l2 = lista.copy() # como se fosse um backup
print(l2)

print(id(lista),id(l2))

#método clear
lista.clear()

print(lista)


#método count - quantas vezes objeto aparece na lista

cores = ["vermelho", "azul", "verde", "verde"]

print(cores.count("verde"))


#extend + atribui mais de um objeto para lista

linguagens = ["pyrhon", "js", "c#"]

print(linguagens)

linguagens.extend(["java", "node"])

print(linguagens)

#index

print(linguagens.index("java"))

print(linguagens.index("node"))

#pop - remove os elementos de cima para baixo.

linguagens.pop()
linguagens.pop()

print(linguagens)

#remove - remove as ocorrencias do elemento

linguagens.remove("c#")
print(linguagens)

#reverse faz o espelhamento da lista

linguagens.reverse()
print(linguagens)
