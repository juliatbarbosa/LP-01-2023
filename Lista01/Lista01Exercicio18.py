""" Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final. """

salario = float(input('Digite seu salário: '))
salarioNovo = salario + (salario * 0.15)

print(f'Seu salário inicial é R${salario:.2f}, seu salário com aumento é R${salarioNovo:.2f} e o salário final é R${salarioNovo - salarioNovo*0.08:.2f}')