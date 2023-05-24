""" Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um programa para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.
 """

Moeda_1R = float(input('Informe a quantidade de moedas de R$1,00: '))
Moeda_50c= float(input('Informe a quantidade de moedas de R$0,50: '))
Moeda_25c = float(input('Informe a quantidade de moedas de R$0,25: '))
Moeda_10c = float(input('Informe a quantidade de moedas de R$0,10: '))
Moeda_5c = float(input('Informe a quantidade de moedas de R$0,05: '))
Moeda_1c = float(input('Informe a quantidade de moedas de R$0,01: '))

total = ((Moeda_1R * 1) + (Moeda_50c * 0.5) + (Moeda_25c * 0.25) + (Moeda_10c * 0.1) + (Moeda_5c * 0.05) + (Moeda_1c * 0.01))

print(f'O  valor total economizado é de R${total:.2f}.')