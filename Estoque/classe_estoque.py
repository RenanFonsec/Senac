import mysql.connector
from classe_produto import *

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
    def registrar_produto(self, cod, nome, fabricante, quantidade):
        obg_produto = Produtos(cod, nome, fabricante, quantidade)
        comando_sql = f'insert into Produto ' \
                      f'(nome, fabricante, quantidade) ' \
                      f'value ' \
                      f'("{obg_produto.nome}", "{obg_produto.fabricante}", "{obg_produto.quantidade}")'    

        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    # Read
    def achar_produto(self, valor):
        comando_sql = f'select * from Produto where cod = {valor}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)
            

    def listar_todos_produtos (self):
        comando_sql = 'select * from Produto'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    # Update
    def alterar_produto (self, atributo, valor, cod):
        comando_sql = f'update Produto set {atributo} = "{valor}" where cod = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    # Delete
    def excluir_produto(self, valor):
        comando_sql = f'delete from Produto where cod = {valor}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    