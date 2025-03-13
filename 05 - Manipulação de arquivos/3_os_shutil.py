import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")


# Explique
'''
O código Python apresentado demonstra várias operações relacionadas à manipulação de arquivos e diretórios. Vamos analisá-lo passo a passo:

**1. Importações:**

```python
import os
import shutil
from pathlib import Path
```

* `os`: Módulo que fornece funções para interagir com o sistema operacional, como criação de diretórios e arquivos, renomeação e exclusão.
* `shutil`: Módulo que fornece funções de nível superior para operações de arquivos, como cópia e movimentação.
* `pathlib`: Módulo que fornece uma forma mais orientada a objetos para trabalhar com caminhos de arquivos.

**2. Definição do caminho raiz:**

```python
ROOT_PATH = Path(__file__).parent
```

* `Path(__file__)`: Obtém o caminho absoluto do arquivo atual (o arquivo Python que está sendo executado).
* `parent`: Obtém o diretório pai do arquivo atual. 
* `ROOT_PATH`: Variável que armazena o caminho raiz do projeto.

**3. Criação de um diretório:**

```python
os.mkdir(ROOT_PATH / "novo-diretorio")
```

* `os.mkdir(...)`: Cria um novo diretório chamado "novo-diretorio" dentro do caminho raiz do projeto.
* `ROOT_PATH / "novo-diretorio"`: Combina o caminho raiz com o nome do novo diretório usando o operador `/` do Pathlib.

**4. Criação de um arquivo:**

```python
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()
```

* `open(...)`: Abre um novo arquivo chamado "novo.txt" no modo escrita ("w"). Se o arquivo já existir, ele será sobrescrito.
* `ROOT_PATH / "novo.txt"`: Combina o caminho raiz com o nome do arquivo.
* `arquivo.close()`: Fecha o arquivo.

**5. Renomeação de um arquivo:**

```python
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")
```

* `os.rename(...)`: Renomeia o arquivo "novo.txt" para "alterado.txt".
* `ROOT_PATH / "novo.txt"`: Caminho do arquivo original.
* `ROOT_PATH / "alterado.txt"`: Novo nome do arquivo.

**6. Exclusão de um arquivo:**

```python
os.remove(ROOT_PATH / "alterado.txt")
```

* `os.remove(...)`: Exclui o arquivo "alterado.txt".
* `ROOT_PATH / "alterado.txt"`: Caminho do arquivo a ser excluído.

**7. Movimentação de um arquivo:**

```python
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
```

* `shutil.move(...)`: Move o arquivo "novo.txt" para dentro do diretório "novo-diretorio".
* `ROOT_PATH / "novo.txt"`: Caminho do arquivo original.
* `ROOT_PATH / "novo-diretorio" / "novo.txt"`: Novo caminho do arquivo.

**Resumo:**

O código cria um novo diretório, um novo arquivo, renomeia o arquivo, exclui o arquivo renomeado, e finalmente move o arquivo original para dentro do diretório recém-criado.

**Observação:**

* O código pressupõe que o arquivo "novo.txt" existe após a criação. Caso contrário, a renomeação e a movimentação falharão.
* É recomendável usar a estrutura `with open(...) as arquivo:` para garantir que o arquivo seja fechado automaticamente, mesmo que ocorra um erro.
* O módulo `pathlib` fornece uma maneira mais segura e concisa de trabalhar com caminhos de arquivos, evitando erros relacionados a barras invertidas e diretórios diferentes.

Espero que essa explicação seja útil! 

'''