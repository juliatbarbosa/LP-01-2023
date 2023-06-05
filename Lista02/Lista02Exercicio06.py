""" 6- Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
A atribuição de conceitos obedece a tabela abaixo:

Média de Aproveitamento | Conceito
MA >= 9,0               | A
7,5 <= MA < 9,0         | B
6,0 <= MA < 7,5         | C
4,0 <= MA < 6,0         | D
MA < 4,0                | E

O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não """

repetir = 'S'

while repetir == 'S':
    NI = input('Digite seu número de identificação: ')

    Nota1 = float(input('Digite sua nota 1: '))
    Nota2 = float(input('Digite sua nota 2: '))
    Nota3 = float(input('Digite sua nota 3: '))

    ME = int(input('Digite sua média dos exercícios: '))

    MA = (Nota1 + Nota2 * 2 + Nota3 * 3 + ME )/7

    if MA >= 9.0:
        conceito = 'A'
    elif MA >= 7.5 and MA < 9.0:
        conceito = 'B'
    elif MA >= 6.0 and MA < 7.5:
        conceito = 'C'
    elif MA >= 4.0 and MA < 6.0:
        conceito = 'D'
    else:
        conceito = 'E'


    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        situacao = 'APROVADO'
    else:
        situacao = 'REPROVADO'

    print(f'Número do aluno: {NI}')
    print(f'Notas: \n\tNota 1: {Nota1} \n\tNota 2: {Nota2} \n\tNota 3: {Nota3}')
    print(f'A média dos exercícios é {ME}')
    print(f'A média de aproveitamento é: {MA:.1f}')
    print(f'Seu conceito é {conceito} e você foi {situacao}!')
    
    resposta = input('Deseja digitar as notas de outro aluno? (Responda com S para SIM e N para NÃO): ')

    if resposta == 'S':
        repetir = 'S'
    else:
        repetir = 'N'
