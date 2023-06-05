#10 Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número

N = int(input('Digite a quantidade de números que deseja: '))

for i in range(N):
    numero = int(input(f'Número [{i+1}]: '))

    if numero == 0:
        print('Zero')
    elif numero < 0:
        print('Negativo')
    else:
        print('Positivo')