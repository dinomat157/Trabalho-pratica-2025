#O while e usado quando precisa repetir alguma coisa enquanto uma condiçao for verdadeira
#nesse exemplo a variavel "entrada_idade" e uma str e esta vazia
#o while vai continuar sendo executado enquanto o valor digitado for diferente de "0"
entrada_idade = ''

while str(entrada_idade) != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    print ('Número digitado:', entrada_idade)