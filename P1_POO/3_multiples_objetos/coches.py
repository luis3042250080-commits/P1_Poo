"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    marca=""
    color="Blanco"
    modelo=""
    velocidad=100
    potencia=0
    asientos=0

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velociad es: {self.velocidad}")
    
    def fenar(self):
        self.velocidad-=1
        print(f"Ahora la velociad es: {self.velocidad}")

#Multiples objetos
coche1=Coches()
coche2=Coches()

print(f"color del coche 1 es: {coche1.color}")
print(f"color del coche 2 es: {coche2.color}")

#coche1.acelerar()
#coche1.acelerar()
#print(f"La velocidad del coche 1 ahora es: {coche1.acelerar}")

for i in range(10):
    coche1.acelerar()
    