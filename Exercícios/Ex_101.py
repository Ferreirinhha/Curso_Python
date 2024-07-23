""" Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o nascimento de uma pessoa, retornando um valor literal indicando se
uma pessoa tem voto negado, opcional ou obrigatório nas eleições. """


def voto(nasc: int):
    from datetime import date # Economiza memória, pois o import fica dentro só do escopo
    idade = date.today().year - nasc
    if 0 <= idade <= 18:
        return "Voto não obrigatório!!!"
    elif 18 <= idade <= 65:
        return "Voto obrigatório!!!"
    elif 65 < idade <= 150:
        return "Voto opicional"
    else:
        return "Ou você está morto ou você não nasceu ainda. Digite a idade correta"


votar = int(input('Em que ano você nasceu: '))

print(voto(votar))