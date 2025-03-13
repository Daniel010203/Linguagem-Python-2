from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)

# Explicação

'''
O código Python que você forneceu demonstra como criar objetos `datetime` com fusos horários personalizados, usando a classe `timezone` do módulo `datetime`.  Vamos analisá-lo passo a passo:

**1. Importações:**

```python
from datetime import datetime, timedelta, timezone
```

* Importa as classes `datetime`, `timedelta` e `timezone` do módulo `datetime`.
    * `datetime` para trabalhar com datas e horas.
    * `timedelta` para representar intervalos de tempo.
    * `timezone` para definir fusos horários personalizados.

**2. Criando Objetos `datetime` com Fusos Horários Personalizados:**

```python
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)
```

* `data_oslo = datetime.now(timezone(timedelta(hours=2)))`:
    * `timedelta(hours=2)`: Cria um objeto `timedelta` representando um intervalo de tempo de 2 horas.
    * `timezone(timedelta(hours=2))`: Cria um objeto `timezone` que representa um fuso horário 2 horas à frente do UTC (Tempo Universal Coordenado).
    * `datetime.now(timezone(timedelta(hours=2)))`: Obtém a data e hora atuais e aplica o fuso horário criado, resultando em um objeto `datetime` para Oslo, Noruega (UTC+2).
* `data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))`:
    * `timedelta(hours=-3)`: Cria um objeto `timedelta` representando um intervalo de tempo de -3 horas.
    * `timezone(timedelta(hours=-3))`: Cria um objeto `timezone` que representa um fuso horário 3 horas atrás do UTC.
    * `datetime.now(timezone(timedelta(hours=-3)))`: Obtém a data e hora atuais e aplica o fuso horário criado, resultando em um objeto `datetime` para São Paulo, Brasil (UTC-3).
* `print(data_oslo)`: Imprime a data e hora em Oslo.
* `print(data_sao_paulo)`: Imprime a data e hora em São Paulo.

**Em resumo, o código demonstra como:**

* Criar objetos `timezone` personalizados definindo um deslocamento em relação ao UTC usando `timedelta`.
* Aplicar esses fusos horários personalizados aos objetos `datetime` usando `datetime.now()`.

**Observações:**

* O código não utiliza a biblioteca `pytz`, mas sim a classe `timezone` do módulo `datetime` para definir fusos horários personalizados.
* O código assume que o sistema operacional já está configurado com a data e hora corretas.
* Em um sistema real, é importante usar a biblioteca `pytz` para garantir a precisão dos fusos horários, pois `pytz` fornece uma lista completa de fusos horários e lida com regras de horário de verão.

'''