"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches:
    def __init__(self,color,marca,velodicad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velodicad


    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
    def tocar_claxon(self):
        pass

coche1=Coches("Blanco","VW",220)
coche2=Coches("Azul","Nissan"),180

print(f"El color del coche 1 es: {coche1.__color}")


#Instanciar o crear objetos de la clase Coches







