from abc import ABC, ABCMeta, abstractmethod

class Conta():
    def __init__(self, saldo, agencia, numero, titular):
        self._saldo = saldo
        self._agencia = agencia
        self._numero = numero
        self._titular = titular.title()

    __metaclass__ = ABCMeta

    def __str__(self):
        return f'Titular: {self._titular} - Saldo: {self._saldo}'

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @agencia.setter
    def nome(self, agencia):
        self._agencia = agencia

    @numero.setter
    def nome(self, numero):
        self._numero = numero

    @titular.setter
    def nome(self, titular):
        self._titular = titular.title()

    def saca(self, valor):
        if (valor <= self._saldo):
            self._saldo -= valor
        else:
            print("Saldo insuficiente para a realização do saque")

    def deposita(self, valor):
        self._saldo += valor

    def transfere(self, Conta, valor):
        self.saca(valor)
        Conta.deposita(valor)

class Imposto:
    @abstractmethod
    def importoValor(self):
        return

class ContaCorrente(Conta, Imposto):
    def saca(self, valor):
        super().saca(valor + 0.2)

    def importoValor(self):
        return 1.2

class ContaPoupanca(Conta, Imposto):
    def transfere(self, Conta, valor):
        super().transfere(Conta, valor + 0.2)

    def importoValor(self):
        return 1

conta1 = ContaPoupanca(100, 1, 1, "mateus")
conta2 = ContaCorrente(100, 2, 2, "lais")

conta1.transfere(conta2, 10)
print(conta1)
print(conta1.importoValor())
print(conta2)
print(conta2.importoValor())
