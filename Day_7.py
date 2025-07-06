#Datos para el ejercicio
it_companies={"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
edad={22,19,24,25,26,24,25,24}

#1.Encontrar la longitud
print(len(it_companies))

#2.Agregar "Twitter" 
it_companies.add("Twitter") #El "add" sirve para subir una variable a la cadena
print(it_companies)

#3.Insertar multiples variables
it_companies.update(["Instagram","Temu"]) #El updatte sirve para subir multiples variables a la cadena
print(it_companies)

#4.Eliminar una de las variables
it_companies.remove("Temu")
print(it_companies)

#Nivel 2 

#1.Unir los conjuntos A y B
union=A.union(B)
print(union)

#2.Encontrar la interseccion entre A y B
interseccion=A.intersection(B) 
print(interseccion)  #El comando "intersection" sirve para obtener la interseccion de dos cadenas

#3.¿A es un subconjunto de B?
print("¿A es un subconjunto de B?")
print(A.issubset(B))   #El comando "issubset" sirve para determinar si una cadena es subconjunto de otra cadena

#4.¿Son A y B conjuntos distintos?
print("¿Son A y B conjuntos distintos?")
print(A.isdisjoint(B)) #El comando "isdisjoint" sirv para determinar si dos cadenas son #disjuntos" entre si

#5.Une A con B y B con A
primera_union=A.union(B)
segunda_union=B.union(A)
print("Union de A con B", primera_union)
print("Union de B con A", segunda_union)

#6.Diferencia simetrica
simetria=A.symmetric_difference(B)
print("Diferencia simetrica:",simetria)

#7.Elimar los conjuntos
del A
del B

#Tercer nivel

#1.Convertir edades a un conjunto y comparar la longitud de la lista con del conjunto, ¿Cual es mas grande?
edad_conjunto=set(edad)
primer_longitud=len(edad)
segunda_longitud=len(edad_conjunto)
comparacion=primer_longitud>segunda_longitud
print("¿La lista es mas grande que el conjunto?",comparacion)

# 2. Explica la diferencia entre tipos de datos "string", "list", "tuple" y "set"
print("El string es una cadena de texto, por ejemplo: 'Hola mundo'. Se usa para almacenar palabras o frases.")
print("La list es una colección ordenada y modificable de elementos, como: [1, 2, 3]. Puede contener duplicados.")
print("El tuple es como una lista, pero inmutable (no se puede cambiar una vez creada). Ejemplo: (1, 2, 3).")
print("El set es una colección desordenada de elementos únicos. Se usa para eliminar duplicados. Ejemplo: {1, 2, 3}.")

#3.Palabras unicas dentro de la oracion

oracion="I am a teacher and I love to inspire and teach people"
palabra=oracion.split()
palabra_unica=set(palabra)
print(palabra_unica)
print(len(palabra_unica))