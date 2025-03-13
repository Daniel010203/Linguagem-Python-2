def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


def ola_mundo():
    print("Olá mundo!")


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

# explicação
'''
Este código demonstra o uso de **decoradores** em Python, uma técnica para modificar o comportamento de funções sem alterá-las diretamente. 

Vamos analisar passo a passo:

1. **Definição do Decorador `meu_decorador(funcao)`:**
   * O decorador `meu_decorador` recebe uma função como argumento (`funcao`).
   * Ele define uma função aninhada `envelope()`. 
   * `envelope()` imprime uma mensagem antes de executar a função passada (`funcao`) e outra mensagem depois.
   * O decorador retorna a função `envelope()`.

2. **Definição da Função `ola_mundo()`:**
   * Esta função simplesmente imprime a mensagem "Olá mundo!".

3. **Aplicação do Decorador:**
   * A linha `ola_mundo = meu_decorador(ola_mundo)` aplica o decorador `meu_decorador` à função `ola_mundo`. Isso significa que a função `ola_mundo` será decorada, ou seja, o seu comportamento será modificado.
   * A atribuição `ola_mundo = ...` reatribui o nome `ola_mundo` para a função `envelope` retornada pelo decorador, que agora encapsula a função original.

4. **Chamada da Função Decorada:**
   * A linha `ola_mundo()` chama a função `ola_mundo`, que agora é a função `envelope` decorada.
   * `envelope` executa as seguintes ações:
     * Imprime "faz algo antes de executar".
     * Chama a função original `ola_mundo`, imprimindo "Olá mundo!".
     * Imprime "faz algo depois de executar".

**Em resumo:**

O código demonstra como um decorador pode ser usado para adicionar código antes e depois da execução de uma função, sem alterar diretamente o código da função original. Isso permite que você adicione funcionalidades como registro de logs, validação de entrada ou tratamento de erros a uma função de forma modular e reutilizável.

**Exemplo de saída:**

```
faz algo antes de executar
Olá mundo!
faz algo depois de executar
```

**Autor:** Bard, um modelo de linguagem grande.


'''