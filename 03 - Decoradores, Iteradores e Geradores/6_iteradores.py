class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)

# Explicação
'''
Este código demonstra a implementação de um iterador personalizado em Python, chamado `MeuIterador`, que dobra cada número em uma lista fornecida.

**Análise do código:**

1. **Definição da Classe `MeuIterador`:**
    * A classe `MeuIterador` é definida para representar um iterador personalizado.
    * **`__init__(self, numeros: list[int])`:**
        * O método construtor `__init__` recebe uma lista de inteiros `numeros` como argumento.
        * Ele inicializa os atributos `self.numeros` (armazenando a lista de números) e `self.contador` (inicializado com 0, para acompanhar a posição atual na lista).
    * **`__iter__(self)`:**
        * O método `__iter__` é chamado pelo loop `for` para obter um iterador.
        * Ele retorna a própria instância da classe `MeuIterador`, pois a própria instância já implementa o protocolo de iterador.
    * **`__next__(self)`:**
        * O método `__next__` é chamado pelo loop `for` a cada iteração.
        * Ele tenta acessar o próximo número da lista `self.numeros` usando `self.numeros[self.contador]`.
        * Se o índice estiver dentro dos limites da lista, ele retorna o número * 2 (dobrado).
        * Ele incrementa o contador `self.contador` para a próxima iteração.
        * Se o índice estiver fora dos limites da lista (IndexError), ele lança a exceção `StopIteration` para sinalizar o fim da iteração.

2. **Criação do Iterador e Loop `for`:**
    * A linha `MeuIterador(numeros=[38, 13, 11])` cria uma instância da classe `MeuIterador` com a lista `[38, 13, 11]` como argumento.
    * O loop `for` itera sobre o iterador criado, chamando o método `__next__` da instância de `MeuIterador` a cada iteração.
    * O loop `for` imprime cada valor retornado por `__next__` (os números da lista dobrados).

**Em resumo:**

O código demonstra como criar um iterador personalizado usando as funções especiais `__iter__` e `__next__`. O loop `for` pode iterar sobre esse iterador, chamando o método `__next__` para obter os próximos elementos. Neste caso, o iterador dobra cada número da lista fornecida.

**Exemplo de saída:**

```
76
26
22
```

**Autor:** Bard, um modelo de linguagem grande.

'''