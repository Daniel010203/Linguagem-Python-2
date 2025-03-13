import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))


#Explicação do código passo a passo. 😊

#1. **Conexão com o banco de dados:**
#    - Primeiro, o código importa o módulo `sqlite3`, que fornece uma interface para trabalhar com bancos de dados SQLite em Python¹.
#    - A variável `ROOT_PATH` é definida como o diretório pai do arquivo atual (onde o script está sendo executado).
#    - A linha `conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")` cria uma conexão com o banco de dados SQLite chamado "meu_banco.sqlite".
#    - Essa conexão permite interagir com o banco de dados, executar consultas e transações.

#2. **Cursor:**
#    - O objeto `cursor` é criado a partir da conexão.
#    - O cursor é usado para executar comandos SQL no banco de dados.
#    - A linha `cursor.row_factory = sqlite3.Row` configura o cursor para retornar os resultados como objetos do tipo `Row`, que permitem acessar as colunas por nome.

#3. **Entrada do usuário:**
#    - O código solicita ao usuário que informe o `id` de um cliente.
#    - O valor inserido pelo usuário é armazenado na variável `id_cliente`.

#4. **Consulta SQL:**
#    - A linha `cursor.execute(f\"SELECT * FROM clientes WHERE id={id_cliente}\")` executa uma consulta SQL na tabela "clientes".
#    - Ela busca todos os registros cujo `id` corresponde ao valor fornecido pelo usuário.
#    - Os resultados são armazenados na variável `clientes`.

#5. **Iteração e impressão:**
#    - O loop `for cliente in clientes:` itera sobre cada registro encontrado.
#    - A função `dict(cliente)` converte o objeto `Row` em um dicionário, facilitando o acesso aos valores das colunas.
#    - Os dados do cliente são impressos no formato de dicionário.



#Fonte: conversa com o Copilot, 24/06/2024
#(1) sqlite3 — DB-API 2.0 interface for SQLite databases - Python. https://docs.python.org/pt-br/3/library/sqlite3.html.
#(2) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://bing.com/search?q=fun%c3%a7%c3%b5es+do+c%c3%b3digo+Python+sqlite3.
#(3) Tutorial: Aplicação em Python + SQLite (Parte 02) | Raccoon Nina. https://raccoon.ninja/pt/post/dev/tutorial-aplicacao-em-python-sqlite-parte-02/.
#(4) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://awari.com.br/python-sqlite3-aprenda-a-utilizar-o-banco-de-dados-sqlite3-com-python/.
#(5) Domine o Python com SQLite: Tutorial completo de instalação e .... https://www.usandopy.com/pt/artigo/domine-o-python-com-sqlite-tutorial-completo-de-instalacao-e-configuracao-do-sqlite-no-python/.
#(6) undefined. https://www.sqlite.org.
#(7) undefined. https://www.w3schools.com/sql/.