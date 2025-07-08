# DESAFIO DO CAPÍTULO 5 - CALCULADORA EM PYTHON

def soma(n1,n2):
    resultado = n1 + n2
    return print("\n",n1, " + ", n2, " = ", resultado)

def sub(n1,n2):
    resultado = n1 - n2
    return print("\n",n1, " - ", n2, " = ", resultado)

def multp(n1,n2):
    resultado = n1 * n2
    return print("\n",n1, " x ", n2, " = ", resultado)

def div(n1,n2):
    if n2 != 0:
        resultado = n1 / n2
        return print("\n",n1, " / ", n2, " = ", resultado)
    else:
        print("\nERRO: Não é possível divisão por zero!")

opcao = True

while opcao:

    opcao = input("\n\n***** CALCULADORA *********\n\n" \
    "1 - Soma\n" \
    "2 - Subtração\n" \
    "3 - Multiplicação\n" \
    "4 - Divisão\n" \
    "0 - Sair\n\n" \
    "Digite a operação desejada: ")

    if opcao == '0':
        print("\nAté logo.. \n")
        break
    
    if opcao in ['1','2','3','4']:
        try:
            n1 = int(input("\nDigite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
        except ValueError:
            print("\nERRO: Digite apenas números inteiros válidos!")
            continue

        if (opcao == '1'):
            soma(n1,n2)
        elif (opcao == '2'):
            sub(n1,n2)
        elif (opcao == '3'):
            multp(n1,n2)
        elif (opcao == '4'):
            div(n1,n2)

    else:
        print("\nOpção inválida, tente novamente..")
        continue



