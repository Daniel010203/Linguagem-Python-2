from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)


# Explicação
'''
O código Python que você forneceu demonstra como trabalhar com datas, horas e datas e horas combinadas usando a biblioteca `datetime`. Vamos analisá-lo passo a passo:

**1. Importando Módulos:**

```python
from datetime import date, datetime, time
```

Essa linha importa as classes `date`, `datetime` e `time` do módulo `datetime`. Essas classes fornecem ferramentas para lidar com datas, horas e datas e horas combinadas em Python.

**2. Trabalhando com Datas:**

```python
data = date(2023, 7, 10)
print(data)
print(date.today())
```

* `data = date(2023, 7, 10)`: Cria um objeto `date` representando a data 10 de julho de 2023.
* `print(data)`: Imprime a data criada (`2023-07-10`).
* `print(date.today())`: Imprime a data atual (`AAAA-MM-DD`).

**3. Trabalhando com Datas e Horas:**

```python
data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())
```

* `data_hora = datetime(2023, 7, 10)`: Cria um objeto `datetime` representando 10 de julho de 2023, às 00:00:00 (meia-noite).
* `print(data_hora)`: Imprime a data e hora criada (`2023-07-10 00:00:00`).
* `print(datetime.today())`: Imprime a data e hora atuais (`AAAA-MM-DD HH:MM:SS`).

**4. Trabalhando com Horas:**

```python
hora = time(10, 20, 0)
print(hora)
```

* `hora = time(10, 20, 0)`: Cria um objeto `time` representando 10:20:00 (10 horas, 20 minutos, 0 segundos).
* `print(hora)`: Imprime a hora criada (`10:20:00`).

**Em resumo, o código demonstra como criar objetos de data, hora e data e hora em Python, imprimir suas representações e obter a data e hora atuais.**

**Observação:** O módulo `datetime` oferece uma variedade de métodos e atributos para trabalhar com datas e horas em Python. Você pode consultar a documentação oficial para explorar as funcionalidades completas: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html).

'''