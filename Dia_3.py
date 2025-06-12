#1. Datos personales
edad = 20
#2 
altura = 1.65 
#3
numerocomplejo = 5+6j

#4. Perimetro de triangulo

a=5
b=4
c=3
print ("El perimetro del triangulo es de: ", (a+b+c))

#5. practica con informacion ingresada por el usuario

print("Porfavor, ingrese los datos del triangulo que se le solicitan: ")
a_user = float ( input ("Medida del lado (a): "))
b_user = float ( input ("Medida del lado (b): "))
c_user = float ( input ("Medida del lado (c): "))
print("El perimetro del triangulo es de: ", (a_user + b_user + c_user))

altura = float(input("Ingrese la altura del triangulo : "))
base = float(input("Ingrese la base del triangulo: "))
area = (altura* base)/2
perimetro= 2 * (altura + base)
print("El area es de:", area)
print("El perimetro es de:", perimetro)

#6. practica con rectangulo
print("Porfavor, ingrese los datos sobre el rectangulo que se le soliciten")
l1 = float (input("Medida de la base: "))
l2 = float(input ("Medida de la altura: "))
perimetro_r = 2 * (l1+l2)
area_r= (l1*l2)
print ("El perimetro es de: ", (perimetro_r))
print ("El area es de: ", (area_r))

#7 practica con circulo
print ("Porfavor, ingrese la informacion del circulo que se le solicite: ")
radio = float (input("Medida del radio: "))
pi = 3.14
area_c= (pi* radio * radio)
circunferencia = 2 * (pi * radio)
print ("El radio es de: ",radio)
print ("La circunferencia es de: ",circunferencia)

#8. punto de interseccion

pendiente = 2
x = 1
y= -2
print("La pendiente es de:", pendiente)
print("El punto de interseccion del punto X es :", x)
print("El punto de interseccion del punto Y es :", y)

#9. pendinete establecida

import math

x1, y1 = 2, 2
x2, y2 = 6, 10

pendiente = (y2 - y1) / (x2 - x1)

#10. Cálculo de la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La pendiente es de:", pendiente)
print("La distancia es de :", distancia)

#11.Comparacion de pendientes

pendiente1=2
pendiente2=2
print ("¿Las pendientes son inguales?: ",(pendiente1==pendiente2) )

#12.busqueda de pendiente en base de funcion

x_Variable= -3
y= x_Variable**2 + 6*x_Variable + 9
print ("Si y= x^2 + 6x + 9; entonces el valor de Y es de: ", y )
print ("Y el valor de X es de: ", x_Variable)

#13.comparacion python y dragon

print ("Paython es mas complejo que Dragon")
payton=1
dragon=2
print ("Eso es: ", payton==dragon)

#14. Dentro del texto

print("¿Esta dragon dentro de python?")
print("En" not in "dragon" and "en" not in "python") 

#15. Verificacion de palabras dentro del texto

frase="I hope this course is not full of jargon"
print("I hope this course is not full of jargon")
print("¿Esta la palabra 'jargon' dentro de la frase?")
print("jargon" in frase)

#16. Dentro del texto

print("¿Esta dragon y python en la frase?")
print("on" not in "dragon" and "on" not in "python")  

#16.1. Longitud de palabra

longitud= len("paython")
lon_cadena = str(longitud)
print("El largo de la palabra es de: ", lon_cadena)

#17. Numero par

num = float( input ("Ingresa un numero: "))
print("¿El numero es par?")
print("Eso es: ", num % 2 == 0)

#18. Da como resultado ¿2.7?

division=7//3
n_esp=2.7
print("¿La operacion de 7 // 3 da como resultado 2.7?")
print("Eso es: ", division==n_esp)

#19. Comparacion entre 10´s

print("Es lo mismo 10 que '10'")
print (type ('10') == type(10))

#20. Comparacion entre numeros

print("Es lo mismo '9.8' que 10")
print (int (9.8)==10)

# 21. Cálculo de salario

horas = int(input("Ingresa las horas trabajadas: "))
tarifa = int(input("Ingresa la tarifa por hora: "))
pago = horas * tarifa
print("Tu ganancia semanal es", pago)


# 22. Calcular segundos vividos

años = int(input("Ingresa el número de años que has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos.")

# 23. Mostrar tabla

for i in range(1, 6):
    print(i, 1, i, i**3)
