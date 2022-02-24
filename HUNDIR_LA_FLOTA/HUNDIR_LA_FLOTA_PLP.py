import numpy as np
import random
import time
import pygame

pygame.init()
pygame.mixer.init()
sonido_juego = pygame.mixer.Sound("BSO.wav")
sonido_disparo = pygame.mixer.Sound("DISPARO.wav")
sonido_agua = pygame.mixer.Sound("AGUA.wav")
sonido_victoria = pygame.mixer.Sound("VICTORIA.wav")


def bienvenida(nombre_jugador):
    print("BIENVENIDO AL JUEGO, ",nombre_jugador,"!!!","\n", "En este juego jugarás a hundir la flota de Jack Sparrow, pero cuidado porque él tambien querrá hundir la tuya")
    print("EL QUE PRIMERO HUNDA LA FLOTA DEL RIVAL SE HARÁ CON EL BOTÍN","\n",
    "A continuacion podrás ver la colocacion de tus barcos","\n","TU EMPIEZAS DISPARANDO","\n","SUERTE")
    return nombre_jugador
    
nombre_usuario = bienvenida(input("Introduzca su nombre:"))

class Tablero:

    def __init__(self,nombre):
        self.nombre = nombre

    def tablero_maquina(self):
        tablero_maquina1 = np.full((11,11),'_')
        return tablero_maquina1

    def tablero_jugador (self):
        tablero_jugador1 = np.full((11,11),'_')
        return tablero_jugador1

    def tablero_oculto (self):
        tablero_jugador1 = np.full((11,11),'_')
        return tablero_jugador1   



terminator_tablero = Tablero("JackSparrow")
nom_jugador_tablero = Tablero(nombre_usuario)
terminator_tablero_oc = Tablero("JackSparrowOculto")

tablero_maquina = terminator_tablero.tablero_maquina()
tablero_jugador = nom_jugador_tablero.tablero_jugador()

tablero_maquina_oculto = terminator_tablero_oc.tablero_oculto()
pygame.mixer.Sound.play(sonido_juego)



def posicionar_barcos():

    barcos = [4,3,3,2,2,2,1,1,1,1]       

    # POSICIONAMIENTO BARCOS DEL JUGADOR
    for longitud in barcos:

        direccion = random.choice(["NS", "EO"])
        longitud
        barquito=True

        while barquito:
            random_fila_barco = random.randint(0,9)
            random_columna_barco = random.randint(0,9)


            if direccion == "NS" and random_fila_barco + longitud -1 <= 9 and len(tablero_jugador[np.where(tablero_jugador[ random_fila_barco : random_fila_barco + longitud, random_columna_barco] == "O")]) == 0:
                tablero_jugador[random_fila_barco, random_columna_barco] = "O"
                tablero_jugador[random_fila_barco : random_fila_barco + longitud, random_columna_barco] = "O"
                barquito=False
            elif direccion == "EO" and random_columna_barco + longitud -1 <=9 and len(tablero_jugador[np.where(tablero_jugador[random_fila_barco, random_columna_barco:random_columna_barco+longitud] =="O")]) == 0:
                tablero_jugador[random_fila_barco, random_columna_barco] = "O"
                tablero_jugador[random_fila_barco, random_columna_barco:random_columna_barco+longitud] ="O"
                barquito=False

    time.sleep(1)
    print(tablero_jugador)

    # POSICIONAMIENTO BARCOS DE LA MAQUINA
    for longitud in barcos:

        direccion = random.choice(["NS", "EO"])
    
        barquito=True  

        while barquito:
            random_fila_barco = random.randint(0,9)
            random_columna_barco = random.randint(0,9)


            if direccion == "NS" and random_fila_barco + longitud -1 <= 9 and len(tablero_maquina[np.where(tablero_maquina[ random_fila_barco : random_fila_barco + longitud, random_columna_barco] == "O")]) == 0:
                tablero_maquina[random_fila_barco, random_columna_barco] = "O"
                tablero_maquina[random_fila_barco : random_fila_barco + longitud, random_columna_barco] = "O"
                barquito=False
            elif direccion == "EO" and random_columna_barco + longitud -1 <=9 and len(tablero_maquina[np.where(tablero_maquina[random_fila_barco, random_columna_barco:random_columna_barco+longitud] =="O")]) == 0:
                tablero_maquina[random_fila_barco, random_columna_barco] = "O"
                tablero_maquina[random_fila_barco, random_columna_barco:random_columna_barco+longitud] ="O"
                barquito=False


