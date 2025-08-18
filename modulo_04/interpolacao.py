# old style %
nome = "joao"
idade = 34
profissao = "enfermeiro"
setor = "UTI"

print("Olá, eu me chamo %s. Eu tenho %d anos. Trabalho como %s. Meu setor é a %s." % (nome,idade,profissao,setor)) # é importante manter a ordem das variáveis

# método format
nome = "Rogerio"
idade = 50
profissao = "Médico"
setor = "PA"

print("Olá, eu me chamo {}. Eu tenho {} anos. Trabalho como {}. Meu setor é a {}.".format(nome,idade,profissao,setor)) 


print("Olá, eu me chamo {3}. Eu tenho {2} anos. Trabalho como {0}. Meu setor é a {1}.".format(nome,idade,profissao,setor)) # você adiciona a posição que deve ser colocada a variavel


print("Olá, eu me chamo {nome}. Eu tenho {idade} anos. Trabalho como {profissao}. Meu setor é a {setor}.".format(nome = nome,idade = idade ,profissao = profissao,setor = setor)) # você pode passar o valor da variavel dentro das chaves 


dados = {"nome1: Gabriel", "idade1: 22" , "profissao1: analista de sistemas", "setor1: Pós-pago"}

print("Olá, eu me chamo {nome1}. Eu tenho {idade1} anos. Trabalho como {profissao1}. Meu setor é a {setor1}.".format(**dados)) # você pode passar o valor da variavel dentro das chaves 

# print f
nome = "Moises"
idade = 1500
profissao = "profeta"
setor = "deserto"

print(f"Olá, eu me chamo {nome}. Eu tenho {idade} anos. Trabalho como {profissao}. Meu setor é a {setor}.")