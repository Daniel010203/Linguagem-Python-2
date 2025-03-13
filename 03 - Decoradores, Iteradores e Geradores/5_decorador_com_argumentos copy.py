def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("João", 1000)
print(resultado)
print(ola_mundo)

# Explicação

'''

Este código demonstra um decorador mais completo, capaz de lidar com funções que recebem argumentos.

**Análise do código:**

1. **Definição do Decorador `meu_decorador(funcao)`:**
   * O decorador `meu_decorador` é definido como antes, recebendo uma função como argumento e retornando a função `envelope()`.
   * A função `envelope` agora recebe `*args` e `**kwargs` para poder lidar com qualquer número de argumentos posicionais e nomeados que a função original possa receber.
   * `envelope` imprime uma mensagem antes de executar a função original (`funcao`), e outra mensagem depois.
   * `envelope` chama a função original com os argumentos recebidos (`*args`, `**kwargs`) e armazena o resultado em `resultado`.
   * `envelope` retorna o resultado da função original.

2. **Definição da Função `ola_mundo(nome, outro_argumento)`:**
   * A função `ola_mundo` agora recebe dois argumentos: `nome` e `outro_argumento`.
   * Ela imprime uma saudação e retorna o nome em letras maiúsculas.

3. **Aplicação do Decorador `@meu_decorador`:**
   * O decorador `meu_decorador` é aplicado à função `ola_mundo` usando a sintaxe `@`.

4. **Chamada da Função Decorada:**
   * A linha `resultado = ola_mundo("João", 1000)` chama a função decorada `ola_mundo` com os argumentos "João" e 1000.
   * A função `envelope` é executada, imprimindo as mensagens antes e depois da execução de `ola_mundo`.
   * `envelope` retorna o resultado da função original (`ola_mundo`), que é o nome em letras maiúsculas ("JOÃO").
   * O resultado é armazenado na variável `resultado` e impresso na tela.

5. **Impressão de `ola_mundo`:**
   * A linha `print(ola_mundo)` imprime a função `ola_mundo` (que na verdade é a função `envelope` retornada pelo decorador). Isso mostra que a função decorada é a função `envelope`.

**Em resumo:**

Este código demonstra um decorador mais versátil, capaz de lidar com funções que recebem diferentes argumentos. Ele imprime mensagens antes e depois da execução da função original e retorna o resultado da função original. O uso do `@` torna a aplicação do decorador concisa e clara.

**Exemplo de saída:**

```
faz algo antes de executar
Olá mundo João!
faz algo depois de executar
JOÃO
<function meu_decorador.<locals>.envelope at 0x...>
```

**Autor:** Bard, um modelo de linguagem grande.

'''