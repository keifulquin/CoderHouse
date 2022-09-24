#CONSIGNA:

#A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

#La primera nota vale un 15% del total

#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
#Ejemplos:

#nota_1 = 10

#nota_2 = 7

#nota_3 = 4


#Solucion

val1=int(input("Primer Nota "))
val2=int(input("Segunda Nota "))
val3=int(input("Tercera Nota "))
nota_1=val1*15
nota_2=val2*35
nota_3=val3*50
suma = nota_1+nota_2+nota_3
media= suma/100
print("Nota Final", media)