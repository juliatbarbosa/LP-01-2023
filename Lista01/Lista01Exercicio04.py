""" Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto
 """

distancia = float(input('Digite a distância total percorrida: '))
combustivel = float(input('Digite a quantidade de combustível gasto: '))

print(f'Seu consumo médio é de {(distancia/combustivel):.2f} litros por quilometros.')