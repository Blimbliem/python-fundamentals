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