'''
#Parâmetro Default

def exibe (valor1=0, valor2=20):
    print("Valor 1", valor1)
    print("Valor 2", valor2)

#Chamada da função

exibe()

#Quando não se sabe a quantidade de argumentos vai passsar para a função, usar args:
def numero (*args):
    for valor in args:
        print(valor)

numero (1, 2, 3, "casa", [3,4,5])


#Funções como parâmetro:

def mult(n1,n2):
    return n1 * n2

def expo(v1,v2):
    return pow (v1,v2)

def exibir(a, b, func):
    print(func(a,b))

exibir(4,3, mult)

exibir(4,3,expo)

'''

#Receber uma lista como argumento (parâmetro):

def exibir_lista(lista):
    return lista[0]

lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"]

mes = exibir_lista(lista_meses)

print(mes) 