posicionar_barcos()

lista_de_coordenadas = [(0, 0), (0, 1), (0, 2), (0, 3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9), 
(1, 0), (1, 1), (1, 2), (1, 3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
(2, 0), (2, 1), (2, 2), (2, 3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
(3, 0), (3, 1), (3, 2), (3, 3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
(4, 0), (4, 1), (4, 2), (4, 3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
(5, 0), (5, 1), (5, 2), (5, 3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
(6, 0), (6, 1), (6, 2), (6, 3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
(7, 0), (7, 1), (7, 2), (7, 3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
(8, 0), (8, 1), (8, 2), (8, 3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
(9, 0), (9, 1), (9, 2), (9, 3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9),]  #SON LAS QUE USA LA MAQUINA PARA DISPARAR AL JUGADOR


#DISPARO JUGADOR A MAQUINA
def disparo_jugador_a_maquina():
    fil = int(input("ES TU TURNO.Introduce la fila de la 1 a la 10: "))
    col = int(input("ES TU TURNO.Introduce la columna de la 1 a la 10: "))
    

    h = (fil-1,col-1)
    b = (fil,col)

    time.sleep(1)

    if fil>10 or col >10:
        print("Elige números del 1 al 10 ZOQUETE, pierdes tu turno")
    
    elif tablero_maquina[h] == '_':
        tablero_maquina[h] = 'A'
        tablero_maquina_oculto[h] = 'A'
        pygame.mixer.Sound.play(sonido_agua)
        print("AGUA en la posicion", h)
        print(tablero_maquina_oculto)
        print("Es el turno del capitán Jack Sparrow")
        return "Agua"

    elif tablero_maquina[h] == 'O':
        tablero_maquina[h] = 'X'
        tablero_maquina_oculto[h] = "X"
        pygame.mixer.Sound.play(sonido_disparo)
        #pygame.mixer.Sound.play(sonido_tocado)
        print("TOCADO en la posicion", b)
        print(tablero_maquina_oculto)
        return "Tocado"
    else:
        print ("Ya habías disparado ahí PIERDES TU TURNO, haberlo pensado mejor")


#DISPARO MAQUINA A JUGADOR
def disparo_maquina_a_jugador():
    random_disparo = random.choice(lista_de_coordenadas)
    lista_de_coordenadas.remove(random_disparo)
    
    time.sleep(1)
    if tablero_jugador[random_disparo] == '_':
        tablero_jugador[random_disparo] = 'A'
        pygame.mixer.Sound.play(sonido_agua)
        print("Jack Sparrow ha fallado, AGUA en :" ,random_disparo, "ES TU TURNO")
        print(tablero_jugador)
        return "Agua"
            
    elif tablero_jugador[random_disparo] == 'O':
        tablero_jugador[random_disparo] = 'X'
        pygame.mixer.Sound.play(sonido_disparo)
        #pygame.mixer.Sound.play(sonido_disparo)
        print("Jack Sparrow ha acertado, TOCADO en :", random_disparo)
        print(tablero_jugador)
        return "Tocado"


lista5 = True 
final = False

while final == False:

    while lista5 == True:  # cuando la lista sea True sera mi turno
        pim = disparo_jugador_a_maquina()

        if len(tablero_maquina[np.where(tablero_maquina=="O")]) == 0:
            pygame.mixer.Sound.play(sonido_victoria)
            print("HAS HUNDIDO TODOS LOS BARCOS DEL CAPITÁN JACK SPARROW!!! \n HAS GANADO LA PARTIDA!! ENHORABUENA")
            final = True
            break

        elif pim == "Tocado":
            continue

        else:
            lista5 = False
            continue
    

    time.sleep(2)  
    
    while lista5 == False:   #cuando la lista sea False sera tueno de la maquina
        pam = disparo_maquina_a_jugador()

        if len(tablero_jugador[np.where(tablero_jugador=="O")]) == 0:
            print("HAS PERDIDO LA PARTIDA!! ERES UN LOOSER")
            final = False
            break       

        elif pam == "Tocado":
            continue

        else:
            lista5 = True   #si falla la lista pasara a ser True por lo tanto cambia al turno del usiario
            continue

    time.sleep(2)

print("HASTA PRONTO PIRATA")   