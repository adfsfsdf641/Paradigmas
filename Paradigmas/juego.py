from baraja import crear_baraja, repartir_carta
from logica import calcular_puntuacion, determinar_ganador


def mostrar_manos(jugador, dealer, mostrar_dealer=False):
    # Esta función muestra en pantalla las cartas
    # del jugador y del dealer.

    # Siempre se muestra la mano completa del jugador
    print("\nTu mano:", jugador, "Puntuación:", calcular_puntuacion(jugador))
    # Si mostrar_dealer es True, se muestra todo
    # Si es False, solo se muestra la primera carta
    if mostrar_dealer:
        print("Mano del dealer:", dealer, "Puntuación:", calcular_puntuacion(dealer))
    else:
        print("Mano del dealer:", [dealer[0], "?"])


def jugar():
    # Crear y mezclar la baraja
    baraja = crear_baraja()
    jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    dealer = [repartir_carta(baraja), repartir_carta(baraja)]

    turno_jugador = True

    # Turno del jugador
    while turno_jugador:
        mostrar_manos(jugador, dealer)

        if calcular_puntuacion(jugador) == 21:
            print("¡Blackjack!")
            break

        opcion = input("¿Pedir carta (p) o plantarse (s)? ").lower()

        if opcion == "p":
            jugador.append(repartir_carta(baraja))
            if calcular_puntuacion(jugador) > 21:
                turno_jugador = False
        elif opcion == "s":
            turno_jugador = False

    # Turno del dealer
    while calcular_puntuacion(dealer) < 17:
        dealer.append(repartir_carta(baraja))

    # Resultado final
    mostrar_manos(jugador, dealer, True)

    p_jugador = calcular_puntuacion(jugador)
    p_dealer = calcular_puntuacion(dealer)

    print("\nResultado:", determinar_ganador(p_jugador, p_dealer))