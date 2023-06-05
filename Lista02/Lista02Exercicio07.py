#7- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

""" numero = int(input('Digite ')) """

print('Digite 80 números: ')

contador = 0

for i in range(80):
    numero = int(input(f'[{i+1}] = '))

    if numero >= 10 and numero <= 150:
        contador+=1

print(f'A quantidade de números entre 10 e 150 é: {contador} ')