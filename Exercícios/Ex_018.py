"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse ângulo
""" 

import math

angulo = math.radians(int(input('Digite um ângulo: ')))

seno = math.sin(angulo)
cosseno =math.cos(angulo) 
tangente = math.tan(angulo)


print(f' Seno: {seno} \n Cosseno: {cosseno} \n Tângente: {tangente}')