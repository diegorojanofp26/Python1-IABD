import random as rnd

def jocPedraPaperTisores():
  seguir = True
  puntos = 0
  puntosIa = 0
  while seguir == True:
    opcionBot = rnd.randint(1,3)
    if puntos == 3:
      print('Has ganado')
      seguir = False
    elif puntosIa == 3:
      print('Ha ganado la IA')
      seguir = False
    else:
      try:
        userSelect = int(input('Escull una opcio:\n 1. Pedra\n 2. Paper\n 3. Tisores\n 0. Sortir'))
      except ValueError:
        print('No has introducido un valor valido')
      if userSelect == 0:
        break
      match userSelect,opcionBot:
          case (1,1) | (2,2) | (3,3):
            print('Empat')
          case (1,2) | (2,3) | (3,1):
            print("Ha guanyat l'IA")
          case (1,3) | (2,1) | (3,2):
            print('Has guanyat')
            puntos +=1

def jocPenjat():
  palabras = ["sol", "mar", "pan", "casa", "gato", "luna", "soles", "fuego", "libro", "perro","camino", "musica", "jardin", "puerta", "bosque", "planeta", "ventana", "sonrisa", "pintura", "riqueza"]
  adivina = rnd.choice(palabras)
  encontradas = ['-'] * len(adivina)
  print(''.join(encontradas))
  intentos = 2 * len(adivina)
  while intentos > 0:
    try:
      letraUser = input('Que letra quieres?: ').lower().strip()
    except KeyboardInterrupt:
      print('\nPartida cancelada.')
      return

    try:
      if letraUser in adivina:
        for i, letra in enumerate(adivina):
          if letra == letraUser:
            encontradas[i] = letra
      else:
        intentos -= 1
        if intentos == 0:
          print(f'Has perdido. La palabra era: {adivina}')
    except IndexError:
      print(f'Error interno al actualizar la palabra')
      return
    print(''.join(encontradas))
    if '-' not in encontradas:
      print("Has ganado!!!")
      break


# Tres en raya #################
def fichaIA(tablero):
  while True:
    j2C = rnd.randint(0,2)
    j2F = rnd.randint(0,2)
    if tablero[j2C][j2F] == '-':
      return j2C, j2F
      break

def revisarGanador(tablero,ficha):
  # fil y col
  for i in range(3):
    if tablero[i][0] == tablero[i][1] == tablero[i][2] == ficha:
      return True
  for i in range(3):
    if tablero[0][i] == tablero[1][i] == tablero[2][i] == ficha:
      return True
  # diagonal
  if tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha:
    return True
  if tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha:
    return True
  return False

def jocTrenEnRatja():
  tablero = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
  while True:
    for fila in tablero:
      for casilla in fila:
          print(casilla, end='', sep=' ')
      print()

    posValida = False
    while posValida == False:
      try:
        j1C = int(input('Que columna quieres? (1,2,3): '))-1
        j1F = int(input('Que fila quieres? (1,2,3): '))-1
        if tablero[j1C][j1F] != '-':
          print('Esta posicion ya esta ocupada')
        else:
          tablero[j1C][j1F] = 'X'
          posValida = True
      except ValueError:
        print('Introduce un numero valido (1,2,3).')
      except IndexError:
        print('La columna y la fila deben estar entre 1 y 3.')
      except KeyboardInterrupt:
        print('\nPartida cancelada.')
        return
    if revisarGanador(tablero,'X') == True:
      print('Felicidades has ganado!!')
      print(tablero)
      break

    j2C,j2F = fichaIA(tablero)
    tablero[j2C][j2F] = 'O'


    if revisarGanador(tablero,'O') == True:
        print('Has perdido :C')
        print(tablero)
        break
#Fin tres en raya ################

