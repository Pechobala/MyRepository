import random
import itertools

class TexasHoldem:

    PALO = ["CORAZONES", "PICAS", "TREBOLES", "DIAMANTES"]
    NUMERO = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    NPLAYERS = 3
    TAMANOMESA = 3
    TAMANOMANO = 2
    RANKING = ["Escalera Real", "Escalera Color", "Poker", "Full", "Color", "Escalera", "Trio", "Doble Pareja", "Pareja", "Carta Alta"]
    manos = [[],[],[]]
    mesa = []
    desempate = [0, 0, 0]

    baraja = [f"{numero} de {palo}" for numero, palo in itertools.product(NUMERO, PALO)]

    baraja = random.sample(baraja, len(baraja)) #random.sample baraja al azar una lista de elementos
    print(baraja)

    #repartir jugadores
    for i in range(TAMANOMANO):
        for j in range(NPLAYERS):
            manos[j].append(baraja[0])
            baraja.pop(0)

    print(manos)

    #repartir mesa
    for i in range(TAMANOMESA):
        mesa.append(baraja[0])
        baraja.pop(0)

    print(mesa)
    puntuacion = [0, 0, 0]
    #CALCULAMOS GANADOR
    for i in range(NPLAYERS):
        print(f"El jugador {i} tiene {manos[i]} y en la mesa hay {mesa}")
        manototal = manos[i] + mesa
        nrepetidos = [0 for _ in NUMERO]
        for carta in manototal:
            for numero in range(len(nrepetidos)):
                if carta[0] == NUMERO[numero][0]:
                    nrepetidos[numero] += 1

        if any(repetido == 4 for repetido in nrepetidos):
            numero = [j for j, repetido in enumerate(nrepetidos) if repetido == 4]
            print(f"El jugador {i} tiene un Poker de {NUMERO[numero[0]]}s")

            puntuacion[i] = [j for j, poker in enumerate(RANKING) if poker == "Poker"][0]
        elif any(repetido == 3 for repetido in nrepetidos):
                    numerotrio = [j for j, repetido in enumerate(nrepetidos) if repetido == 3]
                    numeropareja = [j for j, repetido in enumerate(nrepetidos) if repetido == 2]
                    if len(numeropareja) > 0:
                        print(f"El jugador {i} tiene un Full de {NUMERO[numerotrio[0]]}s y de {NUMERO[numeropareja[0]]}s")
                        puntuacion[i] = [j for j, full in enumerate(RANKING) if full == "Full"][0]
                    else:    
                        print(f"El jugador {i} tiene un Trio de {NUMERO[numerotrio[0]]}s")
        
                        puntuacion[i] = [j for j, trio in enumerate(RANKING) if trio == "Trio"][0]
        elif any(repetido == 2 for repetido in nrepetidos):
            numero = [j for j, repetido in enumerate(nrepetidos) if repetido == 2]
            if len(numero) > 1:
                print(f"El jugador {i} tiene una Doble Pareja de {NUMERO[numero[0]]}s y de {NUMERO[numero[1]]}s")
                puntuacion[i] = [j for j, dpareja in enumerate(RANKING) if dpareja == "Doble Pareja"][0]
            else:    
                print(f"El jugador {i} tiene una Pareja de {NUMERO[numero[0]]}s")

                puntuacion[i] = [j for j, pareja in enumerate(RANKING) if pareja == "Pareja"][0]
        else:
            palosrepetidos = [0, 0, 0, 0]
            color = ""
            for carta in manototal:
                for palo in range(len(palosrepetidos)):
                    if PALO[palo] in carta:
                        palosrepetidos[palo] += 1    
                        if palosrepetidos[palo] == 5:
                            color = PALO[palo]

            numero = []
            for numerin in manototal:
                match numerin[0]:
                    case '1':
                        numero.append(10)
                    case 'J':
                        numero.append(11)
                    case 'Q':
                        numero.append(12)
                    case 'K':
                        numero.append(13)
                    case 'A':
                        numero.append(14)
                    case _:    
                        numero.append(int(numerin[0]))

            desempate[i] = numero[0] + numero[1]
            numero.sort()
            escalera = 0
            #Calculamos escalera
            listaampliada = numero + numero
            for k in range(len(listaampliada)-1):
                if (listaampliada[k]+1) == listaampliada[k+1] or (listaampliada[k] == 14 and listaampliada[k+1] == 2):
                    escalera += 1
                else:
                    escalera = 0
                if escalera == 4:
                    k = 0
                    break
            if color and escalera:
                if 10 in numero and 14 in numero:
                    print(f"El jugador {i} tiene una Escalera Real")
                    puntuacion[i] = [j for j, escalerar in enumerate(RANKING) if escalerar == "Escalera Real"][0]
                else:
                    print(f"El jugador {i} tiene una Escalera de Color")
                    puntuacion[i] = [j for j, escalerac in enumerate(RANKING) if escalerac == "Escalera Color"][0]
            elif color:
                print(f"El jugador {i} tiene Color de {color}s")                
                puntuacion[i] = [j for j, colori in enumerate(RANKING) if colori == "Color"][0]
            elif escalera:
                print(f"El jugador {i} tiene una Escalera")
                puntuacion[i] = [j for j, escalerita in enumerate(RANKING) if escalerita == "Escalera"][0]
            else:
                print(f"El jugador {i} tiene una Carta Alta de {max(numero)}s")
                puntuacion[i] = [j for j, alta in enumerate(RANKING) if alta == "Carta Alta"][0]

        #Calculamos el ganador
        minimo = min(puntuacion)
        empate = puntuacion.count(minimo)
        ganador = -1
        final = 100
        if empate > 1:
            for j in range(len(manos)):
                if puntuacion[j] == minimo and desempate[j] < final:
                    ganador = j
                    final = desempate[j]
        else:
            ganador = puntuacion.index(minimo)
        print(puntuacion)
        print(f"El ganador es el jugador {ganador}")