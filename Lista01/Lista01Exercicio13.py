""" Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário. """

custo = float(input('Digite o preço de custo do produto: '))
percent = int(input('Informe o percentual de acréscimo do produto: '))

acrescimo = percent / 100

print(f'O preço de venda desse produto será de R${custo + custo*acrescimo:.2f}.')