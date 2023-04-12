""" Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado. """

p = int(input('Digite a quantidade de camisetas vendidas no tamanho P: '))
m = int(input('Digite a quantidade de camisetas vendidas no tamanho M: '))
g = int(input('Digite a quantidade de camisetas vendidas no tamanho G: '))

print(f'O valor arrecado será de R${(p*10)+(m*12)+(g*15):.2f}.')