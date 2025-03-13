def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))


# Explicação
'''
Este código Python demonstra um conceito fundamental chamado **funções de primeira classe**. Isso significa que as funções podem ser tratadas como qualquer outra variável, como números ou strings. 

Vamos analisar passo a passo:

**1. Definição das Funções:**

* **`mensagem(nome)`:**
    * Imprime "executando mensagem" na tela.
    * Retorna a string formatada "Oi {nome}" (substituindo "{nome}" pelo valor passado como argumento).
* **`mensagem_longa(nome)`:**
    * Imprime "executando mensagem longa" na tela.
    * Retorna a string formatada "Olá tudo bem com você {nome}?" (substituindo "{nome}" pelo valor passado como argumento).

**2. Função `executar(funcao, nome)`:**

* Recebe duas variáveis como argumento:
    * `funcao`: uma função (neste caso, `mensagem` ou `mensagem_longa`).
    * `nome`: uma string (no exemplo, "Joao").
* Imprime "executando executar" na tela.
* Chama a função passada como argumento (`funcao`) com o argumento `nome`, e retorna o resultado.

**3. Chamadas das Funções:**

* `print(executar(mensagem, "Joao"))`:
    * Chama a função `executar` com as funções `mensagem` e o nome "Joao" como argumentos.
    * `executar` chama a função `mensagem` com "Joao", que retorna "Oi Joao".
    * A função `print` exibe "Oi Joao" na tela.
* `print(executar(mensagem_longa, "Joao"))`:
    * Chama a função `executar` com as funções `mensagem_longa` e o nome "Joao" como argumentos.
    * `executar` chama a função `mensagem_longa` com "Joao", que retorna "Olá tudo bem com você Joao?".
    * A função `print` exibe "Olá tudo bem com você Joao?" na tela.

**Em resumo:**

O código demonstra como funções podem ser passadas como argumentos para outras funções, tornando o código mais flexível e reutilizável. A função `executar` pode ser usada para executar qualquer função que receba um nome como argumento.

**Benefícios da utilização de funções de primeira classe:**

* **Reutilização de código:** A função `executar` pode ser usada com qualquer função que receba um nome como argumento.
* **Flexibilidade:** O comportamento do programa pode ser modificado sem alterar o código principal.
* **Abstração:** O código fica mais limpo e fácil de entender.

'''