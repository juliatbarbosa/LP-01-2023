""" Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque. """

preço_gasolina = float(input('Digite o preço do litro da gasolina: '))
valor = float(input('Digite o valor que deseja pagar: '))

print(f'Com R${valor:.2f} você colocará {valor/preço_gasolina:.2f} litros de gasolina.')