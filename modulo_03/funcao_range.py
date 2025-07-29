# range object
range(4)

#convertendo o valor para list
list(range(4))

# utilizando range com for

for numero in range(0,11):
    print(numero, end=" ")
print()
  
# exibindo tabuada do 5
i = int(input("Digite o número que vc deseja saber a tabuada:"))

for numero in range (0, 101, i):
    print(numero, end=" ")
