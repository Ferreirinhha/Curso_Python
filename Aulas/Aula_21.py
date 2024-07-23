# Funções parte2

# Interactive Help

help(print)

print(input.__doc__)

#DOCSTRINGS

def contador(i, f, p):
    """
    para mdpsldpsadlmsplm
    
    """

#Paramatros opcionais

def somar(a, b= int, c=0): # C é um parametro opicional
    s = a + b + c
    print(s)

somar(1)


# Escopo de variáveis

def variavel():
    global y
    print(y) # Com o global, se eu mexer com aquele Y, vai mexer com o y de fora tambem
    x = 8 # Variável local


y = 10 #Variável Global