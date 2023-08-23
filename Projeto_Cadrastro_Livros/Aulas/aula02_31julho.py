'''
#Função que não retorna valor e que não tem parâmetros:

#DECLARANDO A FUNÇÃO
def exibe():
    print("Estudando funções")

#CHAMANDO A FUNÇÃO
exibe()

#Função que não retorna valor, mas tem parâmetros:
def multiplicacao(valor1, valor2):
    print("Produto:",valor1 * valor2)

multiplicacao(2, 3)

#Função que retorna valor:
def multiplica (valor1, valor2):
    return valor1 * valor2

resultado = multiplica(2,5)
print(resultado)

#Função que retorna mais de um valor
def operacoes(n1, n2):
    return n1 * n2, n1 + n2, n1 - n2

produto, total, restos = operacoes (4,2)

print("Produto:", produto)
print("Total:", total)
print("Restos", restos)

'''

#Retornar mais de um valor usando TUPLA
tupla = ()
lista = ["Produto", "Total", "Resto"]
k = 0

def operacoes(n1, n2):
    return n1 * n2, n1 + n2, n1 - n2

tupla = operacoes (10,3)

print(lista[0], tupla[0])

'''

while k < len(tupla): #len retorna o tamanho 
    print(lista[k], tupla[k])
    k = k + 1

'''


