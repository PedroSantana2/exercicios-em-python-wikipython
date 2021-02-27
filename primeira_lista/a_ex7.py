'''
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
lado = float(input('Digite o comprimento do lado do quadrado: '))
area = lado ** 2
print('A área do quadrado com lado {} é igual a: {} e o dobro dessa área é: {}'.format(lado, area, area * 2))
