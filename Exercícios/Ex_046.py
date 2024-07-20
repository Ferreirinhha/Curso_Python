"""
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifícios,
indo de 10 a 0 com uma pausa de 1 segundo entre eles.
"""
import time

print('')
print('\033[1;33m-=\033[m' * 25)

a = 40

time.sleep(3)
print('\033[1;33m -VAMO GALERA, CONTA COMIGO!!!\033[m')
time.sleep(2)

for c in range(10, 0, -1):
    print(f'\033[1;{a - c}m{c}\033[m')
    time.sleep(1)
    
print('\033[1;33mFELIZ ANO NOVOOOO!!!\033[m')
print('\033[1;33m-=\033[m' * 25)
print('')