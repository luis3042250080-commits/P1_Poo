"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares
class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
     self.__marca=marca
     self.__color=color
     self.__modelo=modelo
     self._velocidad=velocidad
     self._potencia=potencia
     self._asientos=asientos

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velociad es: {self.velocidad}")

    def frenar(self):
       self.velocidad-=1
       print(f"Ahora la velocidad es: {self.velocidad}")

coche1=Coches()
coche2=Coches()

print(f"colordel coche 1 es: {coche1.color}")
print(f"colordel coche 2 es: {coche2.color}")


for i in range(10):
    coche1.acelerar()

"""
Crear los metodos setters y getters .- estos metodos son importantes y necesarios 
en todos clases para que el programador interactue con los valores de los atributos 
a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para 
solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en 
particular de la clase a traves de un objeto. 
En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga 
la clase Los metodos get siempre regresan valor es decir el valor de la propiedad a 
traves del return Por otro lado el metodo set siempre recibe parametros para cambiar o 
modificar el valor del atributo o propiedad en cuestion
"""

def getVelocidad(self):
   return self.__velocidad

def setVelocidad(self,velocidad):
   self.__velocidad=velocidad

def getMarca(self):
   return self.__marca

def setVelocidad(self,marca):
   self.__marca=marca

def getColor(self):
   return self.__Color

def setColor(self,color):
   self.__color=color

def getModelo(self):
   return self.__modelo

def setModelo(self,modelo):
   self.__modelo=modelo

def getPotencia(self):
   return self.__potencia

def setPotencia(self,potencia):
   self.__potencia=potencia

def getAsientos(self):
   return self.__velocidad

def setAsientos(self,asientos):
   self.__asientos=asientos

   