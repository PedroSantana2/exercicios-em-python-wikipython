'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
area = float(input('Digite o tamanho em metros quadrados da área: '))
litros = area / 3
latas = litros / 18

if latas <= 1:
    print('Você precisa de {:.2f} litros de tinta, é necessário apenas uma lata de tinta!'.format(litros))
    print('Valor: R${:.2f}'.format(1 * 80))
else:
    latas = litros // 18 + 1
    print('Você precisa de {:.2f} litros de tinta, é necessário {} latas de tina!'.format(litros, latas))
    print('Valor: R${:.2f}'.format(latas * 80)) 
