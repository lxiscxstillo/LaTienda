from Producto import Producto

class Tienda:

    '''-------------------------------------------------------------------------------------------------
    # Metodos
    -------------------------------------------------------------------------------------------------'''
    # constructor
    def __init__(self):
        self.__producto1 = Producto("PAPELERIA", "lapiz", 500, 30, 9)
        self.__producto2 = Producto("PAPELERIA", "borrador", 300, 15, 5)
        self.__producto3 = Producto("SUPERMERCADO", "cafe", 5600, 20, 10)
        self.__producto4 = Producto("DROGUERIA", "desinfectante", 3200, 12, 11)
        self.__dineroEnCaja = 0.0


    def getProducto1(self):
        return self.__producto1
    
    def getProducto2(self):
        return self.__producto2
    
    def getProducto3(self):
        return self.__producto3
    
    def getProducto4(self):
        return self.__producto4
    
    def getDineroEnCaja(self):
        return self.__dineroEnCaja