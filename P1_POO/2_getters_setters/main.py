from coches import Coches

coche1=Coches
coche2=Coches("Nisan","azul",)

coche1.acelerar()
coche2.acelerar()

print(coche1.__velocidad)

#coche1.__velocidad=400
coche1.setVelociad(400)
#print(coche1.__velocidad)
print(coche1.getVelocidad)