""" O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.
 """

peso = float(input('Digite o peso do seu prato em quilos: '))

print(f'O valor a pagar será de R${peso * 19:.2f}.')