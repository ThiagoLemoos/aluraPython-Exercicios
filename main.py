import os

"""1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual."""

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
listaNomes = ["Thiago", "Igor", "Rafael", "Lucas"]
listaAno = [2003, 2024]
listaNumerosImpares = []
"""2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista."""
for numero in listaNumeros:
    print(numero)


"""3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."""
for numero in listaNumeros:
    if numero % 2 != 0:
        listaNumerosImpares.append(numero)

soma = 0

for numero in listaNumerosImpares:
    soma += numero

print (soma)

"""4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente."""
listaNumeros.sort(reverse=True)
for numero in listaNumeros:
    print(numero)    


"""5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."""
numeroDigitado = int(input("Digite um número: "))
for numero in listaNumeros:
    total = numeroDigitado + numero
    print(f"{numeroDigitado} + {numero} = {total}")


"""6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções."""
soma2 = 0
for numero in listaNumeros:
    try:
        soma2 = soma2 + numero
    except:
        print("error")

print(soma2)
"""7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia."""

mediaLista = [1,5,10,15,2]
numeroDeElementos = len(mediaLista)
soma3 = 0
try:
    for numero in mediaLista:
        soma3 = numero + soma3
    media = soma3 / numeroDeElementos
    print(media)
except:
    print("error")
