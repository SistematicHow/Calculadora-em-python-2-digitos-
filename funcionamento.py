"""
    Titulo do arquivo da calculadora
    //TODO esse arquivo faz calculos somente com 2 numeros.
"""
print('=======================================================================')
print('=======================================================================')
print('==============================Calculadora==============================')
print('=======================================================================')
print('=======================================================================')
#Teclas de atalho para diferentes operadores
print('\n \n \n \n \n \nPressione [1] para somar') #Somar 
print('\nPressione [2] para subtrair') #Subtrair
print('\nPressione [3] para multiplicar') #Multiplicar
print('\nPressione [4] para dividir') #Dividir
print('\nPressione [5] para descobrir raiz quadrada') #raiz quadrada
print('\nPressione [6] para ver desconto em porcentagem') #Porcentagem
#tela de clicar no operador que deseja
'''//TODO
   Se você clicar um dos números acima irá redirecionar seus operadores para o desejado
   1 será clicado e você digitara 2 números para somar
   isso se aplica para o resto
'''
calculador = int(input('Oque você deseja calcular?'));

if calculador == 1: #Se a tecla 1 for clicada acontecera isso e os elif são as outras teclas
    num1 = float(input('Digite um número:')); #Primeiro algoritimo
    num2 = float(input('Digite outro número:')); #Segundo algoritimo
    print('O número {:.2f} somado por {:.2f} resulta em {}'.format(num1, num2, (num1 + num2))) #Realizando o calculo
    #Mesma coisa nos debaixo:
elif calculador == 2:
    num1 = float(input('Digite um número:'));
    num2 = float(input('Digite outro número:'));
    print('O número {:.2f} subtraído por {:.2f} resulta em {}'.format(num1, num2, (num1 - num2)))
elif calculador == 3:
    num1 = float(input('Digite um número:'));
    num2 = float(input('Digite outro número:'));
    print('O número {:.2f} multiplicado por {:.2f} resulta em {}'.format(num1, num2, (num1 * num2)))
elif calculador == 4:
    num1 = float(input('Digite um número:'));
    num2 = float(input('Digite outro número:'));
    print('O número {:.2f} dividido por {:.2f} resulta em {}'.format(num1, num2, (num1 / num2)))
elif calculador == 5:
    num1 = float(input('Digite um número:'));
    print('A raiz quadrada de {} é {}'.format(num1, (num1 ** (1/2))))
elif calculador == 6:
    num1 = float(input('Digite um número:'));
    num2 = float(input('Digite o desconto'))
    calculo = num1 * num2 / 100
    print('O número {} com desconto de {} resulta em {}'.format(num1, num2, (num1 - calculo)))
else:
    print('Algoritimo não reconhecido :(')

#Feito por Miguel Camilo (sistematic tutorials) Se inscreva :)
