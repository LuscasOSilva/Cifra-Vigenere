import re

mensagem = input("Digite a mensagem: ").upper() #Converte para maiúsculas

repeticoes = {}

for i in range(len(mensagem) - 2):
    sequencia = mensagem[i:i+3]
    if sequencia.isalpha(): #confere se os tres caracteres são letras
        if sequencia in repeticoes:
            repeticoes[sequencia]["quantidade"] += 1
            repeticoes[sequencia]["ultima_ocorrencia"] = i
            distancia = i - repeticoes[sequencia]["penultima_ocorrencia"]
            if 1 <= distancia <= 20:
                repeticoes[sequencia]["distancias"].append(distancia)
            repeticoes[sequencia]["penultima_ocorrencia"] = i
        else:
            repeticoes[sequencia] = {
                "quantidade": 1,
                "penultima_ocorrencia": i,
                "ultima_ocorrencia": i,
                "distancias": []
            }

for sequencia in repeticoes:
    if repeticoes[sequencia]["quantidade"] > 1:
        print(f"{sequencia}")
