#1.Pedir al usuario su edad 
edad= int(input("Ingrese su edad: "))
if edad >= 18:
 print("Eres lo suficientemente mayor para conducir")

else:
 menor= 18-edad
 print(f"Te faltan", menor , "años para poder conducir")

#2.Comparar la edad del usuario con la mia
yo = 20
usuario=int(input("Ingrese su edad: "))
if usuario > yo:
 diferencia = usuario -yo
 print("Tienes", diferencia , "años mas que yo")
elif usuario < yo:
  dif=yo - usuario
  print("Eres", dif ,"mas chico que yo")
else:
 print("Tenemos la misma edad")

#3. Obtener dos números del usuario
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))

if n1 > n2:
 print(n1, "es mayor que", n2)

elif n1 < n2:
 print(n2 ,"es mayor que", n1)

else:
 print(n1 , "es igual a " , n2 )

             #Nivel 2:

#1.Asignacion de calificaciones segun puntaje
calificacion=int(input("Ingrese la calificacion: "))

if 80 <= calificacion <= 100:
 print("El alumno obtiene una A ")

elif 70 <= calificacion <= 79:
 print("El alumno obtiene una B ")

elif 60 <= calificacion <=69:
 print("El alumno obtiene una C ")

elif 50 <= calificacion <= 59:
 print("El alumno obtiene una D ")

elif 0 <= calificacion <= 49:
 print("El alumno obtiene una F ")

else:
 print("Puntaje invalido")

 # Ejercicio 2: Detectar estación del año
mes = input("Ingresa el mes: ").strip().lower()
if mes in ['septiembre', 'octubre', 'noviembre']:
    print("La estación es Otoño.")
elif mes in ['diciembre', 'enero', 'febrero']:
    print("La estación es Invierno.")
elif mes in ['marzo', 'abril', 'mayo']:
    print("La estación es Primavera.")
elif mes in ['junio', 'julio', 'agosto']:
    print("La estación es Verano.")
else:
    print("Mes inválido.")

# Ejercicio 3: Verificar fruta en la lista
frutas = ['plátano', 'naranja', 'mango', 'limón']
fruta = input("Ingresa una fruta: ").strip().lower()
if fruta in frutas:
    print("Esa fruta ya está en la lista.")
else:
    frutas.append(fruta)
    print("Fruta agregada. Lista actualizada:", frutas)

       #Nivel 3: Modificacion de lista

persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Espacial',
        'código_postal': '02210'
    }
}

# Verificar si tiene la clave "habilidades"
if 'habilidades' in persona:
    habilidades = persona['habilidades']

# Imprimir la habilidad del medio
medio = len(habilidades) // 2
print("Habilidad del medio:", habilidades[medio])
 # Verificar si tiene Python
tiene_python = 'Python' in habilidades
print("¿Tiene habilidad en Python?", tiene_python)

# Determinar tipo de desarrollador
if habilidades == ['JavaScript', 'React']:
  print("Es un desarrollador frontend.")
elif all(h in habilidades for h in ['Node', 'Python', 'MongoDB']):
  print("Es un desarrollador backend.")
elif all(h in habilidades for h in ['React', 'Node', 'MongoDB']):
  print("Es un desarrollador fullstack.")
else:
  print("Título desconocido.")

# Verificar si está casado y vive en Finlandia
if persona.get('casado') and persona.get('país') == 'Finlandia':
    print(f"{persona['nombre']} {persona['apellido']} vive en Finlandia. Esta casado.")