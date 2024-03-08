"""
import math
cateto_oposto = float(0)
cateto_adjcente = float(input("Coloque aqui o valor do cateto adjcente (a) \n"))
hipotenusa = float(input("Coloque aqui o valor da hipotenusa (c) \n"))
cateto_oposto = (math.sqrt(math.pow(cateto_adjcente,2) - math.pow(hipotenusa,2)  ) )
seno = (cateto_oposto/hipotenusa)
cosseno = (cateto_adjcente/hipotenusa)
tangente = (cateto_oposto/cateto_adjcente)
print("cateto oposto = " + str(cateto_oposto))
print("seno = " + str(cateto_oposto/hipotenusa))
print("cosseno = " + str(cateto_adjcente/hipotenusa))
print("tangente = " + str(cateto_oposto/cateto_adjcente))



"""
hipotenusa = float(input("Digite o valor da hipotenusa"))
cateto_adjcente = float(input("Digite o valir do cateto adjacente"))

cateto_oposto = (hipotenusa**2 - cateto_adjcente**2) ** 0.5
print("O valor do cateto oposto é: ", cateto_oposto)

seno = (cateto_oposto/hipotenusa)
cosseno = (cateto_adjcente/hipotenusa)
tangente = (cateto_oposto/cateto_adjcente)
print("seno = " + str(cateto_oposto/hipotenusa))
print("cosseno = " + str(cateto_adjcente/hipotenusa))
print("tangente = " + str(cateto_oposto/cateto_adjcente))
