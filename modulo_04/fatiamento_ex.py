registro = "USUARIO_123:MARIA_SILVA@GMAIL.COM"

# 1. Extrair apenas o ID (os 11 primeiros caracteres)
id_usuario = registro[:11] 
print(f"ID: {id_usuario}")

# 2. Extrair apenas o Provedor (os últimos 9 caracteres)
provedor = registro[-9:]
print(f"Domínio: {provedor}")

# 3. Extrair o Nome (está entre o ':' e o '@')
# O ':' está no índice 11 e o '@' no 23
nome = registro[12:23]
print(f"Nome no sistema: {nome}")


frase = "Aprendendo Python é muito legal"

#Ex1:Pegar apenas a palavra "Aprendendo"
ex1 = frase[:11]
print(ex1)

#Ex2:Pegar apenas a palavra "legal"
ex2 = frase[26:]
print(ex2)

#Ex3: Inverter a frase inteira.
ex3 = frase[::-1]
print(ex3)

#Ex4: Pegar a frase pulando de 3 em 3 caracteres (gerando um código "secreto")
cod_secreto = frase[::3]
print(cod_secreto)
