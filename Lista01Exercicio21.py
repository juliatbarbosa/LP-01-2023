""" Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?
 """

roupa = float(input('Informe o valor da roupa: '))

print(f'Durante a liquidação ela custará R${roupa - (roupa*0.3):.2f}.')