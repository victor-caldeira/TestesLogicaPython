'''
Aplicação para encontrar anagramas em um arquivo *.txt
'''

print("########################################################")
print("Resolvido em Python por Victor Henrique Caldeira Barbosa")
print('')

import string

arquivo_txt = input("digite o endereço do arquivo *.txt a ser lido: ")
with open(arquivo_txt, 'r') as file:
    texto = file.read().replace('\n', '') # Lê o txt e converte quebra de linhas em espaço

texto = texto.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))) # Converte pontuação em espaço
texto = texto.lower()
palavras = texto.split() # Quebra a string em uma lista de strings (palavras)

anagramas = list()
classe = list()

for i in range(len(palavras)):
  for ii in range(len(palavras)-i):

    # Organiza as strings em ordem alfabética e verifica se são iguais
    if sorted(palavras[i]) == sorted(palavras[ii+i]) and palavras[i] != palavras[ii+i] and not(any(palavras[i] in sublist for sublist in anagramas)): 
      if classe: # Verifica se já foi identificado um anagrama com essa palavra
        classe.append(palavras[ii+i])

      else:
        classe = [palavras[i], palavras[ii+i]]

  
  if classe: # se foi identificado um anagrama, anexar à lista de anagramas e limpar a classe para a próxima pesquisa
    anagramas.append(classe)
    classe = list()

print("Anagramas encontrados: ")
print(anagramas)