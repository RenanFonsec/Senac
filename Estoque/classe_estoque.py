import mysql.connector
from classe_produto import *
from classe_fabricante import *

class DBEstoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    # Create
    def registrar_produto(self, cod, nome, cod_fabricante, quantidade):
        obg_produto = Produtos(cod, nome, cod_fabricante, quantidade)
        comando_sql = f'insert into Produto ' \
                      f'(nome, cod_fabricante, quantidade) ' \
                      f'value ' \
                      f'("{obg_produto.nome}", "{obg_produto.cod_fabricante}", "{obg_produto.quantidade}")'    
        try:
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()
        except:
            print('============================================')
            print('Fabricante não existe !')
            print('============================================')

    def registrar_fabricante(self, cod, fabricante):
        obg_fabricante = Fabricante(cod, fabricante)
        comando_sql = f'insert into Fabricante' \
                      f'(nome)' \
                      f'value' \
                      f'("{obg_fabricante.fabricante}")'

        try:
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()
        except:
            print('============================================')
            print('Não foi possivel registrar esse fabricante')
            print('============================================')

        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()    

    # Read
    def achar_produto(self, valor):
        comando_sql = f'select * from Produto where cod = {valor}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

        try:
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()
        except:
            print('============================================')
            print('Não foi possivel encontrar esse produto !')
            print('============================================')
                    
            

    def listar_todos_produtos (self):
        comando_sql = 'select Produto.cod_produto, ' \
                      'Produto.nome, Fabricante.nome, ' \
                      'Produto.quantidade from Produto, ' \
                      'Fabricante ' \
                      'where Produto.cod_fabricante = Fabricante.Fabri'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    # Update
    def alterar_produto (self, atributo, valor, cod):
        comando_sql = f'update Produto set {atributo} = "{valor}" where cod = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

        try:
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()
        except:
            print('============================================')
            print('Não foi possivel alterar esse produto !')
            print('============================================')

    # Delete
    def excluir_produto(self, valor):
        comando_sql = f'delete from Produto where cod = {valor}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

        try:
            self.meu_cursor.execute(comando_sql)
            self.conexao.commit()
        except:
            print('============================================')
            print('Não foi possivel excluir esse produto !')
            print('============================================')

    