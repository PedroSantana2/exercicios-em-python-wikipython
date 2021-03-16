'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido
'''
ganhos_por_hora = float(input('Digite a quantidade de reais que você ganha por hora: R$'))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas por mês: '))

#Calculando salário bruto
salario_bruto = ganhos_por_hora * horas_trabalhadas
print('O seu salário bruto é de {:.2f} reais'.format(salario_bruto))

#11% para imposto de renda
salario_descontado = salario_bruto - (salario_bruto * 11 / 100)
descontado1 = salario_bruto - salario_descontado 
print('Imposto de renda: -{:.2f} reais'.format(descontado1))

#8% INSS
salario_descontado = salario_descontado - (salario_descontado * 8 / 100)
descontado2 = (salario_bruto - descontado1) - salario_descontado
print('INSS: -{:.2f} reais'.format(descontado2))

#5% Sindicato
salario_descontado = salario_descontado - (salario_descontado * 5 / 100)
descontado3 = (salario_bruto - descontado2 - descontado1) - salario_descontado
print('Sindicato: -{:.2f} reais'.format(descontado3))

print('O salário líquido é: {:.2f} reais'.format(salario_descontado))
