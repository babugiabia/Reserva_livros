import csv
import os

def pesquisar_cliente(nome_cliente):
    with open('clientes.csv', newline='')  as cliente_csv:  #abrindo o arquivo CSV
        dados_cliente = csv.DictReader(cliente_csv, delimiter=",") #lendo conteudo

    for cliente in dados_cliente: #percorrendo as linhas do arquivo
        if(cliente["nome"].lower() == nome_cliente.lower()):
            nome =  (cliente["nome"]) #listar o nome do cliente, a partir da chave ["nome"]
            cpf =  (cliente["cpf"])
            return (True,nome, cpf)
            break
    return (False)


def pesquisar_livros():
    livros_csv = open('livros.csv')
    nome_livro = csv.DictReader(livros_csv, determiter=";")

    for livros in nome_livro:
        if (livros["título"] == nome_livro):
            nome_livro = (livros["título"])
            codigo = (livros["código"])
            return (True, nome_livro, codigo)
            break
    return (False)