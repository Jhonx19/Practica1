from datetime import datetime
import random

class Cronometro:
    def __init__(self):
        self._inicia = datetime.now()
        self._finaliza = None

    def get_inicia(self):
        return self._inicia

    def get_finaliza(self):
        return self._finaliza

    def inicia(self):
        self._inicia = datetime.now()
        self._finaliza = None

    def detener(self):
        self._finaliza = datetime.now()

    def lapso_milisegundos(self):
        if self._finaliza is None:
            diferencia = datetime.now() - self._inicia
        else:
            diferencia = self._finaliza - self._inicia
        return diferencia.total_seconds() * 1000

    def lapso_segundos(self):
        return self.lapso_milisegundos() / 1000

# PROGRAMA PRINCIPAL
if __name__ == "__main__":


    cronometro = Cronometro()

    print("\n1) Hora al crear el objeto:")
    print("   ", cronometro.get_inicia().strftime("%d/%m/%Y %H:%M:%S"))
    print("   Finaliza inicialmente:", cronometro.get_finaliza())

    # Generar
    cantidad = 100000
    print(f"\n2) Generando {cantidad} números aleatorios...")
    numeros = [random.randint(0, 1000000) for _ in range(cantidad)]

    print("   Primeros 10 números generados:")
    print("   ", numeros[:10])

    # Reiniciar crono
    cronometro.inicia()
    print("\n3) Cronómetro reiniciado a las:")
    print("   ", cronometro.get_inicia().strftime("%d/%m/%Y %H:%M:%S"))

    print("\n4) Ordenando los 100,000 números con sort()...")
    numeros.sort()

    # Detener crono
    cronometro.detener()

    print("\n5) Hora final:")
    print("   ", cronometro.get_finaliza().strftime("%d/%m/%Y %H:%M:%S"))

    print("\n6) Tiempo transcurrido:")
    print(f"   Milisegundos: {cronometro.lapso_milisegundos():.2f} ms")
    print(f"   Segundos: {cronometro.lapso_segundos():.4f} s")

    print("\n7) Verificación del ordenamiento:")
    print("   Primeros 10 números ordenados:")
    print("   ", numeros[:10])

    print("\n")