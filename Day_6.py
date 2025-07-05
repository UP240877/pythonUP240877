#1.Declarar una tupla
tupla_vacia = ()

#2.Tupla con los nombres de hermano/a
hermano=("Angel","Erick")
hermana=("Karen",)

#3.Unir las tuplas
hermano_y_hermana= hermano + hermana

#4.Pregunta
cantidad=(len(hermano_y_hermana))
print("¿Cuantos hermanos tienes?")
print(cantidad)

#5.Agregar padres
miembros_familia=hermano_y_hermana + ("Juan", "Guillermina")
print(miembros_familia)

#Ejercicios Nivel 2

#1.Desempaquetar 

Karen, Angel, Erick, Juan, Guillermina = miembros_familia

#2.Crear tupla´s
fruta=("manzana","platano","guayaba")
verdura=("papa","brocoli","cebolla")
productos_animales=("carne","queso","leche")

alimentos_tp = fruta + verdura + productos_animales

print(alimentos_tp)

#3.Conversion de tupla a lista
alimentos_lista=list(alimentos_tp)

#4.Elemento de en medio
print(alimentos_tp[len(alimentos_tp)//2])

#5.Los primeros y ultimos 3
print(alimentos_tp[:3])
print(alimentos_tp[-3:])

#6.Eliminar la tupla
del alimentos_tp

#7.Verificar si existe dentro de la tupla
paises_nordicos=["Denmark","Finland","Iceland","Norway","Sweden"]
print("Estonia" in paises_nordicos)
print("Iceland" in paises_nordicos)


