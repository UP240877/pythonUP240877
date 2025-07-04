#1. Declarar lista vacia
listavacia=[]

#2.Declarar una lista con mas de 5 elementos
objetos=("Telefono","Manzana","Libreta","Tv","Lapiz","Zapato","Control")

#3.Encontar la longitud de la cadena
print(len(objetos))

#4.Primer, Medio y Ultimo de la cadena
print(objetos[0],objetos[len(objetos)//2], objetos[-1])

#5.Declarar lista "mixed_data_types"
mixed_data_types=["Carlos","20 años","165 cm","Soltero","Infonavit Morelos"]

#6.Declarar lista "it_companies"
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#7.Imprimir las cadenas
print(mixed_data_types)
print(it_companies)

#8.Numero de compañias
print(len(it_companies))

#9.Primera, Medio y ultimo de las cadenas
print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])

#10.Lista modificada
it_companies[0]="Instagram"
print(it_companies)

#11.Agregar compañias a la lista
it_companies.append("Intel")
print(it_companies)

#12.Insertar compañia
it_companies.insert(len(it_companies)//2, "Ryzer")
print(it_companies)

#13.Cambiar nombre
it_companies.remove("Instagram")
it_companies.insert(0,"INSTAGRAM")
print(it_companies)

#14.Unir elementos de la lista
print("#".join(it_companies))

#15.Verificacion de datos
print("Apple" in it_companies)

#16.Ordenar lista con el uso de "sort()"
it_companies.sort()
print(it_companies)

#17.Invertir el orden
it_companies.reverse()
print(it_companies)

#18.Las primeras 3 companias
print(it_companies[:3])

#19.Las ultimas 3 compañias
print(it_companies[-3:])

#20.Las compañias de en medio
print(it_companies[len(it_companies)//2])

#21.Eliminar la primera compañia
it_companies.pop(0)
print(it_companies)

#22.ELiminar la compañia de en medio
medio=len(it_companies)//2
eliminar=it_companies.pop(medio)
print(it_companies)

#23.Eliminar la ultima compañia
elim_ulti=it_companies.pop(-1)
print(it_companies)

#24.Eliminar todas las compañias
print(it_companies.clear())

#25.Destruye la lista
del it_companies

#26.Une las siguientes listas
front_end=["HTML","CSS","JS","React","Redux"]
back_end=["Node","Express","MongoDB"]
print(front_end+back_end)

#27.Agregar a la lista
full_stack=front_end+back_end
despues_de= full_stack.index("Redux")
full_stack.insert(despues_de+1,"Python")
full_stack.insert(despues_de+2,"SQL")
print(full_stack)