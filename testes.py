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
