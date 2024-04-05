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