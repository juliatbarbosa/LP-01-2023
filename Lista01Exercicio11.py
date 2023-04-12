""" Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.
 """

valor = float(input('Digite o valor depositado: '))
rendimento = valor * 0.007

print(f'Após um mês, o valor será de R${valor + rendimento:.2f}.')