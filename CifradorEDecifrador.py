from unidecode import unidecode

#Luana Cruz Silva 202033543 - Lucas de Oliveira Silva 200022857

percorre_chave = 0

# Função que usa o codigo ASCII das letras para cifragem
def cifra(letra: str, chave: str) -> str:
    # Garante que as letras terão o mesmo tipo
    if letra.isupper():
        chave = chave.upper()
    else:
        chave = chave.lower()
    if (ord(letra) >= 65 
    and ord(letra) <= 90 
    and ord(letra) + ord(chave) - 65 > 90):
    # Subtrai o valor do inicio das letra em ASCII + 26 (valor do alfabeto)
        cifrada = ord(letra) + ord(chave) - 91
        return cifrada
    if (ord(letra) >= 97 
    and ord(letra) <= 122 
    and ord(letra) + ord(chave) - 97 > 122):
    # Subtrai o valor do inicio das letra em ASCII + 26 (valor do alfabeto)
        cifrada = ord(letra) + ord(chave) - 123
        return cifrada
    if ord(letra) >= 65 and ord(letra) <= 90:
        cifrada = ord(letra) + ord(chave) - 65
        return cifrada
    if ord(letra) >= 97 and ord(letra) <= 122:
        cifrada = ord(letra) + ord(chave) - 97
        return cifrada

def decifra(letra: str, chave: str) -> str:
    if letra.isupper():
        chave = chave.upper()
    else:
        chave = chave.lower()
    if (ord(letra) >= 65 
        and ord(letra) <= 90 
        and ord(letra) - ord(chave) + 65 < 65):
        decifrada = ord(letra) - ord(chave) + 91
        return decifrada
    if (ord(letra) >= 97 
        and ord(letra) <= 122 
        and ord(letra) - ord(chave) + 97 < 97):
        decifrada = ord(letra) - ord(chave) + 123
        return decifrada
    if ord(letra) >= 65 and ord(letra) <= 90:
        decifrada = ord(letra) - ord(chave) + 65
        return decifrada
    if ord(letra) >= 97 and ord(letra) <= 122:
        decifrada = ord(letra) - ord(chave) + 97
        return decifrada

def cifrador():
    global percorre_chave
    mensagem = unidecode(input("Digite a mensagem a ser criptografada: "))
    chave = unidecode(input("Digite a chave para criptografia: "))
    criptograma = ""
    for caracter in mensagem:
        # Confere se é letra
        if caracter.isalpha():
            # Sendo letra, ele irá chamar a função que criptografa a letra
            # Letra criptografada adicionada ao criptograma
            criptograma = criptograma + chr(cifra(caracter, chave[percorre_chave]))
            # Percorre os endereços da chave
            if percorre_chave == len(chave) - 1:
                # Se estivermos no ultimo caracter da chave, voltamos para o primeiro
                percorre_chave = 0
            else:
                percorre_chave += 1
        else:
            # Se não for letra, apenas adiciona o caracter no criptograma ex:"," " "
            criptograma = criptograma + caracter

    return f'O Criptograma criado é: \n\n{criptograma}'

def decifrador():
    global percorre_chave
    criptograma = unidecode(input("Digite a mensagem a ser decifrada: "))
    chave = unidecode(input("Digite a chave usada para cifragem: "))
    mensagem = ""
    for caracter in criptograma:
        if caracter.isalpha():
            # Sendo letra, ele irá chamar a função que decifra a letra
            # Letra criptografada adicionada ao criptograma
            mensagem = mensagem + chr(decifra(caracter, chave[percorre_chave]))
            # Percorre os endereços da chave
            if percorre_chave == len(chave) - 1:
                # Se estivermos no ultimo caracter da chave, voltamos para o primeiro
                percorre_chave = 0
            else:
                percorre_chave += 1
        else:
            # Se não for letra, apenas adiciona o caracter no criptograma ex:"," " "
            mensagem = mensagem + caracter

    return f'A mensagem descriptografada é: \n\n{mensagem}'

def escolha():
    choice = int(input("Escolha\n1 - Cifrador\n2 - Decifrador:\n"))

    if choice == 1:
        print(cifrador())
    if choice == 2:
        print(decifrador())

escolha()