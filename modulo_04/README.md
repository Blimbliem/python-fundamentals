## Strings
### Métodos uteis
- Em Python a classe string tem vários métodos e utilitários que a tornam uma linguagem mais fácil de se trabalhar.

- Método Upper: Deixa todas as letras da string em maiusculo;
- Método Lower: Deixa todas as letras da string em minusculo;
- Método Title: Deixa somente a primeira letra em maiusculo;
- Método strip: Retira todos os espaços da string;
- Método lstrip: Retira os espaços do lado esquerdo da string;
- Método rstrip: Retira os espaços do lado direito da string;
- Método center: Centraliza o conteúdo da string;
- Método join: O inverso do split. Ele pega uma lista de strings e as une em uma única string, usando a string que chama o método como separador.
- Método split: Divide uma string em uma lista de strings, baseando-se em um separador (o padrão é o espaço em branco).
- Slicing [início:fim:passo] : Quando você usa [::-1], você está dizendo: "Comece do início, vá até o fim, mas caminhe com um passo de -1 (ou seja, de trás para frente)".;

### Interpolação de variáveis
- Há 3 formas de interpolar variáveis em python:

- 1- Utilizando o sinal de "%", utiliza-se "%s" quando queremos utilizar o valor tipo string, "%d" para valores do tipo inteiro e "%f" para valores ponto flutuante.Está em desuso.

- 2- Utilizando o método "format". É uma "evolução do oldstyle";

- 3 - Utilizando "f strings";

### Fatiamento de strings
- É uma técnica utilizada para retornar substrings (partes da string original), informando inicio, fim e passo: [start: stop,[step]];
- Imagine que a String é uma régua e cada caractere ocupa exatamente 1 centímetro dessa régua;
- Aceita índices negativos para contar de trás para frente;
- No fatiamento [início : fim], o índice de fim não é incluído no resultado;

### Dica:
- Contar caracteres um por um pode ser cansativo se a frase for muito longa. Em Python, podemos combinar o que aprendemos para facilitar o fatiamento.

- Utilizar o método split para remover o espaço em branco e criar um dicionario com as palavras separadas pelo espaço em branco. Exemplo na aula.
