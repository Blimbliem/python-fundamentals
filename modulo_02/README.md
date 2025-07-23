## Operadores
### Operadores Aritméticos
- Executam operações matemáticas, como adição, subtração, etc.

### Precedência dos operadores
- Regra que indiax quais operações devem ser executadas primeiro. Isso é útil pois, ao analisar uma expressão, dependendo da order das operações o valor pode ser diferente.

A definição indica a seguinte ordem como a correta:
- Parêntesis;
- Expoêntes;
- Multiplicações e divisões (da esquerda para a direita);
- Soma e subtrações (da esquerda para a direita)

### Operadores de Comparação
- São operadores utilizados para comparar dois valores.

### Operadores de atribuição
- São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variavel.

### Operadores Lógicos
- São utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.
- Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.
EX:
op_comparacao + op_logico + op_comparacao...N...
- Uma boa prática é não deixar as comparações lógicas ficarem muito grandes. Neste caso o programador deve pensar em uma forma de quebrar, atribuir a alguma variável e posteriormente avaliar lógicamente. 

### Operadores de Identidade
- São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.
- Operador de identidade é o operador "is"
- Ex: objeto_a is objeto_b