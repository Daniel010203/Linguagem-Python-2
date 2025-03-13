import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("DELETE FROM clientes WHERE id = 8;")
    conexao.commit()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()


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

#3. **Exclusão de registro:**
#    - O bloco `try` inicia uma transação.
#    - A linha `cursor.execute("DELETE FROM clientes WHERE id = 8;")` exclui o registro com `id` igual a 8 da tabela "clientes".
#    - A instrução SQL `DELETE FROM` é usada para remover registros.
#    - Se a operação for bem-sucedida, a transação é confirmada com `conexao.commit()`.

#4. **Inserção de registros:**
#    - Duas inserções são realizadas:
#        - `INSERT INTO clientes (nome, email) VALUES (?,?)` insere um novo cliente com nome "Teste 3" e email "teste3@gmail.com".
#        - `INSERT INTO clientes (id, nome, email) VALUES (?,?,?)` insere outro cliente com `id` 2, nome "Teste 4" e email "teste4@gmail.com".
#    - Os valores são passados como parâmetros para evitar problemas de segurança (SQL injection).

#5. **Tratamento de exceções:**
#    - O bloco `except` captura qualquer exceção que ocorra durante as operações.
#    - Se houver um erro, a transação é revertida com `conexao.rollback()`.
#    - Uma mensagem de erro é impressa com detalhes sobre a exceção.


#[edge browser](#message)
#The user has the page open in a Microsoft Edge browser window whose metadata is:
#```json
#<EMPTY>

#Fonte: conversa com o Copilot, 24/06/2024
#(1) sqlite3 — DB-API 2.0 interface for SQLite databases - Python. https://docs.python.org/pt-br/3/library/sqlite3.html.
#(2) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://bing.com/search?q=fun%c3%a7%c3%b5es+do+c%c3%b3digo+Python+sqlite3.
#(3) Tutorial: Aplicação em Python + SQLite (Parte 02) | Raccoon Nina. https://raccoon.ninja/pt/post/dev/tutorial-aplicacao-em-python-sqlite-parte-02/.
#(4) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://awari.com.br/python-sqlite3-aprenda-a-utilizar-o-banco-de-dados-sqlite3-com-python/.
#(5) Domine o Python com SQLite: Tutorial completo de instalação e .... https://www.usandopy.com/pt/artigo/domine-o-python-com-sqlite-tutorial-completo-de-instalacao-e-configuracao-do-sqlite-no-python/.
#(6) undefined. https://www.sqlite.org.
#(7) undefined. https://www.w3schools.com/sql/.