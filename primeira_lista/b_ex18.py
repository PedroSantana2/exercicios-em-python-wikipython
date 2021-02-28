'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('Digite a velocidade de sua conexão em Mbps: '))
tempo = tamanho / velocidade
minutos = tempo / 60
print('Para baixar um arquivo de {} Mb com uma internet de {} Mbps levará aproximadamente {:.2f} minutos ou {} segundos'.format(tamanho, velocidade, minutos, tempo))
