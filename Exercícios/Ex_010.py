#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode 

carteira = float(input('Quanto de dinheiro você tem na carteira? R$'))

dolar = carteira / 5.37

print(f'Você pode comprar US${dolar:.2f} dólares com esse dinheiro')