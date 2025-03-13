def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))

# Explicação

'''
Este código Python implementa uma calculadora simples usando funções aninhadas e a estrutura `match` para selecionar a operação desejada.

**Análise do código:**

1. **Função `calculadora(operacao)`:**
   * Esta função principal recebe um argumento `operacao`, que representa o operador matemático (+, -, *, /).
   * Dentro dela, são definidas quatro funções aninhadas: `soma`, `sub`, `mul` e `div`, que implementam as operações básicas de adição, subtração, multiplicação e divisão, respectivamente.
   * A instrução `match operacao` é usada para verificar o valor de `operacao` e retornar a função correspondente:
     * Se `operacao` for "+", a função `soma` é retornada.
     * Se `operacao` for "-", a função `sub` é retornada.
     * Se `operacao` for "*", a função `mul` é retornada.
     * Se `operacao` for "/", a função `div` é retornada.

2. **Chamadas da Função `calculadora()`:**
   * A linha `op = calculadora("+")` chama a função `calculadora` com o operador "+". A função `calculadora` retorna a função `soma` e atribui-a à variável `op`.
   * A linha `print(op(2, 2))` chama a função `op` (que agora é a função `soma`) com os argumentos 2 e 2, imprimindo o resultado da soma (4).
   * As linhas seguintes repetem o mesmo processo para os operadores "-", "*", e "/", executando as operações correspondentes.

**Em resumo:**

Este código demonstra uma forma de criar uma calculadora flexível usando funções aninhadas. A função `calculadora` age como uma fábrica de funções, retornando a função específica da operação desejada. Isso permite que o código seja mais organizado e reutilizável, já que a lógica de cada operação é encapsulada em uma função separada.

**Exemplo de uso:**

```python
op = calculadora("+")
resultado = op(5, 3)
print(resultado)  # Saída: 8
```

Neste exemplo, o código chama a função `calculadora` com o operador "+", obtendo a função `soma`. Em seguida, ele chama a função `soma` com os argumentos 5 e 3 e armazena o resultado na variável `resultado`, que é impresso na tela.

**Autor:** Bard, um modelo de linguagem grande.

'''