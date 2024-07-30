# Tratamento de erro 

"""
Tipos de erro ->

NameError: Erro no nome

VAlueError: Erro no valor 

SintaxeError: Erro no sintaxe

ZeroDivisionError: Erro de divisão por zero

TypeErro: Erro de tipo

IndexErro: Erro no índice

ModuloNotFoundError: Modulo não encontrado

---> ETC <---
"""

# Podemos ter varios exceptions com o mesmo Try para personalizar outros tipos de erro.
try:
    a = 2   
    b = 0
    r = a/b
except Exception as erro: # 'as' serve para 'criar' uma variavel do exception
    print(f'Infelizmente deu um erro :( {erro.__class__}') 
else: # Roda se não der erro (opcional)
    print(f'O resultado é: {r}')
finally: # Roda independente do resultado (opcional)
    print('Volte sempre!!!')