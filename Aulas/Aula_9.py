
frase ='Curso em Vídeo Python'

#Fateamento
print('Fateamento:')
print(frase[9]) #Pega o 9° caracter da lista
print(frase[9:13]) #Pega o 9° caracter da lista até 1 antes do 13° elemento
print(frase[9:21:2])  #Pega o 9° caracter da lista até 1 antes do 21° elemento pulando de 2 em 2 e pegando o segundo elemento pulado
print(frase[:5])  #Pega o primeiro caracter da lista até 1 antes do 5° elemento
print(frase[15:])  #Pega o 15° caracter da lista até o último
print(frase[9::3]) #Pega o 9° caracter da lista até o último pulando de 3 em 3 e pegando o terceiro elemento
print('-'*20)

#Análise
print('Análise:')
print(len(frase)) #Retorna o tamanho do string ou quantos caracteres tem
print(frase.count('o')) #Conta quantos 'o' tem 
print(frase.count('o',0,13)) #Conta quantos 'o' tem partindo do primeiro carcater até 1 antes do 13°
print(frase.find('deo')) #Encontra o string desejado
print('Curso' in frase) #Tem 'Curso' na frase?
print('-'*20)

#Transformação
print('Transformação:')
print(frase.replace('Python','Android')) #Transforma 'Pyhton' em 'Android'
print(frase.upper()) #Troca os minusculo por maiusculo
print(frase.lower()) #Troca os maiusculo por minusculo
print(frase.capitalize()) # Toca tudo pra minusculo e o primeiro caracter para maiusculo
print(frase.title()) #Troca o primeiro caracter de cada palavra para maiusculo
print(frase.strip()) #Remove os spaços no inicio e no fim da string
print(frase.rstrip()) #Remove os spaços da direta do string
print(frase.lstrip()) #Remove os spaços da esquerda do string
print('-'*20)

#Divisão
print('Divisão:')
print(frase.split()) #Divide as frases em elementos proprios
print('-'*20)

#Junção
print('Junção:')
print('-'.join(frase))
print('-'*20)
