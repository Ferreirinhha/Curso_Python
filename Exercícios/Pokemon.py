import random
import time

print('')
print('\033[1;33m-=' * 18)
print('\033[1;34m  Sorteio Pokemons 1° geração: ') # add evelucion
print('\033[1;33m-=\033[m' * 18)
print('')


quantidade = int(input('\033[1;35mQuantos pokemons voce quer no seu time: '))
print('')
inicial = str(input('Inclui inicial no sorteio? (responda com Sim ou Não): ')).upper().strip()
print('\033[m \033[1;40m')

#Pokemons
lista_inicial = ["Bulbasaur", "Charmander", "Squirtle"]
pokemon_gen1 = [ 
    "Caterpie", "Weedle", "Pidgey", "Rattata", 
    "Spearow", "Ekans", "Pikachu", "Sandshrew", "Nidoran♀", "Nidoran♂", "Clefairy", 
    "Vulpix", "Jigglypuff", "Zubat", "Oddish", "Paras", "Venonat", "Diglett", 
    "Meowth", "Psyduck", "Mankey", "Growlithe", "Poliwag", "Abra", "Machop", 
    "Bellsprout", "Tentacool", "Geodude", "Ponyta", "Slowpoke", "Magnemite", 
    "Farfetch'd", "Doduo", "Seel", "Grimer", "Shellder", "Gastly", "Onix", 
    "Drowzee", "Krabby", "Voltorb", "Exeggcute", "Cubone", "Hitmonlee", "Lickitung", 
    "Koffing", "Rhyhorn", "Tangela", "Kangaskhan", "Horsea", "Goldeen", "Staryu", 
    "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", 
    "Magikarp", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", 
    "Porygon", "Omanyte", "Kabuto", "Aerodactyl", "Dratini"
    ]

#Ifs escolhas
if quantidade == 6 and inicial == 'SIM' or quantidade < 6 and inicial == 'SIM':
    escolher = (random.sample(lista_inicial, k = (quantidade - quantidade) + 1)) + random.sample(pokemon_gen1, k = quantidade - 1)
    
elif quantidade == 6 and inicial == 'NAO' or 'NÃO' or quantidade < 6 and inicial == 'NAO' or 'NÃO':
    escolher = random.sample(pokemon_gen1, k = quantidade)
    
print(str(escolher))
print('\033[m')
