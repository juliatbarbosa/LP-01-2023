""" Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3. """

A = int(input('Digite um valor para A: '))
B = int(input('Digite um valor para B: '))

valorA = A
A = B
print(f'Seu A vale: {A} e seu B vale: {valorA}')