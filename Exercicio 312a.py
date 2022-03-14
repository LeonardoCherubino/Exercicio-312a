#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distencia a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Entre com a distância em quilometros: '))
velocidade = float(input('Entre com a velocidade média estimada em Km/h: '))
tempo = distancia / velocidade
print('O tempo estimado para essa viagem é de aproximadamente {} horas'.format(tempo))