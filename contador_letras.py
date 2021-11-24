'''
Aplicação para contar número de ocorrências de cada letra em um arquivo *.txt
'''

print("########################################################")
print("Resolvido em Python por Victor Henrique Caldeira Barbosa")
print('')

import string
import itertools

arquivo_txt = input("digite o endereço do arquivo *.txt a ser lido: ")

with open(arquivo_txt, 'r') as file:
    texto = file.read().replace('\n', '') # Lê o txt e converte quebra de linhas em espaço

texto = texto.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))) # Converte pontuação em espaço
texto = texto.replace(" ", "")
texto = texto.lower()

n_letras = len(texto)

ocorrencias = list()

for l in texto:
    n = texto.count(l)
    ocorrencias.append([l, n])

# Eliminar duplicatas na lista
ocorrencias.sort()
ocorrencias = list(ocorrencias for ocorrencias,_ in itertools.groupby(ocorrencias))

# Organizar em ordem alfabética
sorted(ocorrencias, key=lambda x:x[0])

print('Total de letras: ', n_letras)
print('Precentuais:')
for i in range(len(ocorrencias)):
    percent = ocorrencias[i][1]/n_letras*100
    print(ocorrencias[i][0], '=', "{:.2f}".format(percent), '%')