## Módulo 03
### Identação e Blocos - Estetica
- Identar um código, isso para qualquer linguagem, é uma forma de manter o código fonte mais legível e manutenível.
- Em Python, a identação é elevada para outro nível, pois ela exerce o papel de dizer ao interpretador aonde um bloco de comando inicia e onde ele termina.
- Se o código não estiver identado corretamente, o programa não irá funcionar.

### Utilizando espaços
- Em Python, há uma convenção que define boas práticas para escrita de código na linguagem. Nesse documento, é indicado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

## Estrutras Condicionais
- Elas permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

### If
- Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada If. 
- O comando testa a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do If serão executadas.

### IF/ELSE
- Estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. 
- Se a expressão lógica do if for verdadeira o bloco do código do if será executado, caso contrário o bloco de código do else será executado.

### IF/ELIF/ELSE
- Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif;
- Elif é composto por uma nova expressão lógia, que será testada e caso retorne verdadeiro o bloco de código do elif será executado;
- Evite criar grandes estruturas condicionais, pois aumentam a complexidade do código.

### IF aninhado
- Pode criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de códigos de estrturas if/elif/else.

### IF ternário
- Ele permite escrever uma condição em uma única linha.
- Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

## Estruturas de Repetição
- São estruturas utilizadas para repetir um trecho de código em determinado número de vezes. Esse número de vezes pode ser conhecido previamente ou determinado através de uma expressão lógica.

### Comando for
- O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.
 
 ### Função Range
 - Range é uma função built-in do python, ela é usada para produzir uma sequência de números inteiros a partir de um inicio (inclusivo) para um fim (exclusivo). 
 - Ele recebe 3 argumentos: Stop (obtrigatório), Start(opcional) e Step (opcional).

### Comando While
- O comando while é usado para repetir um bloco de código várias vezes. 
- Ele é melhor utilizado quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

