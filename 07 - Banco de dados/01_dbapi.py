import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])
print(f'Seja bem vindo ao sistema {cliente["nome"]}')

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Chappie", "chappie@gmail.com"),
#     ("Melaine", "melaine@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)

#Explicação  do código passo a passo. 😊

#1. **Conexão com o banco de dados:**
#    - Primeiro, o código cria uma conexão com um banco de dados SQLite chamado "meu_banco.sqlite".
#   - A biblioteca `sqlite3` é usada para interagir com o banco de dados.
#    - A variável `conexao` representa essa conexão.

#2. **Cursor:**
#    - Em seguida, o código cria um objeto `cursor` associado à conexão.
#    - O cursor é usado para executar comandos SQL no banco de dados.

#3. **Criação da tabela:**
#    - A função `criar_tabela` cria uma tabela chamada "clientes" no banco de dados.
#    - Essa tabela tem três colunas: "id" (chave primária), "nome" e "email".
#    - A instrução SQL para criar a tabela é executada pelo cursor.

#4. **Inserção de registros:**
#    - A função `inserir_registro` insere um novo registro na tabela "clientes".
#    - Ela recebe os parâmetros `nome` e `email`.
#    - Os dados são inseridos na tabela usando a instrução SQL `INSERT INTO`.

#5. **Atualização de registros:**
#    - A função `atualizar_registro` atualiza um registro existente na tabela.
#    - Ela recebe os parâmetros `nome`, `email` e `id`.
#    - A instrução SQL `UPDATE` é usada para modificar os valores na tabela.

#6. **Exclusão de registros:**
#    - A função `excluir_registro` remove um registro com base no `id`.
#    - A instrução SQL `DELETE FROM` é usada para excluir o registro.

#7. **Inserção de múltiplos registros:**
#    - A função `inserir_muitos` insere vários registros de uma vez.
#    - Ela recebe uma lista de dados e insere cada um na tabela.

#8. **Recuperação de cliente por ID:**
#    - A função `recuperar_cliente` busca um cliente específico com base no `id`.
#    - A instrução SQL `SELECT` é usada para recuperar os dados do cliente.

#9. **Listagem de clientes:**
#    - A função `listar_clientes` retorna todos os clientes ordenados pelo nome.
#    - Os resultados são iterados e impressos como dicionários.

#10. **Mensagem de boas-vindas:**
#    - Por fim, o código recupera o cliente com `id` igual a 2.
#    - Imprime os dados desse cliente e uma mensagem de boas-vindas personalizada.


#Fonte: conversa com o Copilot, 24/06/2024
#(1) Como Se Tornar um Desenvolvedor Python Júnior: Guia Completo e Dicas .... https://awari.com.br/como-se-tornar-um-desenvolvedor-python-junior-guia-completo-e-dicas-essenciais/.
#(2) Saiba o que faz um desenvolvedor Python! - XP Educação. https://blog.xpeducacao.com.br/carreira-desenvolvedor-python/.
#(3) Tudo em blocos: trabalhando com funções — Python Descomplicado. https://wmonteiro-ai.github.io/python-intro-ptbr/06-Funcoes.html.
#(4) Explorando Funções em Python: O Poder de Definir e Utilizar Funções. https://www.dio.me/articles/explorando-funcoes-em-python-o-poder-de-definir-e-utilizar-funcoes.
#(5) Desenvolvedor Python: o que faz, como ser, salário e melhores cursos. https://horadecodar.com.br/desenvolvedor-python/.
#(6) sqlite3 — DB-API 2.0 interface for SQLite databases - Python. https://docs.python.org/pt-br/3/library/sqlite3.html.
#(7) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://bing.com/search?q=fun%c3%a7%c3%b5es+do+c%c3%b3digo+Python+sqlite3.
#(8) Tutorial: Aplicação em Python + SQLite (Parte 02) | Raccoon Nina. https://raccoon.ninja/pt/post/dev/tutorial-aplicacao-em-python-sqlite-parte-02/.
#(9) Python SQLite3: Aprenda a utilizar o banco de dados SQLite3 com Python. https://awari.com.br/python-sqlite3-aprenda-a-utilizar-o-banco-de-dados-sqlite3-com-python/.
#(10) Domine o Python com SQLite: Tutorial completo de instalação e .... https://www.usandopy.com/pt/artigo/domine-o-python-com-sqlite-tutorial-completo-de-instalacao-e-configuracao-do-sqlite-no-python/.
#(11) undefined. https://www.sqlite.org.
#(12) undefined. https://www.w3schools.com/sql/.