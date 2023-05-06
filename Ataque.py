from unidecode import unidecode
import collections
import string
import math

mensagem = unidecode(''.join(filter(str.isalpha, input("Digite a mensagem: ").upper()))) #Converte para maiúsculas

repeticoes = {}

for i in range(len(mensagem) - 2):
    sequencia = mensagem[i:i+3]
    if sequencia in repeticoes:
        #pega distancia da penultima ocorrencia até a ultima 
        #Separa o primeiro indice da ultima repetição
        repeticoes[sequencia].append(i)
    else:
        repeticoes[sequencia] = []


def find_key(message, lenkey):
    english_frequencias = dict(sorted({
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
        'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
        'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
        'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
        'J': 0.10, 'Z': 0.07
    }.items()))

    portuguese_frequencias = dict(sorted({
        'A': 14.63, 'E': 12.57, 'O': 10.73, 'S': 7.81, 'R': 6.53, 'I': 6.18,
        'N': 5.05, 'M': 4.74, 'U': 4.63, 'T': 4.34, 'L': 4.14, 'D': 3.88,
        'C': 3.10, 'P': 2.80, 'V': 1.67, 'G': 1.30, 'Q': 1.20, 'F': 1.02,
        'H': 0.99, 'B': 0.83, 'Z': 0.47, 'J': 0.40, 'X': 0.21, 'K': 0.02,
        'Y': 0.01, 'W': 0.01
    }.items()))
    
    chave = ""
    for i in range(lenkey):
        frequencias_mensagem = {letter: 0 for letter in string.ascii_uppercase}
        total_caracters = 0
        for caracter in range(i, len(message) - 1, lenkey):
            frequencias_mensagem[message[caracter]] += 1
            total_caracters += 1

        for letra in frequencias_mensagem:
            frequencias_mensagem[letra] = frequencias_mensagem[letra]*100/total_caracters

        caracter_chave = ""
        diferenca_chave = -1
        for i in range(26):
            diferenca = 0
            for x, y in zip(frequencias_mensagem, portuguese_frequencias):
                diferenca += abs(frequencias_mensagem[x] - portuguese_frequencias[y])
            if diferenca < diferenca_chave or diferenca_chave == -1:
                diferenca_chave = diferenca
                caracter_chave = next(iter(frequencias_mensagem))

            # Move o dicionario, primeira posição vai pro ultimo lugar no dicionario
            move_dicionario_chave = next(iter(frequencias_mensagem))
            move_dicionario_valor = frequencias_mensagem[next(iter(frequencias_mensagem))]
            frequencias_mensagem.pop(next(iter(frequencias_mensagem)))
            frequencias_mensagem[move_dicionario_chave] = move_dicionario_valor
        # Adiciona o caracter encontrado para a chave
        chave = chave + caracter_chave
    return chave
'''
print(find_key(mensagem, 8))
'''

final = {}
for i in repeticoes:
    if len(repeticoes[i]) > 1:
        final[i] = repeticoes[i]

def lenkey(rep):
    tamanhos = []
    for sequencia, distancias_sequencia in rep.items():
        for divisor in range(1, 21):
            if all(d % divisor == 0 for d in distancias_sequencia):
                tamanhos.append(divisor * len(sequencia))
    # Calcula a média dos tamanhos encontrados para determinar o tamanho da chave
    tamanho_chave = round(sum(tamanhos) / len(tamanhos))
    return tamanho_chave

print(find_key(mensagem, lenkey(final)))

'''
#Descobre o tamanho da chave
    for tamanho_chave in reversed(range(len(tamanhos))):
        if distancia % (tamanho_chave + 2) == 0:
            tamanhos[tamanho_chave] += 1
'''

'''
for sequencia in repeticoes:
    if repeticoes[sequencia]["quantidade"] > 1:
        print(f"{sequencia}")
'''