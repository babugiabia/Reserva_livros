import os, csv

def listar_clientes():
    with open('clientes.csv', newline = '') as clientes_csv:
        dados_cliente = csv.DictReader(clientes_csv, delimiter=',')

        for cliente in dados_cliente:
            print(cliente)

def listar_livros():
    with open('livros.csv', newline = '') as livros_csv:
        nome_livros = csv.DictReader(livros_csv, delimiter=";")

        for livro in nome_livros:
            print(livro)
          

def listar_emprestimos():
    return 0