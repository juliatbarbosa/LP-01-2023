""" Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês. """

vendedor = str(input('Digite seu nome: '))
salario_fixo = float(input('Digite seu salário fixo: '))
vendas = float(input('Digite o valor total de vendas do mês: '))
comissao = vendas * 0.15

print(f'{vendedor}, seu salário fixo é R${salario_fixo:.2f} e seu salário no final do mês é R${salario_fixo + comissao:.2f}.')