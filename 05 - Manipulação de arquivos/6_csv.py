import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1


try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

# Explicação
'''
O código Python apresentado demonstra como usar a biblioteca `csv` para trabalhar com arquivos CSV, incluindo a criação, escrita e leitura de dados. Vamos analisá-lo passo a passo:

**1. Importações e definição do caminho raiz:**

```python
import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
```

* `import csv`: Importa o módulo `csv` para trabalhar com arquivos CSV.
* `from pathlib import Path`: Importa a classe `Path` do módulo `pathlib` para manipulação de caminhos de arquivos.
* `ROOT_PATH = Path(__file__).parent`: Define a variável `ROOT_PATH` como o caminho do diretório pai do arquivo atual.

**2. Definição de constantes:**

```python
COLUNA_ID = 0
COLUNA_NOME = 1
```

* `COLUNA_ID`: Constante que representa o índice da coluna "id" no arquivo CSV (0).
* `COLUNA_NOME`: Constante que representa o índice da coluna "nome" no arquivo CSV (1).

**3. Criação de um arquivo CSV ("usuarios.csv"):**

```python
try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
```

* `try: ... except IOError as exc:`: Tenta abrir o arquivo "usuarios.csv" no modo escrita ("w") com codificação UTF-8. Se ocorrer um erro de entrada/saída (`IOError`), o bloco `except` será executado.
* `with open(...) as arquivo:`: Usa o contexto `with` para garantir que o arquivo seja fechado automaticamente após a escrita, mesmo que ocorra um erro.
* `newline=""`: Evita a inserção de linhas em branco adicionais no arquivo CSV.
* `escritor = csv.writer(arquivo)`: Cria um objeto `csv.writer` para escrever dados no arquivo CSV.
* `escritor.writerow(["id", "nome"])`: Escreve o cabeçalho do arquivo CSV com as colunas "id" e "nome".
* `escritor.writerow(["1", "Maria"])` e `escritor.writerow(["2", "João"])`: Escreve duas linhas de dados no arquivo CSV, contendo os IDs e nomes dos usuários.

**4. Leitura de um arquivo CSV ("usuarios.csv") com acesso por índice:**

```python
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
```

* `try: ... except IOError as exc:`: Tenta abrir o arquivo "usuarios.csv" no modo leitura ("r") com codificação UTF-8. Se ocorrer um erro de entrada/saída (`IOError`), o bloco `except` será executado.
* `with open(...) as arquivo:`: Usa o contexto `with` para garantir que o arquivo seja fechado automaticamente após a leitura, mesmo que ocorra um erro.
* `leitor = csv.reader(arquivo)`: Cria um objeto `csv.reader` para ler dados do arquivo CSV.
* `for idx, row in enumerate(leitor):`: Itera sobre cada linha do arquivo CSV, obtendo o índice da linha (idx) e os dados da linha (row).
* `if idx == 0: continue`: Pula a primeira linha, pois ela contém o cabeçalho do arquivo.
* `print(f"ID: {row[COLUNA_ID]}")` e `print(f"Nome: {row[COLUNA_NOME]}")`: Imprime o ID e o nome do usuário de cada linha.

**5. Leitura de um arquivo CSV ("usuarios.csv") com acesso por chave:**

```python
try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
```

* `try: ... except IOError as exc:`: Tenta abrir o arquivo "usuarios.csv" no modo leitura. Se ocorrer um erro de entrada/saída (`IOError`), o bloco `except` será executado.
* `with open(...) as csvfile:`: Usa o contexto `with` para garantir que o arquivo seja fechado automaticamente após a leitura, mesmo que ocorra um erro.
* `reader = csv.DictReader(csvfile)`: Cria um objeto `csv.DictReader` para ler dados do arquivo CSV, onde cada linha é representada como um dicionário.
* `for row in reader:`: Itera sobre cada linha do arquivo CSV.
* `print(f"ID: {row['id']}")` e `print(f"Nome: {row['nome']}")`: Imprime o ID e o nome do usuário de cada linha, acessando os valores pelo nome da chave.

**Observações:**

* O código assume que o arquivo "usuarios.csv" já existe. Se não existir, a leitura do arquivo falhará.
* Você pode adicionar mais linhas de dados ao arquivo CSV usando o objeto `csv.writer` antes de fechar o arquivo.
* O módulo `csv` oferece diversas funções para manipular arquivos CSV, como a possibilidade de especificar delimitadores personalizados, tratar de linhas vazias e lidar com erros de conversão de dados.

Espero que essa explicação seja útil! 

'''