# Cifra de Viginere
Este programa implementa a cifra de Vigenere, uma cifra de substituição polialfabética que usa uma palavra-chave para determinar a sequência de alfabetos a serem usados na criptografia. É possível tanto cifrar como decifrar uma mensagem com a chave que é fornecida previamente.

# Descrição "CrifradorEDescifrador"
A cifra de Vigenere é uma extensão da cifra de César, onde a letra é substituída por outra letra para posições à frente dela no alfabeto. Na cifra de Vigenere, em vez de usar um deslocamento para todas as letras da mensagem, usa-se uma palavra-chave para determinar o deslocamentos que será realizado.

O programa implementa duas funções principais: **cifra** e **decifra**. A função cifra recebe uma letra e uma chave e retorna a letra cifrada. A função decifra recebe uma letra e uma chave e retorna a letra decifrada.

A função **cifrador** lê a mensagem a ser cifrada e a chave do usuário e, em seguida, itera através de cada letra da mensagem, cifrando cada letra usando a função cifra e a chave correspondente. A função **decifrado** funciona de maneira semelhante, decifrando a mensagem usando a função decifra e a chave correspondente.

A função **escolha** permite ao usuário escolher entre cifrar ou decifrar (1 ou 2) a mensagem. Se o usuário escolher cifrar a mensagem, a função cifrador será chamada; se o usuário escolher decifrar a mensagem, a função decifrador será chamada. A mensagem cifrada ou decifrada será exibida na tela.

Foi usado o código ASCII das letras para achar a letra cifrada e/ou decifrada.

## Como Rodar
1. Abra um terminal e vá até a pasta onde se encontra o arquivo.
2. Instale a biblioteca *unidecode*
```
pip install unidecode
```
3. Execute o comando python CifradorEDecifrador.py no terminal.
```
python Cifrador&Decifrador.py
```
4. Escolha entre cifrar ou decifrar a mensagem digitando 1 ou 2 e pressionando Enter.
5. Digite a mensagem e a chave quando solicitado.
6. A mensagem cifrada ou decifrada será exibida na tela.

# Descrição "Ataque"
## Como usar

Este código tenta quebrar as mensagens criptografadas usando métodos de quebra de cifras Vigenere através de técnicas como o método de Kasiski para descobrir a chave para descriptografia.

Para quebrar a cifra Vigenere e descobrir a chave usada para criptografar uma mensagem, basta fornecer a mensagem criptografada. O script tentará determinar o tamanho da chave e, em seguida, quebrará a cifra usando uma combinação de análise de frequência de letras e o índice de coincidência.

Caso a chave encontrada não satisfaça a descriptografia, digite "n" para que o código encontre uma chave menor que possa ser correta.

## Como Rodar
1. Abra um terminal na pasta onde se encontra o arquivo.
2. Instale a biblioteca *unidecode*
```
pip install unidecode
```
3. Execute o comando python Ataque.py no terminal.
```
python Ataque.py
```
4. Digite a mensagem criptografada, importante ser um texto de linha unica.

