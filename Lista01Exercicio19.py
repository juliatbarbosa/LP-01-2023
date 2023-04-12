""" A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra """

sanduiches = int(input('Digite a quantidade de sanduíches a fazer: '))
queijo = 0.1
presunto = 0.05
hamburguer = 0.1

print(f'Será necessário comprar {sanduiches * queijo}kg de queijo, {sanduiches * presunto}kg de presunto e {sanduiches * hamburguer}kg de hambúrguer.')