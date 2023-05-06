# Cifra de Viginere
Este programa implementa a cifra de Vigenere, uma cifra de substituição polialfabética que usa uma palavra-chave para determinar a sequência de alfabetos a serem usados na criptografia. É possível tanto cifrar como decifrar uma mensagem com a chave que é fornecida previamente.

# Descrição "Crifrador & Descifrador"
A cifra de Vigenere é uma extensão da cifra de César, onde a letra é substituída por outra letra para posições à frente dela no alfabeto. Na cifra de Vigenere, em vez de usar um deslocamento para todas as letras da mensagem, usa-se uma palavra-chave para determinar o deslocamentos que será realizado.

O programa implementa duas funções principais: **cifra** e **decifra**. A função cifra recebe uma letra e uma chave e retorna a letra cifrada. A função decifra recebe uma letra e uma chave e retorna a letra decifrada.

A função **cifrador** lê a mensagem a ser cifrada e a chave do usuário e, em seguida, itera através de cada letra da mensagem, cifrando cada letra usando a função cifra e a chave correspondente. A função **decifrado** funciona de maneira semelhante, decifrando a mensagem usando a função decifra e a chave correspondente.

A função **escolha** permite ao usuário escolher entre cifrar ou decifrar (1 ou 2) a mensagem. Se o usuário escolher cifrar a mensagem, a função cifrador será chamada; se o usuário escolher decifrar a mensagem, a função decifrador será chamada. A mensagem cifrada ou decifrada será exibida na tela.

## Como Rodar
1. Abra um terminal na pasta onde se encontra o arquivo.
2. Execute o comando python Cifrador & Decifrador.py no terminal.
```
python Cifrador & Decifrador.py
```
3. Escolha entre cifrar ou decifrar a mensagem digitando 1 ou 2 e pressionando Enter.
4. Digite a mensagem e a chave quando solicitado.
5. A mensagem cifrada ou decifrada será exibida na tela.

# Descrição "Ataque"
## Como usar
Este código criptografa e decriptografa mensagens usando a criptografia Vigenere. Ele também tenta quebrar as mensagens criptografadas usando métodos de quebra de cifras Vigenere.

Para criptografar uma mensagem, basta executar o script e seguir as instruções na linha de comando. O script solicitará a mensagem a ser criptografada e a chave a ser usada para criptografar a mensagem. Em seguida, ele imprimirá a mensagem criptografada.

Para decriptografar uma mensagem, basta fornecer a mensagem criptografada e a chave usada para criptografar a mensagem. Em seguida, o script imprimirá a mensagem original.

Para quebrar a cifra Vigenere e descobrir a chave usada para criptografar uma mensagem, basta fornecer a mensagem criptografada. O script tentará determinar o tamanho da chave e, em seguida, quebrará a cifra usando uma combinação de análise de frequência de letras e o índice de coincidência.

## Exemplo
```bash
python Ataque.py
```
Digite a mensagem: Esta é uma mensagem secreta
Digite a chave: segredo
Mensagem criptografada: YHOP È T CVLDJDL VKXJSF

Digite a mensagem criptografada: YHOP È T CVLDJDL VKXJSF
Chave: segredo
Mensagem original: ESTA E UMA MENSAGEM SECRETA

Digite a mensagem criptografada: RGKGMFCIQQFNDKLZEPVXZANOLNVEYVQWRTTXPKBOKVHKCPNIN
FTGBGBCWZLTUCNLZVXVLGLTVJLZTHFTECZHHTJTHMCS
PXEKGTFXTZXQKPUEIZCBRWEZQOWDLAHFBPOJLHFXRS
RAFFELDGKMIKTDFMWCBPIHUKJIZMDCRQDSZSYUPBLH
UYJDKSJAHVLPMGTVDDZIVLHMXCNVUJCOAZUMLZVZZX
ORCMTJYSLYEWOWTJLGPIRXKZSKOYPNRLGYPTDZPGRO
ZPPXIOZPVEGCEMKNQPLDCJSPVDCUNBJGAIKCXRKSMW
FBOBKKRYZLVXSCZALFFCZSBFXCWZLZNJFMQDCSPCJL
WSWLRGJDJJYFVWHIUCBMDPYGCTZLFXDKHRMEHSPFAW
HPPLJCE
Chave: desvendandoacifra
Mensagem original: A HISTORIA DO MUNDO E UMA HISTORIA DE GUERRA.