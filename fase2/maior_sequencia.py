"""
Problema: Maior sequência crescente
Dada uma lista de N números inteiros, você deve descobrir qual é o tamanho da maior sequência de números consecutivos que está em ordem estritamente crescente.
Uma sequência crescente é aquela em que cada número é maior que o anterior.
Entrada
A primeira linha contém um inteiro N.
A segunda linha contém N números inteiros.
Saída
Imprima um único inteiro: o tamanho da maior sequência crescente encontrada.
"""

n = int(input())
lista = []
cont = 0
maior = []

for i in range(0,n):
    temp = int(input())
    lista.append(temp)

for i in range(1, len(lista)):
    atual = lista[i]

    anterior = lista[i - 1]

    print(f"Anterior : {anterior}")
    print(f"atual: {atual}")
    if atual > anterior:
        cont += 1
        maior.append(cont)
    else:
        cont = 1
print(max(maior))