from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)

# Explicação
'''
O código Python apresentado demonstra o uso de blocos `try...except` para lidar com erros ao abrir e ler arquivos, incluindo o tratamento de codificação de caracteres. Vamos analisá-lo passo a passo:

**1. Importações e definição do caminho raiz:**

```python
from pathlib import Path

ROOT_PATH = Path(__file__).parent
```

* `from pathlib import Path`: Importa a classe `Path` do módulo `pathlib`, que fornece uma maneira mais orientada a objetos para trabalhar com caminhos de arquivos.
* `ROOT_PATH = Path(__file__).parent`: Define a variável `ROOT_PATH` como o caminho do diretório pai do arquivo atual.

**2. Leitura de um arquivo (1lorem.txt):**

```python
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
```

* `try: ... except IOError as exc:`: Tenta abrir o arquivo "1lorem.txt" no modo leitura ("r") e imprimir seu conteúdo. Se ocorrer um erro de entrada/saída (`IOError`), como o arquivo não existir ou não ter permissões de leitura, o bloco `except` será executado.
* `with open(...) as arquivo:`: Usa o contexto `with` para garantir que o arquivo seja fechado automaticamente após o término da leitura, mesmo que ocorra um erro.
* `print(arquivo.read())`: Lê todo o conteúdo do arquivo e imprime na tela.

**3. Bloco comentado (para fins de ilustração):**

```python
# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")
```

Este bloco comentado demonstra como escrever dados em um arquivo com codificação UTF-8. 

**4. Leitura de um arquivo com codificação UTF-8 (arquivo-utf-8.txt):**

```python
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
```

* `try: ... except IOError as exc: ... except UnicodeDecodeError as exc:`: Tenta abrir o arquivo "arquivo-utf-8.txt" no modo leitura ("r") com codificação UTF-8 e imprimir seu conteúdo. Se ocorrer um erro de entrada/saída (`IOError`) ou um erro de decodificação de caracteres (`UnicodeDecodeError`), o bloco `except` correspondente será executado.
* `encoding="utf-8"`: Especifica a codificação UTF-8 para a leitura do arquivo.
* `print(arquivo.read())`: Lê todo o conteúdo do arquivo e imprime na tela.

**Explicação detalhada dos erros:**

* **IOError:** Ocorre quando há um erro de entrada/saída genérico, como o arquivo não existir, não ter permissões de leitura, ou o disco estar cheio.
* **UnicodeDecodeError:** Ocorre quando o arquivo está codificado em um formato diferente do especificado na opção `encoding`. Se o arquivo não estiver codificado em UTF-8, mas a leitura foi configurada para UTF-8, esse erro pode ocorrer.

**Observações:**

* O código assume que os arquivos "1lorem.txt" e "arquivo-utf-8.txt" existem no mesmo diretório do arquivo Python que está sendo executado.
* É importante especificar a codificação UTF-8 ao abrir e ler arquivos que contenham caracteres Unicode, como acentos ou caracteres especiais. Caso contrário, você pode encontrar erros de decodificação.
* Usar o contexto `with` para abrir arquivos é uma boa prática que garante o fechamento automático do arquivo, mesmo que ocorra um erro, evitando vazamentos de recursos.
* Se você precisar escrever dados em um arquivo com uma codificação específica, use o argumento `encoding` na função `open()`, como mostrado no bloco comentado.

Espero que essa explicação seja útil! 



'''