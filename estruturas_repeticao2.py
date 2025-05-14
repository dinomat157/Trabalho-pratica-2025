
#for e usado quando eu preciso repetir algo , percorrer uma sequencia de coisas ,
#como uma itens de uma lista , numeros dentro de um intervalo. o for passa por cada item.


#no primeiro exemplo o for vai passando por cada letra da frase que esta em "texto" uma de cada vez e vai imprimindo o caractere
texto = 'Olá, laço for.'

for item in texto:
    print('Caractere: ' + item)
#-------------------------------------------------

#no segundo exemplo o for esta rodando de 1 ate 10 (range1,11), ele vai contando numero por numero e mostrando o resultado
for numero in range(1, 11):
    print('Número do intervalo: ' + str(numero))