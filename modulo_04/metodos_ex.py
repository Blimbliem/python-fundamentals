# --- DADOS INICIAIS (Não altere estas variáveis) ---
usuario_bruto = "  marianA SILVA  "


# --- DESAFIO 1: Limpeza de Nome ---
# Objetivo: Deixar o nome sem espaços extras e com a primeira letra de cada nome maiúscula.
# Dica: Use métodos encadeados (um seguido do outro).
nome_limpo = usuario_bruto.strip().title() 
print(f"Usuário: {nome_limpo}")

# --- DESAFIO 2: Centralização de Título ---
# Objetivo: Criar um cabeçalho chamado "RELATÓRIO DE VENDAS" com 40 caracteres de largura.
# O preenchimento deve ser o caractere "="
# Dica: Use o método .center()
titulo = "RELATÓRIO DE VENDAS"
# ESCREVA SEU CÓDIGO AQUI:
cabecalho = print(titulo.center(40,"="))


# --- DESAFIO 3: Listagem de Produtos ---
# Objetivo: Transformar a lista 'produtos_lista' em uma única string separada por " | ".
# Dica: Use o método .join()
# Saída esperada: "Caderno | Caneta | Borracha | Régua"
# ESCREVA SEU CÓDIGO AQUI:
produtos_lista = ["Caderno", "Caneta", "Borracha", "Régua"]
string_produtos = print(f" | ".join(produtos_lista))

# --- DESAFIO 4: Manipulação de Data ---
# Objetivo: O sistema agora precisa da data no formato americano (Ano-Mês-Dia).
# 1. Use .split() para separar a data atual pela barra "/"
# 2. Use .join() com o traço "-" para juntar na ordem inversa (se conseguir) ou apenas juntar.
# ESCREVA SEU CÓDIGO AQUI:

data_hoje = "19/12/2025"

partes_data = (data_hoje.split('/'))
data_invertida = partes_data[::-1] 
data_formatada = ("-".join(data_invertida))
print(f"Data formatada: {data_formatada}")

# --- DESAFIO 5: Padronização de Comandos ---
# Objetivo: O programa deve perguntar "Deseja salvar? (S/N)". 
# O usuário pode digitar "s", "S", " sim " ou "SIM".
# Use .strip() e .upper() para garantir que a resposta seja sempre comparada como "S" ou "SIM".
resposta = "  sim  " # Simulação de entrada do usuário
# ESCREVA SEU CÓDIGO AQUI:
confirmacao = resposta.strip().upper()
print(f"Resposta padronizada: {confirmacao}")