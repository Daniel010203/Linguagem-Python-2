# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()


# Explicação
'''
O código Python apresentado demonstra diferentes maneiras de ler dados de um arquivo de texto chamado "lorem.txt". Vamos analisá-lo passo a passo:

**1. Abertura do arquivo e leitura completa:**

```python
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()
```

* `open(...)`: Abre o arquivo "lorem.txt" no modo leitura ("r"). O caminho completo do arquivo deve ser fornecido.
* `arquivo.read()`: Lê todo o conteúdo do arquivo como uma única string e a imprime na tela.
* `arquivo.close()`: Fecha o arquivo após a leitura.

**2. Leitura de uma linha:**

```python
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()
```

* `arquivo.readline()`: Lê apenas a primeira linha do arquivo e a imprime na tela. 

**3. Leitura de todas as linhas em uma lista:**

```python
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()
```

* `arquivo.readlines()`: Lê todas as linhas do arquivo e as armazena em uma lista, que é então impressa na tela.

**4. Leitura linha a linha com loop:**

```python
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
```

* `while len(linha := arquivo.readline()):`:  
    * Usa a atribuição de expressão para ler uma linha do arquivo e atribuí-la à variável `linha` dentro do loop `while`.
    * A condição `len(linha)` verifica se a linha lida é vazia (indicando o fim do arquivo). Se a linha não for vazia, o loop continua.
* `print(linha)`: Imprime cada linha lida na tela.

**Observação:** É fundamental fechar o arquivo após a leitura para evitar erros e liberar os recursos do sistema. A maneira mais segura de fazer isso é usando o comando `with open(...) as arquivo:` que garante o fechamento automático do arquivo, mesmo que ocorra um erro.

**Exemplo de uso:**

Se o arquivo "lorem.txt" contém o seguinte texto:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

O código imprimirá o seguinte:

**Exemplo 1:**

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

**Exemplo 2:**

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

**Exemplo 3:**

```
['Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n']
```

**Exemplo 4:**

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

'''