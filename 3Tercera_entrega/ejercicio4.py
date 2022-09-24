#Escribí un programa que pida al usuario cuantos números quiere introducir.

#Luego lee todos los números y realiza una media aritmética


#inicio = 1
#cant= int(input("Indique cuantos numeros quiere ingresar"))
#while inicio <= cant:
#    numeros=int(input("Numero: "))
#    inicio +=1

#print("La media es: ", sum(numeros)//cant)



suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)