#Inicio BlackJack #######################
PALOS = ["Corazones", "Diamantes", "Tréboles", "Picas"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
MANOJUGADOR = []
MANODEALER = []

def sacarCarta():
    while True:
        carta = [rnd.choice(VALORES), rnd.choice(PALOS)]
        if carta not in MANOJUGADOR and carta not in MANODEALER:
            return carta

def mostrarCartas(seguir):
      print(f'Mano Dealer (Siempre para al llegar a 16 o mas): {MANODEALER} un total de {sumarCartas(MANODEALER)}')
      print(f'Tu Mano: {MANOJUGADOR} un total de {sumarCartas(MANOJUGADOR)}')
      if len(MANODEALER) == len(MANOJUGADOR) and len(MANOJUGADOR) > 2 and seguir == True:
        print('\nAmbos pedis cartas')
      elif len(MANOJUGADOR) > 2:
        print('\nPides carta')

def sumarCartas(mano):
    total = 0
    ases = 0
    for carta in mano:
        valor = carta[0]
        if valor in ("J", "Q", "K"):
          total += 10
        elif valor == "A":
          total += 11
          ases += 1
        else:
          total += int(valor)
    while total > 21 and ases > 0:
      total -= 10
      ases -= 1
    return total

def dealerPara():
  if sumarCartas(MANODEALER) >= 16:
    print('\nEl Dealer para de pedir cartas.')
  else:
    MANODEALER.append(sacarCarta())

def esBlackjack(mano):
  if len(mano) == 2 and sumarCartas(mano) == 21:
    return True
  else:
    return False

def jocBlackJack():
  turn = 0
  sigue = True
  while True:
    if turn == 0:
      for i in range(2):
        MANOJUGADOR.append(sacarCarta())
        MANODEALER.append(sacarCarta())
      turn +=1
      mostrarCartas(sigue)
      if esBlackjack(MANOJUGADOR) == True:
        print(f'Has gando por blackjack!!\n{MANOJUGADOR}')
      elif esBlackjack(MANOJUGADOR) == True:
        print(f'Has gando por blackjack!!\n{MANODEALER}')
      else:
        continue
    else: 
      if sigue == True:
        try:
          opcionHS = input('\nHit or Stand: ').lower()
        except KeyboardInterrupt:
          print('\nPartida cancelada.')
          break
      dealerPara()
      if opcionHS == 'hit':
        MANOJUGADOR.append(sacarCarta())
        mostrarCartas(sigue)
      elif opcionHS == 'stand':
        sigue = False
      else:
        print('Valor introducido no valido')

      if sigue == False and sumarCartas(MANODEALER) >= 16 or sumarCartas(MANOJUGADOR) > 21:
        mostrarCartas(sigue)
        totalJugador = sumarCartas(MANOJUGADOR)
        totalDealer = sumarCartas(MANODEALER)
        if totalJugador > 21:
            print("Te has pasado, gana el dealer")
            break
        elif totalDealer > 21:
            print("El dealer se ha pasado, ganas tú")
            break
        elif totalJugador > totalDealer:
            print("Ganas tú")
            break
        elif totalJugador < totalDealer:
            print("Gana el dealer")
            break
        else:
            print("Empate")
            break

#Fin BlackJack #######################



def main():
  opcion = False
  while not opcion:
    print('\n\n--- Menu ---')
    print('1. Pedra, Paper, Tisores')
    print('2. Penjat')
    print('3. Tres en ratlla')
    print('4. BlackJack')
    print('0. Salir')
    try:
      userInput = int(input('Que juego quieres jugar (0-4): '))
    except ValueError:
      print('Introduce un número válido (0-4).')
      continue
    except KeyboardInterrupt:
      print('\nAdios!!')
      break
    if userInput < 0 or userInput > 4:
      print('Tu opcion no es valida, vuelve a elegir una.')
      continue
    if userInput == 0:
      print('Adios!!')
      opcion = True
      continue

    try:
      if userInput == 1:
        jocPedraPaperTisores()
      elif userInput == 2:
        jocPenjat()
      elif userInput == 3:
        jocTrenEnRatja()
      elif userInput == 4:
        jocBlackJack()
    except NameError:
      print(f'Ese juego todavía no está disponible')
    except KeyboardInterrupt:
      print('\nJuego cancelado, volviendo al menú.')
    except Exception:
      print(f'Error inesperado durante el juego')
