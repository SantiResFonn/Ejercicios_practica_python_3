class Rectangulo:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def area(self):
        lado1 = ((self.x1 - self.x1)**2+(self.y2-self.y1)**2)**0.5
        lado2 = ((self.x2 - self.x1)**2+(self.y1-self.y1)**2)**0.5
        area = (lado1*lado2)
        print("El area de su rectangulo es", area)
    def perimetro(self):
        lado1 = ((self.x1 - self.x1)**2+(self.y2-self.y1)**2)**0.5
        lado2 = ((self.x2 - self.x1)**2+(self.y1-self.y1)**2)**0.5
        perimetro = (lado1+lado2+lado1+lado2)
        print("El perimetro de su rectangulo es", perimetro)
    def cuadrado(self):
        lado1 = ((self.x1 - self.x1)**2+(self.y2-self.y1)**2)**0.5
        lado2 = ((self.x2 - self.x1)**2+(self.y1-self.y1)**2)**0.5
        if(lado1 == lado2):
            print("Los puntos forman un cuadrado")
        else:
            print("Los puntos no forman un cuadrado")


r1 = Rectangulo(1,8,5,3)
r1.area()
r1.perimetro()
r1.cuadrado()