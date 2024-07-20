#Condições aninhadas

# Ignore o codigo a baixo, apenas quero explicar como o elif funciona.
if 1 > 2:
    print(2)
elif 3 > 4: # o elif só será execultado se o primeiro if não for execultado, se entrar no if, o elif nunca será acessado
    print(3)
else:
    print(5)