from calendar import c


class Cadastro:

    historico = []

    def __init__(self, nome: str, senha: int, cpf: str, datanasc: int, tel: int, saldo=0.0):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.datanasc = datanasc
        self.tel = tel
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append('depositou ' + str(valor))
        return self.saldo

    def saque(self, valor):
        self.saldo -= valor
        self.historico.append('sacou ' + str(valor))
        return self.saldo

    def transferencia(self, valor, conta):
        self.saldo -= valor
        conta.saldo += valor
        self.historico.append(
            'transferiu ' + str(valor) + ' para ' + conta.nome)
        conta.historico.append('recebeu ' + str(valor) + ' de ' + self.nome)
