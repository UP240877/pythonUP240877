#1.Creacion de diccionario vacio
dog={}

#2.Agregar informacion al diccionario
dog["name"]= "Akira"
dog["color"] = "Black and white"
dog["breed"] = "Mixta"
dog["legs"]= "4"
dog["age"]="5 meses"
print(dog)

#3.Crear un diccionario de estudiante y agregar informacion
estudiante={}

estudiante["first_name"]="Carlos"
estudiante["last_name"]="Martinez"
estudiante["gender"]="Masculino"
estudiante["age"]="20 años"
estudiante["marital_statues"]="Soltero"
estudiante["skills"]="Agilidad mental, adaptibilidad, "
estudiante["country"]="Mexico"
estudiante["city"]="Aguascalientes"
estudiante["address"]="Infonavit Morelos"

print(estudiante)

#4.Obtener longitud del diccionario "estudiante"
print("Longitud del diccionario Estudiante es de: ", len(estudiante))

#5.Obtener valor de skills y verficar su tipo de dato
skills=estudiante["skills"]
print(type(skills))

#6.Modificar el valor de skills agregando uno o dos habilidades
skills=skills+"Coordinacion","Velocidad de lectura"
print(skills)

#7.Obtener las claves del diccionario como una lista
claves=list(estudiante)
print(claves)

#8.Obtener los valores del diccionario como una lista
valores=list(estudiante.values())
print(valores)

#9.Convertir el diccionario a una lista de tuplas
tupla=estudiante.items()
print(tupla)

#10.Eliminar uno de los elemtos del diccionario
estudiante.pop("first_name")
print(estudiante)

#11.Eliminar uno de los diccionarios
del dog