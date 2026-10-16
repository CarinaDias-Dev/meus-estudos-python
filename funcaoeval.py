def calcular_expressao():
    #solicitar ao usuário que insira uma expressão matemática
    expressao = input("Digite uma expressão matamática: ")

    try:
        #Avaliar a expressão usando eval
        resultado = eval(expressao)
        print("O resultado da expressão é: ", resultado)
    except exception as e:
        print("Erro ao avalias a expressão: ", e)

#chamar a função
calcular_expressao()
#exemplo da chamada do programa:
#Digite uma expresão matemática: 2+3*(4-1)
#O resultado da expressão é: 11