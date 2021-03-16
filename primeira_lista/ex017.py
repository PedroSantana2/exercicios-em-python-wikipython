'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
area = float(input('Digite o tamanho da área em metros quadrados: '))
litros = area / 6
latas = litros / 18
galoes = litros / 3.6

print('É necessário {:.2f} litros de tinta'.format(litros))
print('=-' * 10)
#Comprar apenas latas
if latas <= 1:
    print('Você precisa comprar apenas uma lata de tinta!\nValor: R$80')
    print('=-' * 10)
else:
    latas = litros // 18 + 1
    print('Você precisa comprar comprar {} latas!'.format(latas))
    print('Valor: R${:.2f}'.format(latas * 80))
    print('=-' * 10)

#Comprar apenas em galões:
if galoes <= 1:
    print('Ou apenas um galão de tinta pelo valor de R$25')
    print('=-' * 10)
else:
    galoes = litros // 3.6 + 1
    print('Ou comprar {} galões!'.format(galoes))
    print('Valor: R${:.2f}'.format(galoes * 25))
    print('=-' * 10)

#Comprar galões e latas
litros = area / 6
latas = litros / 18
galoes = litros / 3.6

if latas % 18 == 0:
    galoes = 0
if latas % 18 != 0:
    resto = (litros % 18) / 3.6
    if resto % 3.6 == 0:
        galoes = resto / 3.6
    else:
        galoes = int(resto) + 1
        latas = int(latas)
        if 80 < galoes * 25:
            galoes = 0
            latas = latas + 1
if latas < 1:
    galoes = galoes / 3.6
    if galoes % 3.6 != 0:
        galoes = litros // 3.6 + 1
        if 80 < (galoes * 25):
            galoes = 0
            latas = 1
print('Ou comprando {:.2f} lata(s) e {:.2f} galão(ões)'.format(latas, galoes))
print('Preço: R${}'.format(galoes * 25 + latas * 80))
