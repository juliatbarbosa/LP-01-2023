""" Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos. """
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

print(f'{numero1:.2f} + {numero2:.2f} = {numero1 + numero2:.2f}')
print(f'{numero1:.2f} - {numero2:.2f} = {numero1 - numero2:.2f}')
print(f'{numero1:.2f} * {numero2:.2f} = {numero1 * numero2:.2f}')
print(f'{numero1:.2f} / {numero2:.2f} = {numero1 / numero2:.2f}')