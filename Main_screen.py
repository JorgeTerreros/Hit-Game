#idea hacer un juego de hit como el que hice hace mucho, empezare por hacer la base de pegarle a un enemigo y bajarle la vida
#debo intentar utilizar estructuras de datos que mejoren el rendimiento
#ultimo paso sera basicamente hacerlo visual
from random import randint
from random import random
player_1 = {'hp': 150, 'name': "Duncan", 'profesion': "attacker", 'damage': 20}
player_2 = {'hp': 200, 'name': "Robert", 'profesion': "tank", 'damage': 10}
player_3 = {'hp': 100, 'name': "Zet", 'profesion': "magician", 'damage': 30}
player = []
player.append(player_1)
player.append(player_2)
player.append(player_3)
shield = 5
cura = 10
enemy_1 = {'hp': 100, 'name': 'robert', 'damage': 5}
""" enemy_2 = {'hp': 100, 'name': 'jose', 'damage': 5}, 
enemy_3 = {'hp': 100, 'name': 'juan', 'damage': 5} """


### Seleccion de personaje ###
### ejemplo eso con switch case ###
""" def switch(personaje):
    if personaje == "1":
        return f"haz seleccionado {player_1['name']} tu daño es de {hit(player_1['damage'])}, tu hp es de {player_1['hp']}"
    elif personaje == "2":
        return f"haz seleccionado {player_2['name']} tu daño es de {hit(player_2['damage'])}, tu hp es de {player_2['hp']}"
    elif personaje == "3":
        return f"haz seleccionado {player_3['name']} tu daño es de {hit(player_3['damage'])}, tu hp es de {player_3['hp']}"
        """
personaje = int(input(f"Seleccione a su personaje: 1) {player_1['name']}: {player_1['profesion']}, 2) {player_2['name']}: {player_2['profesion']}, 3) {player_3['name']}: {player_3['profesion']}: "))

""" if personaje != int:
    print('Ingrese un valor aceptable [1] [2] o [3]')
    personaje = int(input(f"Seleccione a su personaje: 1) {player_1['name']}: {player_1['profesion']}, 2) {player_2['name']}: {player_2['profesion']}, 3) {player_3['name']}: {player_3['profesion']}: "))
 """

def hit():
    enemy_1['hp'] = enemy_1['hp'] - damage
    return enemy_1['hp']

### a la final me decidi por el metodo match case ###
match personaje: 
    case 1:
        print (f"haz seleccionado {player_1['name']} tu daño es de {player_1['damage']}, tu hp es de {player_1['hp']}")
        damage = player_1['damage']
    case 2:
        print(f"haz seleccionado {player_2['name']} tu daño es de {player_2['damage']}, tu hp es de {player_2['hp']}")
        damage = player_2['damage']
    case 3:
        print(f"haz seleccionado {player_3['name']} tu daño es de {player_3['damage']}, tu hp es de {player_3['hp']}")
        damage = player_3['damage']

print('Bienvenido a Game Hit: ')
### Indice basicamente toma el input de personaje y le resta 1 para que tenga el valor correcto en la posicion de la lista player
indice = personaje - 1

def heal():
    player[indice]['hp'] = player[indice]['hp'] + cura
    return

while player[indice]['hp'] >= 1:
    decision = input('atacar (a), defender (b), curar (c):')

## quiero añadir una funcion de bufo random del enemigo que haga al jugador peligrar y decidir si defenderse o curarse
    dados_de_daño = randint(0, 1)
    if dados_de_daño == 0:
        random_number= 0
        enemyBuffDamage = enemy_1['damage'] + random_number
    elif dados_de_daño == 1:
        random_number = randint (20, 50)
        print('El enemigo se ha bufeado')
        enemyBuffDamage = enemy_1['damage'] + random_number
    
    ### HAY QUE MEJORAR LA SINTAXIS CON ESTRUCTURAS DE DATOS PARA LOOPS
    if decision == 'a':
        hit()
        print(f'Al enemigo le quedan: {enemy_1["hp"]} de vida')
        player[indice]['hp'] = player[indice]['hp'] - enemyBuffDamage
        print(f'Daño recibido: {enemyBuffDamage} Te quedan: {player[indice]["hp"]} puntos de vida')
    elif decision == 'b':
        print(f'te haz defendido')
        print(f'Al enemigo le quedan: {enemy_1["hp"]} de vida')
        print(f'Te quedan: {player[indice]["hp"]} puntos de vida')
    elif decision == 'c':
        heal()
        print(f'Al enemigo le quedan: {enemy_1["hp"]} de vida')
        player[indice]['hp'] = player[indice]['hp'] - enemyBuffDamage
        print(f'Daño recibido: {enemyBuffDamage} pero te haz curado te quedan: {player[indice]["hp"]} puntos de vida')
        """ player[indice]['hp'] += cura """
    
    if player[indice]['hp'] <= 0:
        print('haz muerto')
    elif enemy_1['hp'] <= 0:
        print('Haz derrotado a tu enemigo felicidades!!')
    
        break