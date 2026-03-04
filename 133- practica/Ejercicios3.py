import math

class EcuacionLineal:
    # Constructor
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c


    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b + math.sqrt(d)) / (2*self.__a)
        else:
            return 0

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b - math.sqrt(d)) / (2*self.__a)
        else:
            return 0

def main():
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    c = float(input("Ingrese c: "))

    ecuacion = EcuacionLineal(a, b, c)
    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        print("La ecuación tiene dos raíces", 
              round(ecuacion.getRaiz1(), 5), "y", 
              round(ecuacion.getRaiz2(), 5))
    elif discriminante == 0:
        print("La ecuación tiene una raíz", 
              round(ecuacion.getRaiz1(), 5))
    else:
        print("La ecuación no tiene raíces reales")


if __name__ == "__main__":
    main()