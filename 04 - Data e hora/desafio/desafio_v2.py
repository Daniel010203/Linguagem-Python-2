import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(
        cliente=cliente, numero=numero_conta, limite=500, limite_saques=50
    )
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
            )


main()


# Explicação

'''
Este código implementa um sistema bancário simples em Python, permitindo aos usuários realizar operações como depósitos, saques, extratos e criação de contas e clientes. Vamos analisar o código passo a passo para entender sua estrutura e funcionalidades:

**1. Importações:**

* `textwrap`: Para formatar texto, facilitando a apresentação do menu.
* `abc`: Para definir classes abstratas (`ABC`, `abstractclassmethod`, `abstractproperty`) e métodos abstratos.
* `datetime`: Para trabalhar com datas e horas.

**2. Classes:**

* **`ContasIterador`:**
    * Cria um iterador para iterar sobre uma lista de contas.
    * O método `__next__` formata os dados da conta antes de retorná-la.

* **`Cliente`:**
    * Classe base para clientes.
    * Atributos: `endereco`, `contas`, `indice_conta`.
    * Métodos:
        * `realizar_transacao`: Verifica se o cliente pode realizar a transação (limite de transações por dia) e a registra na conta.
        * `adicionar_conta`: Adiciona uma nova conta ao cliente.

* **`PessoaFisica`:**
    * Subclasse de `Cliente` para clientes físicos.
    * Atributos adicionais: `nome`, `data_nascimento`, `cpf`.

* **`Conta`:**
    * Classe base para contas bancárias.
    * Atributos: `_saldo`, `_numero`, `_agencia`, `_cliente`, `_historico`.
    * Métodos:
        * `nova_conta`: Método de classe para criar uma nova conta.
        * `saldo`: Propriedade para obter o saldo da conta.
        * `numero`: Propriedade para obter o número da conta.
        * `agencia`: Propriedade para obter o número da agência.
        * `cliente`: Propriedade para obter o cliente da conta.
        * `historico`: Propriedade para obter o histórico de transações da conta.
        * `sacar`: Permite sacar dinheiro da conta, verificando se há saldo suficiente.
        * `depositar`: Permite depositar dinheiro na conta.

* **`ContaCorrente`:**
    * Subclasse de `Conta` para contas correntes.
    * Atributos adicionais: `_limite`, `_limite_saques`.
    * Métodos:
        * `nova_conta`: Método de classe para criar uma nova conta corrente.
        * `sacar`: Permite sacar dinheiro da conta corrente, verificando o limite de saque e o número de saques.

* **`Historico`:**
    * Classe para gerenciar o histórico de transações de uma conta.
    * Atributos: `_transacoes`.
    * Métodos:
        * `transacoes`: Propriedade para obter a lista de transações.
        * `adicionar_transacao`: Adiciona uma nova transação ao histórico.
        * `gerar_relatorio`: Gera um relatório de transações, permitindo filtrar por tipo de transação.
        * `transacoes_do_dia`: Retorna as transações realizadas no dia atual.

* **`Transacao`:**
    * Classe abstrata para representar transações.
    * Atributos: `valor`.
    * Métodos:
        * `registrar`: Método abstrato para registrar uma transação em uma conta.

* **`Saque`:**
    * Subclasse de `Transacao` para saques.
    * Método `registrar`: Registra um saque na conta.

* **`Deposito`:**
    * Subclasse de `Transacao` para depósitos.
    * Método `registrar`: Registra um depósito na conta.

**3. Funções:**

* **`log_transacao`:**
    * Decorador que registra a data e hora de cada transação no console.

* **`menu`:**
    * Exibe o menu de opções para o usuário.

* **`filtrar_cliente`:**
    * Filtra a lista de clientes por CPF.

* **`recuperar_conta_cliente`:**
    * Recupera a primeira conta do cliente (FIXME: implementação simplificada, permitindo apenas uma conta por cliente).

* **`depositar`:**
    * Permite realizar um depósito na conta do cliente.

* **`sacar`:**
    * Permite realizar um saque na conta do cliente.

* **`exibir_extrato`:**
    * Exibe o extrato da conta do cliente.

* **`criar_cliente`:**
    * Cria um novo cliente.

* **`criar_conta`:**
    * Cria uma nova conta para o cliente.

* **`listar_contas`:**
    * Lista as contas existentes, formatando os dados de cada conta.

* **`main`:**
    * Função principal que controla o fluxo do programa, exibindo o menu e processando as opções do usuário.

**4. Execução:**

* A função `main` inicia o programa, criando as listas de clientes e contas, e entrando em um loop para processar as opções do usuário.

**Observações:**

* O código utiliza `textwrap.dedent` para formatar o menu e a saída de informações.
* O código inclui comentários para explicar o funcionamento do código.
* O código é modularizado em classes e funções, o que facilita a organização e a manutenção do código.
* O código utiliza `@log_transacao` como um decorador para registrar as transações.
* O código possui um `FIXME` que indica um ponto a ser revisado e melhorado, relacionado à escolha da conta do cliente.

**Pontos a serem melhorados:**

* Implementação da escolha da conta do cliente (o cliente deve poder escolher qual conta deseja utilizar, caso tenha mais de uma).
* Inclusão de validações de entrada de dados (por exemplo, validação do formato do CPF e da data de nascimento).
* Implementação de outras funcionalidades bancárias, como transferências e pagamentos.
* Uso de banco de dados para persistir os dados do sistema bancário.

Este código fornece uma base sólida para a construção de um sistema bancário mais completo e robusto. 

'''