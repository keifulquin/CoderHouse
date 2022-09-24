#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#
#- Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#
#- Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#
#- Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#
#- Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#
#- Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
#🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))#




a=list(range(0, 11))
print(a)
b=list(range(-10, 1))
print(b)
c=list(range(0, 22, 2))
print(c)
d=list(range(-21, 0, 2))
print(d)
e=list(range(0, 55, 5))
print(e)