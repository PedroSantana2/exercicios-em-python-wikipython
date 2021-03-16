'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
#Recebendo as notas
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
nota4 = float(input('Digite a quarta nota do aluno: '))

#Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

#Resultado
print('A média do aluno foi: {:.1f}'.format(media))
