#9- Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.

repetir = 'S'

carros_2000 = 0
total_geral = 0
soma = 0

print('\n---------------------------------------------------\n')

while repetir == 'S':

    valor = float(input('Valor do veículo: R$'))
    ano = int(input('Ano do veículo: '))

    if ano <= 2000:
        desconto = valor*0.12
        valor_pago = valor - desconto
        carros_2000+=1
        soma = soma + valor_pago

    else:
        desconto = valor*0.07
        valor_pago = valor - desconto
        soma = soma + valor_pago

    total_geral += 1

    print(f'O desconto será de R${desconto:.2f}.')
    print(f'O valor a ser pago será de R${valor_pago:.2f}.')

    print('\n---------------------------------------------------\n')

    repetir = input('Deseja calcular mais descontos? (Responda S para SIM e N para NÃO) ').upper()

    print('\n---------------------------------------------------\n')

print(f'Total de carros com ano até 2000: {carros_2000}.')
print(f'Total geral de carros: {total_geral}.')
print(f'Soma total dos valores dos carros: {soma}.')

print('\n---------------------------------------------------\n')



