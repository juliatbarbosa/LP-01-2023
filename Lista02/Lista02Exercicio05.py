#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 

avaliacoes = int(input('Digite o número total de avaliações: '))
notas = []

for a in range(avaliacoes):
    nota = float(input(f'Digite a nota {a+1}: '))
    notas.append(nota)

media = sum(notas) / avaliacoes
print(f'A média aritmética das suas notas é: {media}')