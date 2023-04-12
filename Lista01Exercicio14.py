""" A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança. """

paes = int(input('Digite a quantidade de pães vendidos: '))
bolo = int(input('Digite a quantidade de pedaços de bolos vendidos: '))

valor_paes = paes * 0.12
valor_bolo = bolo * 1.5
poupanca = ((valor_paes) + (valor_bolo)) * 0.1

print(f'Foi arrecadado neste dia R${(valor_paes) + (valor_bolo):.2f} e deve-se guardar na poupança o valor de R${poupanca:.2f}.')