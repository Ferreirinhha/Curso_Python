import secrets


while True:
    senha = 'asevedo'
    tentativa = secrets.token_urlsafe(5)
    print(tentativa, end=" ")
    if tentativa == senha:
        break
print()
print('Parabéns, acertou a senha!!!')

