columnas = input("indique columnas")
columnas =int(columnas)
filas = input("indique filas")
filas =int(filas)
j=0
i=0
for i in range(filas):
    for j in range(columnas):
        print("+----",end="")
    print("+")
    for j in range(columnas):
        print("|    ",end="")
    print("|")
for j in range(columnas):
    print("+----",end="")
print("+")
