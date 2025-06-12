#Dia 2: Level 2

#Comparacion de longitud entre nombre y apellido

Nombres="Carlos Michel"
Apellido="Martinez Mendoza"
print("El numero de letras que tiene el nombre es de: ", len(Nombres))
print("El numero de letras que tiene el apellido es de: ", len(Apellido))

#Declaracion de numeros

n1=5 
n2=4

#Operaciones

print("La suma es de: " , (n1 + n2))  #suma
print("La resta es de: " ,(n1 - n2))   #resta
print("La multiplicacion: ", (n1 * n2))   #multiplicacion
print("El porcentaje: ",(n1 % n2))   #porcentaje
print("El exponencial: ",(n1 ** n2))  #exponencial
print("La raiz es: ",(n1 // n2))  #nose
print("La division: ",(n1 / n2))   #division

#Datos del circulo

radio = 30
pi = 3.1416

#Proceso

area = (pi*radio ** 2)
Circu = (2 * pi * radio)

#Exponer area

print ("El área del circulo es:")
Area_circulo = (area)
print ("La circunferencia es de")
Circunferencia = (Circu)

#Radio desde Imput

user_radio = float (input("Ingrese el radio del circulo: "))
user_area = pi * user_radio ** 2
print("Área del círculo con radio del usuario: ", user_area)

#Obtener datos del usuario

user_nombre= input("Ingresa tus nombres: ")
user_apellido= input("Ingresa tus apellidos: ")
pais_user= input("Ingrese su pais: ")
año_user= input("Ingrese su edad")

print ("Nombre completo: ", user_nombre  + user_apellido)
print ("País: ", pais_user)
print ("Edad: ", año_user)