def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.') # converte a vigula para o ponto e não o ponto para virgula
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro: \"{entrada}"\ é um preço invalido.')
        else:
            valido = True
            return float(entrada)