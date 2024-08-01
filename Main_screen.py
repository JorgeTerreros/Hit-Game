#idea hacer un juego de hit como el que hice hace mucho, empezare por hacer la base de pegarle a un enemigo y bajarle la vida
#debo intentar utilizar estructuras de datos que mejoren el rendimiento
#ultimo paso sera basicamente hacerlo visual
from random import randint
from random import random
class Player:
    def __init__(self, name, profesion, hp, damage):
        self.name = name
        self.profesion = profesion
        self.hp = hp
        self.damage = damage
player_1 = Player("Duncan", "attacker", 150, 20) ##tuplas
player_2 = Player("Robert", "tank", 200, 10)
player_3 = Player("Zet", "magician", 100, 30)
playerList = []
playerList.append(player_1) ##metodo para meter un valor a una lista
playerList.append(player_2)
playerList.append(player_3)

""" hacer un inventario para los personajes cambiar armas o guardar armas que ganen en el camino
Me recomiendan usar un array/diccionario/lista simple
Mi pensar es con una pila o listas y colas para poder tener un limite de inventario y en caso de querer cambiar arma sacar la anterior del inventario"""

class Inventario:
    def __init__(self, nombre_item, dmg_weapon, def_shield, healing_amount_item):
        self.nombre_item = nombre_item
        self.dmg_weapon = dmg_weapon
        self.def_shield = def_shield
        self.healing_amount_item = healing_amount_item

Mazo = Inventario("Mazo", 300, 0, 0)
Espada = Inventario("Espada", 150, 0, 0)
Daga = Inventario("Daga", 50, 0, 0)

WeaponList = []
""" hacer una condicion para que el personaje elija un arma dentro del inventario (estoy pensando en que las armas sean dropeadas por los mounstros o un loot random) """
""" if jugador_eleccion = "Mazo":
    WeaponList.append(Mazo)
elif juegador_eleccion = "Espada"
    WeaponList.append(Espada)
elif jugador_eleccion = "Daga"
    WeaponList.append(Daga) """

class Enemy:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp
""" enemy_1 = {'hp': 100, 'name': 'robert', 'damage': 5}"""
enemy_1 = Enemy("InfernoDog", 5, 100)
enemy_2 = Enemy("DarkClerig", 30, 100)
enemy_3 = Enemy("OrcWarrior", 10, 200)
shield = None #none significa que no tiene ningun valor y se puede cambiar a futuro
cura = 10



### Seleccion de personaje ###
### ejemplo eso con switch case ###
""" def switch(personaje):
    if personaje == "1":
        return f"haz seleccionado {player_1.name} tu daño es de {hit(player_1.damage)}, tu hp es de {player_1.hp}"
    elif personaje == "2":
        return f"haz seleccionado {player_2.name} tu daño es de {hit(player_2.damage)}, tu hp es de {player_2.hp}"
    elif personaje == "3":
        return f"haz seleccionado {player_3.name} tu daño es de {hit(player_3.damage)}, tu hp es de {player_3.hp}"
        """
personaje = int(input(f"Seleccione a su personaje: 1) {player_1.name}: {player_1.profesion}, 2) {player_2.name}: {player_2.profesion}, 3) {player_3.name}: {player_3.profesion}: "))

""" if personaje != int:
    print('Ingrese un valor aceptable [1] [2] o [3]')
    personaje = int(input(f"Seleccione a su personaje: 1) {player_1.name}: {player_1.profesion}, 2) {player_2.name}: {player_2.profesion}, 3) {player_3.name}: {player_3.profesion}: "))
"""

def hit():
    enemy_1.hp = enemy_1.hp - damage
    return enemy_1.hp

### a la final me decidi por el metodo match case ###
match personaje: 
    case 1:
        print (f"haz seleccionado {player_1.name} tu daño es de {player_1.damage}, tu hp es de {player_1.hp}")
        damage = player_1.damage
    case 2:
        print(f"haz seleccionado {player_2.name} tu daño es de {player_2.damage}, tu hp es de {player_2.hp}")
        damage = player_2.damage
    case 3:
        print(f"haz seleccionado {player_3.name} tu daño es de {player_3.damage}, tu hp es de {player_3.hp}")
        damage = player_3.damage

print('Bienvenido a Game Hit: ')
### Indice basicamente toma el input de personaje y le resta 1 para que tenga el valor correcto en la posicion de la lista player
indice = personaje - 1

def heal():
    playerList[indice].hp = playerList[indice].hp + cura
    return

while playerList[indice].hp >= 1:
    decision = input('atacar (a), defender (b), curar (c):')

## quiero añadir una funcion de bufo random del enemigo que haga al jugador peligrar y decidir si defenderse o curarse
    dados_de_daño = randint(0, 1)
    if dados_de_daño == 0:
        random_number= 0
        enemyBuffDamage = enemy_1.damage + random_number
    elif dados_de_daño == 1:
        random_number = randint (20, 50)
        print('El enemigo se ha bufeado')
        enemyBuffDamage = enemy_1.damage + random_number
    
    ### HAY QUE MEJORAR LA SINTAXIS CON ESTRUCTURAS DE DATOS PARA LOOPS
    if decision == 'a':
        hit()
        print(f'Al enemigo le quedan: {enemy_1.hp} de vida')
        playerList[indice].hp = playerList[indice].hp - enemyBuffDamage
        print(f'Daño recibido: {enemyBuffDamage} Te quedan: {playerList[indice].hp} puntos de vida')
    elif decision == 'b':
        print(f'te haz defendido')
        print(f'Al enemigo le quedan: {enemy_1.hp} de vida')
        print(f'Te quedan: {playerList[indice].hp} puntos de vida')
    elif decision == 'c':
        heal()
        print(f'Al enemigo le quedan: {enemy_1.hp} de vida')
        playerList[indice].hp = playerList[indice].hp - enemyBuffDamage
        print(f'Daño recibido: {enemyBuffDamage} pero te haz curado te quedan: {playerList[indice].hp} puntos de vida')
        """ player[indice].hp += cura """
    
    if playerList[indice].hp <= 0:
        print('haz muerto')
    elif enemy_1.hp <= 0:
        print('Haz derrotado a tu enemigo felicidades!!')
    
        break