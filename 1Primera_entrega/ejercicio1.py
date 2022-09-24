#CONSIGNA:

#"Crear un programa para calcular la nota final del estudiante en base a dos exámenes, los exámenes cuentan con un porcentaje distinto de la nota final"

#nota_1 cuenta como el 40% de la nota final
#nota_2 cuenta como el 60% de la nota final
#Aspectos a incluir: Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. Los datos deben guardarse en variables y deben ser dinámicos por medio de input.


#Solucion

val1=int(input("Primer Nota "))
val2=int(input("Segunda Nota "))
nota_1=val1*40
nota_2=val2*60
suma = nota_1+nota_2
print("Nota Final", suma/100)
