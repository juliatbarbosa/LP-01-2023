#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 

avaliacoes = int(input('Digite o número total de avaliações: '))
resultado = 0

for a in range(avaliacoes):
    nota = float(input('Digite a nota: '))
    resultado = resultado + nota

print(f'A média aritmética das suas notas é: {resultado/avaliacoes}')