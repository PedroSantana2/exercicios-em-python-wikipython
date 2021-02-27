'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
temperatura = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = temperatura * 9 / 5 + 32
print('{:.1f} graus Celsius equivale a {:.1f} graus Fahrenheit!'.format(temperatura, fahrenheit))
