import re

mensagem = ''.join(filter(str.isalpha, input("Digite a mensagem: ").upper())) #Converte para maiúsculas

repeticoes = {}
tamanhos = [0]*19

for i in range(len(mensagem) - 2):
    sequencia = mensagem[i:i+3]
    if sequencia in repeticoes:
        repeticoes[sequencia]["quantidade"] += 1
        distancia = i - repeticoes[sequencia]["ultima_ocorrencia"]
        for tamanho_chave in reversed(range(len(tamanhos))):
            if distancia % (tamanho_chave + 2) == 0:
                tamanhos[tamanho_chave] += 1
                distancia = tamanho_chave/2
        repeticoes[sequencia]["ultima_ocorrencia"] = i+3
    else:
        repeticoes[sequencia] = {
            "quantidade": 1,
            "ultima_ocorrencia": i+3
        }
print(tamanhos)
'''
for sequencia in repeticoes:
    if repeticoes[sequencia]["quantidade"] > 1:
        print(f"{sequencia}")
'''