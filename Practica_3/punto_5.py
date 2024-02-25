import numpy as np

class Circulo:
    def __init__(self,cx,cy,r):
        self.cx = cx 
        self.cy = cy
        self.radio = r
    
    def area(self):
        area = np.pi*(self.radio**2)
        print("El area de su circulo es", area)
    def perimetro(self):
        perimetro = 2*np.pi*self.radio
        print("El perimetro de su circulo es", perimetro)
    def pertenece(self):
        x = float(input("Ingrese la coordenada X del punto "))
        y = float(input("Ingrese la coordenada Y del punto "))
        distancia =((x - self.cx)**2+(y-self.cy)**2)**0.5
        if (distancia>self.radio):
            print("El punto ingresa esta por fuera de la circuferencia")
        else:
            print("El punto pertenece a la circuferencia")


c1 = Circulo(1,3,3)
c1.area()
c1.perimetro()
c1.pertenece()