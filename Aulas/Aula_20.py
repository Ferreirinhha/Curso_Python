# Funções

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

def soma(a, b):
    print(a + b)


# Empacotar parâmetros

def contador(* num):  # * == Desempacotar
    tam = len(num)
    print(f'O tamanho de {num} é {tam}')

def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa principal
titulo('            Somando')
soma(4,5)

contador(1, 2, 3, 4, 5, 6) # Vai criar uma tupla com todos os parâmetros

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobrar(valores)
print(valores)