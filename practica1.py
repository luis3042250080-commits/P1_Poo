"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado

def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 3))

#Implementar el paradigma Orientado a Objetos (OO)

class Rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rect = Rectangulo(5, 3)
print(rect.area())


class Rectangular:
    def are(self,base,altura):
        areaR=base*altura
        return areaR


Rectangulo1=Rectangulos() #Crear o intanciar un objeto "rectangulao1" de la clase "Recatngulos"
print(f"El area del rectangulo es: {rectangulo1.area(5,6)}")