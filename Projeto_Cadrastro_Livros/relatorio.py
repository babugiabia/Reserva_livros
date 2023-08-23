import csv, os
from datetime import datetime 
import pesquisar


def relatorio_livros():
    emprestimo_csv = open('emprestimo..csv')

    dados_emprestimo = csv.DictReader(emprestimo_csv, delimiter = ";")

    os.system('cls') or None
    print("------------- RELATORIO EMPRESTIMOS --------")
    print(f'{"CPF": 15}', f'{"Nome":25}', f'{"Titulo":15}', f'{"Emprestimo":15}', f'{"Situação":20}', f'{"Dias"}')
    for emprestados in dados_emprestimo:
        data_emprestimo = datetime.strptime(emprestados[data_emprestimo])
        data_hoje = datetime.today()
        dias_atrasados = (data_hoje - data_emprestimo).days

        if dias_atrasados > 7:
            situacao = "Atrasado"
            print(f'{emprestados["cpf"]:15}',
                  f'{emprestados}'
                  )

    relatorio_livros()