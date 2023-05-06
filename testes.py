'''
mensagem = input("Digite a mensagem: ").upper()#converte para maiúsculas

frequencias = {} # dicionário para armazenar as frequências das sequências de 3 caracteres
for i in range(len(mensagem) - 2):
    if mensagem[i:i+3].isalpha(): #confere se os tres caracteres são letras
        seq = mensagem[i:i+3]
        if seq not in frequencias:
            frequencias[seq] = [i]
        else:
            frequencias[seq].append(i)

# exibe as frequências de cada sequência
for seq, freqs in frequencias.items():
    print(f"A sequência '{seq}' aparece {len(freqs)} vezes nas posições {freqs}")

divisores_comuns = {} # dicionário para armazenar os divisores comuns das frequências
for i in range(1, 21):
    divisores_comuns[i] = []
    for seq, freqs in frequencias.items():
        if len(freqs) % i == 0:
            divisores_comuns[i].append(seq)

# exibe os divisores comuns das frequências
for i in range(1, 21):
    if divisores_comuns[i]:
        print(f"As sequências {divisores_comuns[i]} aparecem em frequência divisível por {i}")
'''




'''
import collections
import math
import re

# Função para encontrar todas as repetições de uma sequência na mensagem cifrada
def encontrar_repeticoes(mensagem_cifrada, tamanho_sequencia):
    repeticoes = collections.defaultdict(list)
    for i in range(len(mensagem_cifrada) - tamanho_sequencia + 1):
        sequencia = mensagem_cifrada[i:i+tamanho_sequencia]
        # Ignora sequências com caracteres especiais ou espaços
        if not re.match('^[A-Za-z]+$', sequencia):
            continue
        repeticoes[sequencia].append(i)
    return repeticoes

# Função para calcular as distâncias entre as repetições de uma sequência
def calcular_distancias(repeticoes):
    distancias = collections.defaultdict(list)
    for sequencia, indices in repeticoes.items():
        for i in range(len(indices) - 1):
            distancia = indices[i+1] - indices[i]
            distancias[sequencia].append(distancia)
    return distancias

# Função para encontrar o tamanho da chave
def encontrar_tamanho_chave(mensagem_cifrada):
    # Encontra as repetições de sequências de 3 caracteres na mensagem cifrada
    repeticoes = encontrar_repeticoes(mensagem_cifrada, 3)
    # Calcula as distâncias entre as repetições
    distancias = calcular_distancias(repeticoes)
    # Encontra os divisores comuns das distâncias para determinar o tamanho da chave
    tamanhos = []
    for sequencia, distancias_sequencia in distancias.items():
        for divisor in range(1, 21):
            if all(d % divisor == 0 for d in distancias_sequencia):
                print(divisor)
                tamanhos.append(divisor * len(sequencia))
    # Calcula a média dos tamanhos encontrados para determinar o tamanho da chave
    tamanho_chave = round(sum(tamanhos) / len(tamanhos))
    return tamanho_chave

print(encontrar_tamanho_chave(input("cuzin?")))
'''



'''
def descobrir_chave(criptograma):
    tam_chave = len(criptograma)
    chave = [""] * tam_chave
    for i in range(tam_chave):
        frequencias = [0] * 26
        for j in range(i, len(criptograma), tam_chave):
            letra = criptograma[j]
            if letra.isalpha():
                frequencias[ord(letra.upper()) - ord('A')] += 1
        letra_e = max(range(26), key=lambda x: frequencias[x])
        deslocamento = (letra_e - ord('E')) % 26
        chave[i] = chr(ord('A') + deslocamento)
    return "".join(chave)

print(descobrir_chave(input("zucin")))
'''
'''
import collections
import math

mensagem = ''.join(filter(str.isalpha, input("Digite a mensagem: ").upper())) #Converte para maiúsculas

repeticoes = {}

for i in range(len(mensagem) - 2):
    sequencia = mensagem[i:i+3]
    if sequencia in repeticoes:
        #pega distancia da penultima ocorrencia até a ultima 
        #Separa o primeiro indice da ultima repetição
        repeticoes[sequencia].append(i)
    else:
        repeticoes[sequencia] = []

final = {}
for i in repeticoes:
    if len(repeticoes[i]) > 1:
        final[i] = repeticoes[i]

print(final)

def encontrar_tamanho_chave(dicionario_sequencias):
    # Extrair as sequências do dicionário
    sequencias = list(dicionario_sequencias.keys())
    
    # Calcular as distâncias entre as ocorrências de cada sequência
    distancias = {}
    for seq in sequencias:
        posicoes = dicionario_sequencias[seq]
        distancias_seq = [posicoes[i+1] - posicoes[i] for i in range(len(posicoes)-1)]
        distancias[seq] = distancias_seq
    
   # Calcular os divisores comuns entre as distâncias
    divisores_comuns = set(range(5, 21)) # considerando distâncias entre 2 e 20 caracteres
    for distancias_sequencia in distancias.values():
        divisores_comuns_seq = set(divisor for divisor in divisores_comuns if all(d % divisor == 0 for d in distancias_sequencia))
        if divisores_comuns_seq:
            divisores_comuns &= divisores_comuns_seq

    # Retornar o menor divisor comum encontrado
    return min(divisores_comuns)


print(encontrar_tamanho_chave(final))
'''

'''import string

frequencias_mensagem = {letter: 0 for letter in string.ascii_uppercase}
print(frequencias_mensagem["A"])
print(dict(sorted({
        'A': 14.63, 'E': 12.57, 'O': 10.73, 'S': 7.81, 'R': 6.53, 'I': 6.18,
        'N': 5.05, 'M': 4.74, 'U': 4.63, 'T': 4.34, 'L': 4.14, 'D': 3.88,
        'C': 3.10, 'P': 2.80, 'V': 1.67, 'G': 1.30, 'Q': 1.20, 'F': 1.02,
        'H': 0.99, 'B': 0.83, 'Z': 0.47, 'J': 0.40, 'X': 0.21, 'K': 0.02,
        'Y': 0.01, 'W': 0.01
    }.items())))
message = "rvgllakieg tye tirtucatzoe.  whvnvvei i winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg, drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl. wzty a pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis. zf khep blt keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv."
for caracter in range(0, len(message) - 1, 5):
    print(message[caracter])
print(abs(10-15))
'''
frequencias_mensagem = {"A": 1, "B": 2, "C": 3}
print(frequencias_mensagem)
move_dicionario_chave = next(iter(frequencias_mensagem))
move_dicionario_valor = frequencias_mensagem[next(iter(frequencias_mensagem))]
frequencias_mensagem.pop(next(iter(frequencias_mensagem)))
frequencias_mensagem[move_dicionario_chave] = move_dicionario_valor
print(frequencias_mensagem)