class Carta:
    def __init__(self,valor,pinta):
        self.valor = valor
        self.pinta = pinta

    def carta(self):
        if (self.valor==1):
            print("El valor de su carta es As")
        elif(self.valor>1 and self.valor<11):
            print("El valor de su carta es", self.valor)
        elif(self.valor == 11):
            print("El valor de su carta es J -Jota")
        elif(self.valor == 12):
            print("El valor de su carta es Q - Reina")
        elif(self.valor == 13):
            print("El valor de su carta es K - Rey")
        else:
            ("Solo se pueden recibir valores de 1 a 13")
        if (self.pinta == 1):
            print("La pinta de su carta es espadas")
        elif (self.pinta == 2):
            print("La pinta de su carta es corazones")
        elif (self.pinta == 3):
            print("La pinta de su carta es picas")
        elif (self.pinta == 4):
            print("La pinta de su carta es diamantes")
        else:
            print("Introduzca un valor de 1 a 4 para saber la pinta de su carta")

c1 = Carta(13,1)
c1.carta()