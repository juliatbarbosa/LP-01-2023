#8- Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.

print('Digite a idade de 75 pessoas: ')

for i in range(75):
    idade = int(input(f'Pessoa [{i+1}]: '))

    if idade < 18:
        print('Menor de idade')
    else:
        print('Maior de idade')