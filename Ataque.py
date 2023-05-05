import collections
import math

mensagem = ''.join(filter(str.isalpha, input("Digite a mensagem: ").upper())) #Converte para maiúsculas

repeticoes = {}
tamanhos = [0]*19

for i in range(len(mensagem) - 2):
    sequencia = mensagem[i:i+3]
    if sequencia in repeticoes:
        #pega distancia da penultima ocorrencia até a ultima 
        distancia = i - repeticoes[sequencia][len(repeticoes[sequencia]) - 1] + 1
        #Descobre o tamanho da chave
        for tamanho_chave in reversed(range(len(tamanhos))):
            if distancia % (tamanho_chave + 2) == 0:
                tamanhos[tamanho_chave] += 1
                distancia = tamanho_chave/2
        #Separa o primeiro indice da ultima repetição
        repeticoes[sequencia].append(i)
    else:
        repeticoes[sequencia] = [i]

print(tamanhos)
'''
for sequencia in repeticoes:
    if repeticoes[sequencia]["quantidade"] > 1:
        print(f"{sequencia}")
'''