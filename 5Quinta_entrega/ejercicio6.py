#CONSIGNA:

#Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.

#La primera con los números pares, y la segunda con los números impares:

#🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

#Por ejemplo:
#pares, impares = separar([6,5,2,1,7])#
#print(pares)   # valdría [2, 6]#
#print(impares)  # valdría [1, 5, 7]#
pares= []
impares= []
def separar(lista):
    lista.sort()
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)



separar([16, 3, 25, 86, 11, 1, 4])
print("Lista de pares:", pares)
print("Lista de impares:", impares)



