import random
opciones = ["piedra","papel","tijera","lagarto","spock"]
jugador = input("Eliga una de las opciones")
pc = random.choice(opciones)
if jugador not in opciones:
    print("Opción inválida")
else:
    if jugador == pc:
        print("Empate")
    elif jugador == "tijera" and pc in ["papel","lagarto"]:
        print("ganaste")
    #aca van todos los elif
    else:
        print("pc eligio", pc)
        print("perdiste")