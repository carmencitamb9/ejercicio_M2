""""**********************************
Autor       : Bristela Muñoz Burgos
Carrera     : Ingeniería en Informática
Ramo        : Programación Básica
Modulo      : M1-E1
Ejercicio 4 : Con lo aprendido hasta el momento, realiza un programa que de manera totalmente matemática
(ocupando solo lo visto hasta el momento), muestre el digito verificador de un programa.
digito verificador de un rut con 8 digitos)
**********************************
"""


# paso 1 Se lee el número de derecha a izquierda y este se multiplica con números secuencias desde 2 a 7 y
# después se vuelven a repetir.
#paso 1.a
x= input("ingrese la parte entera de un rut:")
x= int(x)

print(x)
x1 = int(x % 10)
print(x1)

x = x / 10
print(x)
x2 = int(x % 10)
print(x2)

x = x / 10
print(x)
x3 = int(x % 10)
print(x3)

x = x / 10
print(x)
x4 = int(x % 10)
print(x4)

x = x / 10
print(x)
x5 = int(x % 10)
print(x5)

x = x / 10
print(x)
x6 = int(x % 10)
print(x6)

x = x / 10
print(x)
x7 = int(x % 10)
print(x7)

x = x / 10
print(x)
x8 = int(x % 10)
print(x8)
print(x1, x2, x3, x4, x5, x6, x7, x8)

# paso1.b
m1 = x1 * 2
m2 = x2 * 3
m3 = x3 * 4
m4 = x4 * 5
m5 = x5 * 6
m6 = x6 * 7
m7 = x7 * 2
m8 = x8 * 3
print(m1, m2, m3, m4, m5, m6, m7, m8)

# paso 2 (sumar todos los resultados)
suma = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
print(suma)

# paso 3 obtenemos el resto (suma%11)

resto = suma % 11
print(resto)

# paso 4 para obtener dígito restamos  a 11 el resultado anterior (resto)
dígito = 11 - resto
print(dígito)


