class Punto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def coordenadas(self):
        print("La coordenada en x es", self.x, "y la coordenada en y es", self.y)

    def cambio(self):
        cambio = input("¿Quiere cambiar la coordenada x o y? ")
        if (cambio == "x"):
            self.x = float(input("Ingrese el valor de la nueva coordenada x "))
            print("La nueva coordenada en x es", self.x, "y la coordenada en y es", self.y)
        else:
            self.y = float(input("Ingrese el valor de la nueva coordenada y "))
            print("La coordenada en x es", self.x, "y la nueva coordenada en y es", self.y)
    def calcular_distancia(self):
        x2 = float(input("Ingrese la coordenada X del punto 2 "))
        y2 = float(input("Ingrese la coordenada Y del punto 2 "))
        d = (((x2-self.x)**2)+((y2-self.y)**2))**0.5
        print("La distancia entre ambos puntos es ", d)




p1 = Punto(1, 2)
p1.coordenadas()
p1.calcular_distancia()