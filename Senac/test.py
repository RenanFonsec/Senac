from Classe_cadastro import *

cliente1 = Cadastro('Renan', '1234', '123456789-01', '21/01/2005', '9 1234-5678')
print(cliente1)

cliente1.deposito(100)
print(cliente1.saldo)