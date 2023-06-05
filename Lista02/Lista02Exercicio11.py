#11- Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto.
#Informe a média de preço de custo e do preço de venda.

print('------------------')

soma_custo = 0
soma_venda = 0

for i in range(1,41):
  print(f'Produto {i}')
  custo = float(input('Preço de custo: '))
  venda = float(input('Preço de venda: '))
  
  soma_custo += custo
  soma_venda += venda

  if custo > venda:
    print('Prejuízo')
  elif custo < venda:
      print('Lucro')
  else:
      print('Empate')
  print('------------------')

media_custo = soma_custo/40
media_venda = soma_venda/40

print(f'A média dos preços de custo foi de: R${media_custo:.2f}')
print(f'A média dos preços de venda foi de: R${media_venda:.2f}')
print('------------------')

