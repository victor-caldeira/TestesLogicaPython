'''
Aplicação para verificar se uma palavra digitada é um palíndromo.
'''

print("########################################################")
print("Resolvido em Python por Victor Henrique Caldeira Barbosa")
print('')

palavra = input('Digite uma palavra: ')
n_chars = len(palavra)
palindromo = True

for i in range(round(n_chars/2)):
  if palavra[i].lower() != palavra[-i-1].lower():
    palindromo = False
    break

if palindromo:
  print("A palavra digitada é um palíndromo!")
else:
  print("A palavra digitada NÃO é um palíndromo!")