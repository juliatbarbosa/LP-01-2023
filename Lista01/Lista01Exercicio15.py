""" Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
Ex: Tibúrcio, você já viveu 6935 dias.
 """

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

print(f'{nome}, você já viveu {idade * 365} dias.')