""" A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações """

compra = float(input('Digite o valor total da sua compra: '))

print(f'Suas prestações terão o valor de R${compra/5:.2f} sem juros.')