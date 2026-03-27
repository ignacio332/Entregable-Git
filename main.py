import random
opciones = ["piedra","papel","tijera","lagarto","spock"]
jugador = input("Eliga una de las opciones: ")
pc = random.choice(opciones)
if jugador not in opciones:
    print("Opción inválida")
else:
    #aca van todos los elif
    if jugador == pc:
        print("Empate")
    elif jugador == "tijera" and pc in ["papel","lagarto"]:
        print("ganaste")
    elif jugador == "papel" and pc in ["piedra","spock"]:
        print("ganaste")
    elif jugador == "piedra" and pc in ["lagarto","tijera"]:
        print("ganaste")
    elif jugador == "lagarto" and pc in ["spock","papel"]:
        print("ganaste")
    elif jugador == "spock" and pc in ["tijera","piedra"]:
        print("ganaste")
    else:
        print("PC eligio", pc)
        print("perdiste")