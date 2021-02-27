'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

resposta1 = num1 * 2 + num2 / 2
resposta2 = num1 * 3 + num3
resposta3 = num3 ** 3

print('Produto do dobro do primeiro com metade do segundo: {:.2f}'.format(resposta1))
print('Soma do triplo do primeiro com o terceiro: {:.2f}'.format(resposta2))
print('Terceiro elevado ao cubo: {:.2f}'.format(resposta3))