## Exemplo
```
python Ataque.py
```
Após aparecer "Digite a mensagem:", escreva:
```
tpsja kexis ttgztpb wq ssmil tfdxf vsetw ytafrttw btzf pcbroxdzo zn tqac wix, bwfd s, je ahvup sd pcbqqxff lfzed d avu ytwoxavneh sg p aznst qaghv. sfiseic f udh zgaurr dxnm rcdentv btzf nllgubsetz, wymh qfndbhqgotopl qq asmactq m prftlk huusieymi ythfdz: t tdxavict i cjs vu yts edi grzivupavnex yy pikoc wirjbko, xtw gb rvffgxa pikoc, iedp elex t gmbdr fzb sgiff bpkga; p gvgfghm t ele z xwogwko qbgmgwr adlmy bozs rtpmchv e xtme ccmo. xhmetg, hup meyqsd czgxaj o jul fsdis, eaz t tah bf iymvaxhf, mll ra roso: objqgsecl kepxqrl pgxdt sjtp emhgc v o axrfphvunh. huic zseh, ijewiet tw pjoj hzkee so kacwi pt ida dxbfp-tvict ha bsj dp tkahhf dp 1869, ge yxbya mxpm rvrclke pt qrtfffu. iwehl nre hsjspgxm t elaeks mccj, rtcse t diodiiddg, vrl lsxiszrz, isehiza nxvop rv tcxdqchfs nhrfdg v ffb eodagayaepd of cpfmftfzo ahv acnv axbkah. cezp tquvcj! vpkhmss v qfx rmd vfugx gmghrs yxq mciecthw. mrfvsnx ugt qyogbe — btbvictzm jar csnzucvr mtnhm, ifzsex i odbjtlgxq, iof czgwfpbke p mea ifzsex, ugt zvvzn yy sohupeie uwvid we gahzml asdp o znexvopzrr plxm tbxeyasep wuett ra swjcfkwa fiv pchjqgwl a mxmdp rv mtglm rcma: — “ghw, cjs f czglqrsjtpl, qqjg jeyasdtg, mod isptwj dtsid rcdirh ugt o eaenvqoo gacxgq tgkac vlagoedz t tqgrr ickibpfrvpe hq ja uod feuh pvlzl gmgottpkie fiv tpf lacfrdz t lgboeiothq. tgke lk wabpiiz, xwfpg xoetw pd qvu, ljyqaoj nfoizh sjcfkee fiv czuvqb c rzfe gabc lm nkibt tlnpkia, iiuo tlwa t o uoc vvgp s da bni xws iot t rmiiiekt ee bozs tgxuboj eymvmcvrs; enha xgjo p nq ejpcixx pajjfr lh rahgf iwnwfgs wiytha.” qcd e qbix pazgz! gea, cof mp tvdtdvnoh hmh jznex ebdzzcpl ugt zye oxmjtw. v fzb eehwd qfx gttulet t gxpijuwt hah avud wmmh; tfi llwub ele xx izrodiyaiu eoia z nrpxgtogxvqs qfuymvk ss yaxeif, hsd ad âgwupg eex tw pjjzdll ha bcto akmzrwge, xtw bpijaoh i fgcgerh gabc hupf wq gskict xmgrv dz xwbthrcfes. fpfue p tfagfvctws. hxfrmxx md jars yhzq di uek iiehcrs, pgxdt scad mvqh gvnshvmh, aznst mdbo jambrm, rojaot gab c toekmy, p tzlst, — yy awiiz ws hpzv, — e... exrtpa ganbizrwr! dljyu p dfunh pttg uicxm cjsd ect e ftftetke etbyoct. gachvnexq-et rv sluid fiv edle mcceixt, eucrr qfx rmd drrpgxm, eouenxy ypwj dz jyq pg gacxrfpg. v vpkhmss, gaoxgqj arid. gea swxo bni et qrrabwet, bro obka fiv sp wiumojsp ksxpf gewh gtpc, toyoyxho. eex h qqj csieh idp qfidt exiodeymi pgodaebgm... ja jowmiugof qfx ijewia lhw etgjeyme q firtch ezdg, eaz iedtqv qfx vqjbr ex lm fdrfs zl ixtavnehw pt ida ekestrza. p wepd ele dbq, a fiv mpgse rcevtglm p sjsl tracwda pke meoieyme-xd. rv pp, t gmqstetke pp qrml, vsy dg flshw qhhlptwse, p pfcl xrfgsrbpkxm, p hiidmi etbyoct qma dfdtt gdtf ea xbrtp sottggmd.
```
ou qualquer outro texto sifrado com a sifra de Vigenere que quiser, temos os arquivos "desafio1.txt" e "desafio2.txt" como exemplo para serem usados.

Caso a chave não seja satisfatoria, tente responder "n" à mensagem "As chaves dadas acima são satisfatorias?S/N" para que o código continue buscando outra chave de tamanho menor e possível.

# Auxílio
## FoxCalculators
https://pt.foxcalculators.com/webtools/12173.html
## COMPARAÇÃO DE STRINGS EM PYTHON
http://excript.com/python/comparacao-de-string-python.html