def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


ola_mundo()

# Explicação

'''
Este código demonstra uma forma mais concisa e elegante de utilizar decoradores em Python, utilizando a sintaxe `@`.

**Análise do código:**

1. **Definição do Decorador `meu_decorador(funcao)`:**
   * O decorador `meu_decorador` é definido exatamente como no exemplo anterior, recebendo uma função como argumento e retornando a função `envelope()` que encapsula a função original.

2. **Aplicação do Decorador com `@`:**
   * A linha `@meu_decorador` é chamada de **sintaxe de decorador**. Ela aplica o decorador `meu_decorador` à função `ola_mundo` **antes mesmo de a função ser definida**. 
   * Essa sintaxe é um atalho para a linha `ola_mundo = meu_decorador(ola_mundo)`, que era usada no exemplo anterior.

3. **Definição da Função `ola_mundo()`:**
   * A função `ola_mundo` é definida normalmente, mas como ela foi decorada com `@meu_decorador`, o comportamento da função será modificado.

4. **Chamada da Função Decorada:**
   * A linha `ola_mundo()` chama a função `ola_mundo`, que agora está decorada com `meu_decorador`. 
   * A função `envelope` (retornada pelo decorador) é executada, imprimindo as mensagens "faz algo antes de executar" e "faz algo depois de executar" antes e depois da execução da função original `ola_mundo`.

**Em resumo:**

A sintaxe `@` torna a aplicação de decoradores mais clara e concisa. Em vez de atribuir a função decorada a uma nova variável, você simplesmente coloca o decorador acima da definição da função. Isso torna o código mais legível e organizado.

**Exemplo de saída:**

```
faz algo antes de executar
Olá mundo!
faz algo depois de executar
```

**Autor:** Bard, um modelo de linguagem grande.


'''