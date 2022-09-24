#CONSIGNA:

#La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

#🖐 Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista.


# Partirás de: 
#matriz = [ 
#    [1, 5, 1],
#    [2, 1, 2],
#    [3, 0, 1],
#    [1, 4, 4]
#]

#Debes llegar a: 

#matriz = [ 
#    [1, 5, 1, 7],
#    [2, 1, 2, 5],
#    [3, 0, 1, 4],
#    [1, 4, 4, 9]
#]


#Solucion

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

lista0=sum(matriz[0])
lista1=sum(matriz[1])
lista2=sum(matriz[2])
lista3=sum(matriz[3])

matriz[0].append(lista0)  
matriz[1].append(lista1)
matriz[2].append(lista2)
matriz[3].append(lista3)

matriz
