num = int(input("Elija un número impar: "))

while num % 2 == 0 :
    num = int(input("Inténtelo otra vez: "))
else :
    print ("Tu número es: ", num)
