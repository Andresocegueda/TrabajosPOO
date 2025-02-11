class CuentaBancaria:
    def __init__(self, nombre_titular, saldo_inicial):
        self._titular = nombre_titular
        self._saldo = saldo_inicial
        self.__historial = []

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo...")

    def __actualizar_historial(self, transaccion):
        self.__historial.append(transaccion)

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            self.__actualizar_historial(f"Depósito de {cantidad}")
            print(f"Deposito exitoso... Su saldo actual es de {self._saldo}")
        else:
            print(f"Error: La cantidad debe ser mayor que 0.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            self.__actualizar_historial(f"Retiro de {cantidad}")
            print(f"Retiro exitoso... Su saldo actual es de {self._saldo}")
        else:
            print("Error: Fondos insuficientes o cantidad invalida.")

    def obtener_historial(self):
        return self.__historial
        
    def mostrar_info(self):
        return f"""Titular: {self._titular}
Saldo: {self._saldo}"""
    
    def obtener_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Juan Perez", 1000)
print(cuenta.mostrar_info())
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.retirar(1500)
print(f"Saldo final: {cuenta.obtener_saldo()}")
cuenta.saldo = -100
print(f"Historial de transacciones: {cuenta.obtener_historial()}")