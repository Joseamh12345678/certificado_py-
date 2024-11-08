#como imprimir
print ("hola mundo")
#identacion
if condition:
    instruccio1
    instruccion2
else:
    instruccion3
    instruccion4
#comentarios

#este es un comentario
"""
comentario de varias lineas
"""

#python distingue entre mayusculas y minusculas por lo tanto variable, Variable, VARIABLE
# a diferencia de otros lenguajes se puede usar en la misma linea de codigo para las instrucciones solo se separa con ;
# parentecis se usan para agrupar extenciones  
resultado = (a + b) * c

# timestap es para fecha actual
#operadores logicos
a=8
b=3
resultado_and = (a > 5) and (b < 5) #true
resultado_or = (a > 15) or (b > 5) #true
resultado_not = not (a > 5) #false

#condicionales
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
#elif es para verificar conciciones una por una

#for es un ciclo
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

contador = 5

while contador < 5:
    print(contador)
    contador += 1

print("Termino el bucle")

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

for i in range (10):
    if i % 2 == 0:
        continue
    print(i)

frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

numeros = [1, 2, 3, 4, 5]
#1. definimos x de a corde al la posicion del arreglo numerico
#2. elevar al cuadrado
#3. revisar el residuo
#4. si la condicion se cumple, x se agrega al arreglo
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16] 