"""
Escreva um programa que leia um número N inteiro e mostre na tela os N primeiros 
elementos de uma Sequencia Fibonacci.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

termo = int(input('Quantos termos você quer mostrar: '))

t1 = 0 #Criei o primeiro termo da sequencia
t2 = 1 #Criei o segundo termo da sequencia
cont = 3

print(t1, t2, end=" → ")

while cont <= termo:
    t3 = t1 + t2 # criei o terceiro termo da sequencia que seria a soma dos dois primeiros
    print(t3, end=" → ")
    t1 = t2 # aqui eu fiz o t1 andar uma casa para frente, fazendo ele tomar o lugar do t2
    t2 = t3 # aqui eu fiz o t2 andar uma casa para frente, fazendo ele tomar o lugar do t3, e o t3 nos ja sabemos que é a soma dos dois ultimos que no momento, já estão com os novos valores.Fazendo eles andarem toda vezs que o while andar tambem.
    cont += 1
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')
    
   
    
    
