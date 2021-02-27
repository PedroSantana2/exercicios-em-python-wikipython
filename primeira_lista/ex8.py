'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
ganhos_por_hora = float(input('Digite a quantidade que você ganha por hora: R$'))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas no mês: '))
print('Ganhando {} reais por hora e trabalhando {} horas por mês, você ganhará {} reais a cada mês!'.format(ganhos_por_hora, horas_trabalhadas, horas_trabalhadas * ganhos_por_hora))
