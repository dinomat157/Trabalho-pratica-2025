def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisao por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação invalida"
    return resultado

saida = ''
while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
        operacao = input('Digite a operaçao (+, -, *, /) ou o nome da operaçao (adicao, subtracao, multiplicacao, divisao): ').strip()

        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operaçao:', resultado)

    except ValueError:
        print("Por favor, insira numeros validos.")
    saida = input('Deseja continuar? (S/N): ').strip()
print('Programa encerrado.')