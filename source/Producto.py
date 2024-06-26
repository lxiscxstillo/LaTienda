from enum import Enum

'''-----------------------------------------------------------------------------------------------------------
# Enumeracion
-----------------------------------------------------------------------------------------------------------'''
class Tipo(Enum):
    '''--------------------------------------------------------------------------------------------------------
    # Enumeraciones
    --------------------------------------------------------------------------------------------------------'''
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto:
    __subsudio = True

    calidad = 'A'

    '''----------------------------------------------------------------------------------------------------------------------------------------------------
    # Constantes
    -----------------------------------------------------------------------------------------------------------------------------------------------------'''

    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA= 0.12

    '''----------------------------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------------------------'''
    # Constructor
    def __init__(self, pTipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo = pTipo
        self.__nombre = pNombre
        self.__valorUnitario = pValorUnitario
        self.__cantidadBodega = pCantidadBodega
        self.__cantidadMinima = pCantidadMinima
        self.__cantidadUnidadesVendidas = 0 

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setValorUnitario(self, ValorUnitario):
        self.__valorUnitario = ValorUnitario

    def setCantidadBodega(self, CantidadBodega):
        self.__cantidadBodega = CantidadBodega

    def setCantidadMinima(self, CantidadMinima):
        self.__cantidadMinima = CantidadMinima

    def setCantidadUnidadesVendidas(self, CantidadUnidadesVendidas):
        self.__cantidadUnidadesVendidas = CantidadUnidadesVendidas

    def vender(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
        else:
            print("Cantidad no disponible")

    def haySuficiente(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False
        
    def getIVA(self):
        if self.__tipo == "PAPELERIA":
            return self.__IVA_PAPELERIA
        elif self.__tipo == "FARMACIA":
            return self.__IVA_FARMACIA
        elif self.__tipo == "SUPERMERCADO":
            return self.__IVA_SUPERMERCADO
        else:
            print("Categoria no soportada")
    
    def subirValorUnitario(self):
        if self.__valorUnitario < 1000:
            self.__valorUnitario += self.__valorUnitario * 0.01
        elif self.__valorUnitario == [1000, 5000]:
            self.__valorUnitario += self.__valorUnitario * 0.02
        elif self.__valorUnitario > 5000:
            self.__valorUnitario += self.__valorUnitario * 0.03

    def hacerPedido(self, pCantidad):
        if self.__cantidadBodega <= self.__cantidadMinima:
            self.__cantidadBodega += pCantidad

    def cambiarValorUnitario(self):
        if self.__tipo == "FARMACIA" or self.__tipo == "PAPELERIA":
            self.__valorUnitario -=self.__valorunitario *0.10
        elif self.__tipo == "SUPERMERCADO":
            self.__valorUnitario += self.__valorUnitario * 0.05

    def nombreTipoProducto(self):
        tipo = self.getTipo()
        if tipo == "SUPERMERCADO":
            return "El producto es de supermercado"
        elif tipo == "FARMACIA":
            return "El producto es de farmacia"
        elif tipo == "PAPELERIA":
            return "El producto es de papeleria"
        
    def aumentarValorUnitario(self):
        if self.__tipo == "FARMACIA":
            self.__valorUnitario += self.__valorUnitario * 0.01
        elif self.__tipo == "SUPERMERCADO":
            self.__valorUnitario += self.__valorUnitario * 0.03
        elif self.__tipo == "PAPELERIA":
            self.__valorUnitario += self.__valorUnitario * 0.02