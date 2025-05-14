#funçoes sao blocos de codigo que podemos criar e usar sempre que quiser. como se fosse uma caixa , atribuimos um nome e uma açao
#depois podemos chamar essa caixa para que ela execute oque tem dentro
#nesse exemplo o "def" cria a funçao chamada "imprimir_variavel"
#dentro da funçao nos colocamos oque ela vai fazer , e neste caso ela cria a variavel "texto" e imprime a frase "Olá, funções em Python"
#quando for chamada a funçao "imprimir_variavel()"


def imprimir_variavel():
    texto = 'Olá, funções em Python'
    print(texto)

imprimir_variavel()