class CuentaBancaria:
    def __init__(self,numero_cuenta, propietario, balance):
        self.cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self):
        deposito = float(input("Ingrese el valor a depositar: "))
        self.balance = self.balance + deposito
        print("El valor de su cuenta ahora es:", self.balance)
    def retirar(self):
        retiro = float(input("Ingrese el valor a retirar: "))
        if (self.balance==0):
            ("No tiene dinero en su cuenta para retirar")
        elif ((self.balance-retiro)<0):
            ("Esa cantidad no esta disponible en su cuenta bancaria")
        else:
            self.balance = self.balance - retiro
            print("Retiro exitoso, valor actual en su cuenta:", self.balance)            
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance = self.balance - cuota
        print("A su cuenta se le aplicara una cuota de manejo de", cuota,"El nuevo valor disponible:",self.balance)
    def mostrar_detalles(self):
        print("El numero de la cuenta es:", self.cuenta,"propietario de la cuenta:",self.propietario,"saldo disponible en la cuenta:",self.balance)


cb1 = CuentaBancaria(12345,"Gabriel",0)
cb1.depositar()
cb1.retirar()
cb1.aplicar_cuota_manejo()
cb1.mostrar_detalles()