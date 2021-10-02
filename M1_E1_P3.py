""""**********************************
Autor       : Bristela Muñoz Burgos
Carrera     : Ingeniería en Informática
Ramo        : Programación Básica
Modulo      : M1-E1
Ejercicio 3 : . Supón que un ramo tiene las siguientes evaluaciones:
3 tareas en Laboratorio, estas valen un 15% del curso,
3 tareas en clase, que valen un 15% del curso, y
2 notas de solemnes, cada una un 35%
Elabora un programa que, ingresando todas las notas, entregue la nota de presentación.
**********************************
"""


#input
lab1=input("ingrese nota lab1:")
lab1= float(lab1)
print("la nota es:", lab1)
lab2=input("ingrese nota lab2:")
lab2= float(lab2)
print("la nota es:", lab2)
lab3=input("ingrese nota lab3:")
lab3= float(lab3)
print("la nota es:", lab3)

nt1=input("ingrese nota nt1:")
nt1= float(nt1)
print(nt1)
nt2=input("ingrese nota nt2:")
nt2= float(nt2)
print(nt2)
nt3=input("ingrese nota nt3:")
nt3= float(nt3)
print(nt3)

nsol_1=input("ingrese nota nsol_1")
nsol_1= float(nsol_1)
print (nsol_1)
nsol_2=input("ingrese nota nsol_2")
nsol_2= float(nsol_2)
print (nsol_2)

#promedios

promedio_lab= (lab1+lab2+lab3)/3
print( "el promedio es:", promedio_lab)

promedio_nt= (nt1+nt2+nt3)/3
print("el promedio es:", promedio_nt)

promedio_nsol= (nsol_1+nsol_2)/2
print("el promedio es:", promedio_nsol)

# nota presentación
nota_presentación= (promedio_lab*0.15)+ (promedio_nt*0.15)+(promedio_nsol*0.7)
print("la nota de presentación es:" , nota_presentación)

