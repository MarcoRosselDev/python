class CuentaBancaria:
    """ funcionalidad importante:
    * retirar
    * depositar
    * generar balance
    * actualizar datos
     """
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)        

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

mi_cuenta = CuentaBancaria("105-356-645", "Nora sSmith", 5600)
#print(mi_cuenta.balance) # 5600

mi_cuenta.depositar(1000)
mi_cuenta.depositar(1000)
mi_cuenta.depositar(1000)
mi_cuenta.depositar(1000)
mi_cuenta.depositar(1000)
mi_cuenta.generar_balance()