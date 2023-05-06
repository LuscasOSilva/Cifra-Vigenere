percorre_chave = 0

def cifra(letra: str, chave: str) -> str:
    if letra.isupper():
        chave = chave.upper()
    else:
        chave = chave.lower()
    if (ord(letra) >= 65 
    and ord(letra) <= 90 
    and ord(letra) + ord(chave) - 65 > 90):
        cifrada = ord(letra) + ord(chave) - 91
        return cifrada
    if (ord(letra) >= 97 
    and ord(letra) <= 122 
    and ord(letra) + ord(chave) - 97 > 122):
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
    mensagem = input("Digite a mensagem a ser descriptografada: ")
    chave = input("Digite a chave para cifragem: ")
    criptograma = ""
    for caracter in mensagem:
        if caracter.isalpha():
            criptograma = criptograma + chr(cifra(caracter, chave[percorre_chave]))
            if percorre_chave == len(chave) - 1:
                percorre_chave = 0
            else:
                percorre_chave += 1
        else:
            criptograma = criptograma + caracter

    return criptograma

def decifrador():
    global percorre_chave
    criptograma = input("Digite a mensagem a ser decifrada: ")
    chave = input("Digite a chave usada para cifragem: ")
    mensagem = ""
    for caracter in criptograma:
        if caracter.isalpha():
            mensagem = mensagem + chr(decifra(caracter, chave[percorre_chave]))
            if percorre_chave == len(chave) - 1:
                percorre_chave = 0
            else:
                percorre_chave += 1
        else:
            mensagem = mensagem + caracter

    return mensagem

def escolha():
    choice = int(input("Escolha\n1 - Cifrador\n2 - decifrador:\n"))

    if choice == 1:
        print(cifrador())
    if choice == 2:
        print(decifrador())

escolha()