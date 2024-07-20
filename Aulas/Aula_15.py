# Interrompendo o while 

cont = 1 
while True:
    print(cont, ' → ', end='')
    cont += 1
    if cont == 1000:
        break
print('Fim.')