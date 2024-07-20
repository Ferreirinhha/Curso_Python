#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Qual o preço do produto? R$'))
desconto = produto - (produto * 0.05)

print(f'Meus parabéns, você ganhou 5% de desconto nesse produto, de R${produto} passou a ser R${desconto:.2f}')