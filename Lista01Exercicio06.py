""" Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética). """

nome = str(input('Digite seu nome: '))
prova1 = float(input('Digite a nota da prova 1: '))
prova2 = float(input('Digite a nota da prova 2: '))
prova3 = float(input('Digite a nota da prova 3: '))

print(f'{nome}, a média de suas provas é: {(prova1 + prova2 + prova3) / 3:.2f}.')