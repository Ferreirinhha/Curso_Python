#============================================================================
#Operacões aritmeticas
nome2 = input('Qual o seu nome? ')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potenciacao = n1**n2
divisao_inteira = n1//n2
modulo = n1%n2
potencia = pow(n1,n2) # 3 elevado a 5
raiz_quadrada = n1**(1/2)
multiplicar_palavra = 'oi' * 5 #vai mostrar oi 5 vezes

print(f'A soma é: {soma} \n A subtração é: {subtracao} \n A multiplicação é: {multiplicacao} \n A divisão é: {divisao} \n A potencia é: {potenciacao} \n A divisão inteira é: {divisao_inteira} \n O Módulo é: {modulo} \n A potencia com pow é: {potencia} \n A raiz quadrada é: {raiz_quadrada}')

print('Prazer em conhecer {:20}'.format(nome2), end =' ') #Prazer em conhecer Daniel ///// o end vai fazer n pular linha de um print para o outro
print('Prazer em conhecer {:>20}'.format(nome2)) #Prazer em conhecer               Daniel
print('Prazer em conhecer {:<20}'.format(nome2)) #Prazer em conhecer Daniel
print('Prazer em conhecer {:^20}'.format(nome2)) #Prazer em conhecer        Daniel
print('Prazer em conhecer {:=^20}'.format(nome2)) #Prazer em conhecer =======Daniel=======
