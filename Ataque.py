from unidecode import unidecode
import collections
import string

# Luana Cruz Silva 202033543 - Lucas de Oliveira Silva 200022857

def message():
    # Retira o que não for letra, deixa tudo em letras maisculas e retira acentos
    mensagem = unidecode(''.join(filter(str.isalpha, input("Digite a mensagem: ").upper())))
    return mensagem

def find_rep(mensagem):
    repeticoes = {}

    for i in range(len(mensagem) - 2):
        sequencia = mensagem[i:i+3]
        if sequencia in repeticoes:
            #pega distancia da penultima ocorrencia até a ultima 
            #Separa o primeiro indice da ultima repetição
            repeticoes[sequencia].append(i)
        else:
            repeticoes[sequencia] = []
    # Separa apenas os padrões que foram encontrados mais de 1 vez
    final = {}
    for i in repeticoes:
        if len(repeticoes[i]) > 1:
            final[i] = repeticoes[i]
    return final

def lenkey(rep):
    tamanhos = []
    for sequencia, distancias_sequencia in rep.items():
        for divisor in range(1, 21):
            if all(d % divisor == 0 for d in distancias_sequencia):
                tamanhos.append(divisor * len(sequencia))
    # Calcula a média dos tamanhos encontrados para determinar o tamanho da chave
    tamanho_chave = round(sum(tamanhos) / len(tamanhos))
    return tamanho_chave

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

    chave_portugues = ""
    chave_ingles = ""
    for i in range(lenkey):
        frequencias_mensagem = {letter: 0 for letter in string.ascii_uppercase}
        total_caracters = 0
        for caracter in range(i, len(message) - 1, lenkey):
            frequencias_mensagem[message[caracter]] += 1
            total_caracters += 1

        for letra in frequencias_mensagem:
            frequencias_mensagem[letra] = frequencias_mensagem[letra]*100/total_caracters

        caracter_chave_portugues = ""
        diferenca_chave_portugues = -1
        # Achar chave em portugues comparando as frequencias do texto com as da lingua portuguesa
        for i in range(26):
            diferenca = 0
            for x, y in zip(frequencias_mensagem, portuguese_frequencias):
                diferenca += abs(frequencias_mensagem[x] - portuguese_frequencias[y])
            if diferenca < diferenca_chave_portugues or diferenca_chave_portugues == -1:
                diferenca_chave_portugues = diferenca
                caracter_chave_portugues = next(iter(frequencias_mensagem))

            # Move o dicionario, primeira posição vai pro ultimo lugar no dicionario
            move_dicionario_chave = next(iter(frequencias_mensagem))
            move_dicionario_valor = frequencias_mensagem[next(iter(frequencias_mensagem))]
            frequencias_mensagem.pop(next(iter(frequencias_mensagem)))
            frequencias_mensagem[move_dicionario_chave] = move_dicionario_valor

        caracter_chave_ingles = ""
        diferenca_chave_ingles = -1
        # Achar chave em ingles comparando as frequencias do texto com as da lingua inglesa
        for i in range(26):
            diferenca = 0
            for x, y in zip(frequencias_mensagem, english_frequencias):
                diferenca += abs(frequencias_mensagem[x] - english_frequencias[y])
            if diferenca < diferenca_chave_ingles or diferenca_chave_ingles == -1:
                diferenca_chave_ingles = diferenca
                caracter_chave_ingles = next(iter(frequencias_mensagem))

            # Move o dicionario, primeira posição vai pro ultimo lugar no dicionario
            move_dicionario_chave = next(iter(frequencias_mensagem))
            move_dicionario_valor = frequencias_mensagem[next(iter(frequencias_mensagem))]
            frequencias_mensagem.pop(next(iter(frequencias_mensagem)))
            frequencias_mensagem[move_dicionario_chave] = move_dicionario_valor
        # Adiciona o caracter encontrado para a chave
        chave_portugues = chave_portugues + caracter_chave_portugues
        chave_ingles = chave_ingles + caracter_chave_ingles
    return f'\nChave texto PT-BR = "{chave_portugues}"\nChave texto EN = "{chave_ingles}"'

# Função que apenas confere se a chave é valida para o usuario
def retornar_resposta(mensagem, tamanho_chave):
    print(find_key(mensagem, tamanho_chave))
    escolha = input(f'\nAs chaves dadas acima são satisfatorias?S/N\n').upper()
    if escolha == "N":
        # Caso a chave não seja válida para o usuario, é possível procurar outra chave menor
        retornar_resposta(mensagem,tamanho_chave - 1)
    else:
        print(":D")

mensagem = message()
tamanho_chave = lenkey(find_rep(mensagem))

retornar_resposta(mensagem, tamanho_chave)
