class EcuacionLineal:
    # Constructor
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # MétodO
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    # Método X
    def getX(self):
        det = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / det

    # Método Y
    def getY(self):
        det = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / det


print("Sistema de ecuaciones 2x2")
print("ax + by = e")
print("cx + dy = f")

# datos
a, b, c, d, e, f = map(float, input("Ingrese a, b, c, d, e, f: ").split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

# Mostrar resultado
if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")