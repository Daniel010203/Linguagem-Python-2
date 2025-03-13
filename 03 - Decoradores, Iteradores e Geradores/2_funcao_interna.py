def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()


principal()


# Explicação

'''
Este código demonstra o conceito de **funções aninhadas** em Python. 

Vamos analisar passo a passo:

1. **Definição da Função `principal()`:**
   * A função `principal()` é a função principal do código, que será executada primeiro.
   * Dentro dela, há duas funções aninhadas: `funcao_interna()` e `funcao_2()`.

2. **Funções Aninhadas:**
   * **`funcao_interna()`:** Imprime a mensagem "executando a funcao interna" na tela.
   * **`funcao_2()`:** Imprime a mensagem "executando a funcao 2" na tela.

3. **Chamadas das Funções:**
   * Dentro da função `principal()`, as funções aninhadas são chamadas:
     * `funcao_interna()` é chamada primeiro.
     * `funcao_2()` é chamada depois.

4. **Chamada da Função `principal()`:**
   * A última linha `principal()` chama a função `principal()`, iniciando a execução do código.

**Como o código funciona:**

1. Quando o script é executado, a função `principal()` é chamada.
2. Dentro de `principal()`, a mensagem "executando a funcao principal" é impressa.
3. Em seguida, `funcao_interna()` é chamada dentro de `principal()`, imprimindo "executando a funcao interna".
4. Após `funcao_interna()`, `funcao_2()` é chamada, imprimindo "executando a funcao 2".
5. A função `principal()` termina sua execução.

**Importância das Funções Aninhadas:**

* **Escopo:** As funções aninhadas têm acesso ao escopo da função externa onde foram definidas. Isso significa que elas podem acessar as variáveis da função principal.
* **Organização de Código:** As funções aninhadas podem ser usadas para organizar o código em blocos lógicos.
* **Reutilização:** As funções aninhadas podem ser reutilizadas dentro da função externa.

**Exemplo:**

```python
def principal():
    print("executando a funcao principal")
    x = 10  # Variável da função principal

    def funcao_interna():
        print("executando a funcao interna")
        print("Valor de x:", x)  # Acessando a variável da função principal

    funcao_interna()


principal()
```

Neste exemplo, a função `funcao_interna()` consegue acessar a variável `x` da função `principal()`.

'''