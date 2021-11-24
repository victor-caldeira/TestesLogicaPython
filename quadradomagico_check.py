'''
Aplicação para verificar se uma matriz NxN é um quadrado mágico.
'''

print("########################################################")
print("Resolvido em Python por Victor Henrique Caldeira Barbosa")
print('')

import numpy as np

n = int(input('Entre com a dimensão da matriz NxN: '))
matriz = np.zeros((n, n))

for i in range(n):
  for ii in range(n):
    print('Entre com o valor do elemento', i+1, 'x', ii+1, ": ")
    matriz[i,ii] = input()

soma_hor = np.sum(matriz,axis=1)
soma_ver = np.sum(matriz,axis=0)  
soma_diag = np.trace(matriz)
soma_diag2 = np.trace(np.fliplr(matriz))


if (soma_hor==soma_ver).all() and soma_diag==soma_diag2 and soma_diag==soma_hor[0]:
  print('quadrado mágico')
else:
  print('quadrado não mágico')