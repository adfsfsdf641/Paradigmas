#se evalua la puntuacion de las manos
def calcular_puntuacion(mano):
    puntuacion = sum(mano)

    # Ajustar As de 11 a 1 si es necesario
    while puntuacion > 21 and 11 in mano:
        mano[mano.index(11)] = 1
        puntuacion = sum(mano)

    return puntuacion

# esta funcion evalua cual de las dos manos gano si la del dealer o la del jugador
def determinar_ganador(p_jugador, p_dealer):
    if p_dealer > 21:
        return "El dealer se pasó. ¡Ganaste!"
    elif p_jugador > 21:
        return "Te pasaste. Perdiste."
    elif p_jugador > p_dealer:
        return "¡Ganaste!"
    elif p_jugador < p_dealer:
        return "Perdiste."
    else:
        return "Empate."