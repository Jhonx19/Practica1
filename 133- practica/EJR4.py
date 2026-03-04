import math

def promedio(datos):
    return sum(datos) / len(datos)

def desviacion(datos):
    n = len(datos)
    prom = promedio(datos)
    suma = 0

    for x in datos:
        suma += (x - prom) ** 2

    return math.sqrt(suma / (n - 1))

# Programa
datos = []

print("Ingrese 10 números:")

for i in range(10):
    num = float(input(f"Número {i+1}: "))
    datos.append(num)

prom = promedio(datos)
desv = desviacion(datos)

print(f"El promedio es {prom:.2f}")
print(f"La desviación estándar es {desv:.5f}")