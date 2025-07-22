# python-fundamentals
Guardando todo o aprendizado para obter uma boa fundamentação em python.

## Aula 01
### Tipos de dados
### Por que utilizamos tipos?
Os tipos servem para definir as caracteristicas e comportamentos de um valor (objeto) para o interpretador. Por exemplo: com certos tipos eu consigo realizar operações matematicas, com outros não é possível.

### Tipos built-in (aqueles já vem na linguagem):

|Texto    | str                         |
|Numerico | int, float, complex         |
|Sequência| list, tuple, range          |
|Mapa     | dict                        |
|Coleção  | set, frozenset              |
|Booleano | bool                        |
|Binário  | bytes, bytearray, memoryview|

### Números inteiros
Representados pela classe int e possuem precisão ilimitada. Ex: 1, 10, -1, -100, 90870...

### Números de ponto flutuante
São usados para representar os números racionais e sua implementação é feita pela classe float. Ex: 1.5, -17.764, 3.14, -54.43295723,...

### Booleano
É utilizado para representar verdadeiro ou falso, e é implementado pela classe bool. Em Python o tipo booleano é uma subclasse do int. 0 é falso e qualquer número diferente de 0 é verdadeiro. Ex: True e False

### Strings 
São utilizadas para representar valores alfanúmericos. São definidas dentro da classe str.Ex: "Pyton", 'py',"""pyth""",'''piton'''.

### Dicas VScode
Ao implementar uma classe por exemplo "int()", se segurarmos a tecla CRTL em cima da classe o VScode abre uma aba de ajuda.

## Aula 02
### Modo interativo
O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever o código e ver o resultado na hora.

### Iniciando modo interativo:
1 - Chamar o interpretador (python)
2 - Executando o script com a flag -i (python -i app.py)

### dir
O metodo "dir", utilizado no terminal, sem argumentos, retorna a lista de nomes do escopo local. Com argumentos, retorna uma lista de atributos validos para o objeto. Ex: dir(), dir(20);

### help
Invoca o sistema de ajuda integrado da linguagem. Ele nos diz quais são os argumentos que tal atributo recebe, o que ele retorna, como ele funciona de fato. Ex:help() help (20)

### Variáveis
São valores que podem sofrer alterações no decorrer da execução do programa.
Não é necessário definir o tipo de dados da variável, pois o python faz isso automáticamente para nós. 
Não pode ser criado uma variavel sem atribuir um valor

Um exemplo disso pode ser encontrado no arquivo "variaveis.py"

### Constantes
Não existe palavra reservada em python para informar ao interpretador que o valor é constante. Porém em Python há uma convenção que diz ao programador que tal variável é uma constante, e nesse caso é quando uma variável contém seu nome todo em letras maiúsculas. 

### Boas praticas
- O padrão de nomes de ser snake case (camelCase não é utilizado em python);
- Escolher nomes sugestivos;
- Nome de constantes todo em maiúsculo.


## Aula 03 - Conversão de tipos
- Em alguns momentos será necessário converter o tipo de uma variavel para manipular de forma forma diferente. 
Ex:
- Variaveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

## Aula 04 - Funções de entrada e saída
### Função input
- É utilizada quando queremos ler dados da entrada padrão. Ela recebe um argumento do tipo String, que é exibido para o usuário na saída padrão. Resumidamente, a função lê a entrada, converte para string e retorna o valor.

### Função Print
- É utilizada quando queremos exibir dados na saída padrão. Ela recebe um argumento obrigatório do tipo "varargs" de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida ao usuário.