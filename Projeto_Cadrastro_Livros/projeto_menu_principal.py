
import cadastro, listar, emprestimo, pesquisar, remover, relatorio

resposta = 'sim'

while resposta == 'sim':
    menu = '''----------------- BIBLIOTECA TDS 10 -----------------
    [1] Cadastrar Cliente
    [2] Listar Clientes
    [3] Cadastrar Livro
    [4] Listar Livros 
    [5] Realizar Empréstimo
    [6] Lista de Empréstimos   
    [7] Relatório de Livros
    [8] Remover Cliente
    [9] Remover Livro
    '''
    print(menu)

    opcao = int(input('Entre com uma opção: ')) #escolher a opção digitada

    if opcao == 1:
        cadastro.cadastrar_cliente()
    elif opcao == 2:
        listar.listar_clientes()

    elif opcao == 3:
        cadastro.cadastrar_livro()
    
    elif opcao == 4:
        listar.listar_livros()

    elif opcao == 5:
        emprestimo.realizar_emprestimo()
    
    elif opcao == 6:
        listar.listar_emprestimos()

    elif opcao == 7:
        relatorio.relatorio_livros()

    elif opcao == 8:
        remover.remover_cliente()
    
    elif opcao == 9:
        remover.remover_livro()

        resposta = input("\nDeseja continuar? [sim/nao]")



