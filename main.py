import random
opciones = ["piedra","papel","tijera","lagarto","spock"]
print("Opciones: piedra,papel,tijera,lagarto,spock")
jugador = input("Eliga una de las opciones: ")
pc = random.choice(opciones)
if jugador not in opciones:
    print("Opción inválida")
else:
    #aca van todos los elif
    if jugador == pc:
        print("Empate, los dos tiraron: "+pc)
    elif jugador == "tijera" and pc in ["papel","lagarto"]:
        print("ganaste, tijera le gana a "+pc)
    elif jugador == "papel" and pc in ["piedra","spock"]:
        print("ganaste, papel le gana a "+pc)
    elif jugador == "piedra" and pc in ["lagarto","tijera"]:
        print("ganaste,  piedra le gana a "+pc)
    elif jugador == "lagarto" and pc in ["spock","papel"]:
        print("ganaste,  lagarto le gana a "+pc)
    elif jugador == "spock" and pc in ["tijera","piedra"]:
        print("ganaste,  spock le gana a "+pc)
    else:
        print("PC eligio", pc)
        print("perdiste")
print("Vuelve a jugar!")
