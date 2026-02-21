#se importa la bibliotaca random para crear una baraja aleatoria
import random
#creacion de la funcion de la baraja aleatoria
def crear_baraja():
    valores = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    baraja = valores * 4
    #usamos la funcion shuffle para aleatorizar los valores de la baraja
    random.shuffle(baraja)
    return baraja
# Función que recibe la baraja (lista de cartas), 
# saca la última carta usando pop() y la devuelve.
# pop() elimina la carta de la lista para evitar que se repita.
def repartir_carta(baraja):
    return baraja.pop()