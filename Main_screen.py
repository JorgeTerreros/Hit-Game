#idea hacer un juego de hit como el que hice hace mucho, empezare por hacer la base de pegarle a un enemigo y bajarle la vida
#debo intentar utilizar estructuras de datos que mejoren el rendimiento
#ultimo paso sera basicamente hacerlo visual
from random import randint
from random import random
player = {'hp': 100}
enemy_1 = {'hp': 100, 'name': 'robert', 'damage': 5}
""" enemy_2 = {'hp': 100, 'name': 'jose', 'damage': 5}, 
enemy_3 = {'hp': 100, 'name': 'juan', 'damage': 5} """


def hit():
    enemy_1['hp'] = enemy_1['hp'] - 20
    return enemy_1['hp']
shield = 5
cura = 10
    
    
print('Bienvenido a Game Hit: ')

while player['hp'] >= 1:
    decision = input('atacar (a), defender (b), curar (c):')

## quiero añadir una funcion de bufo random del enemigo que haga al jugador peligrar y decidir si defenderse o curarse
    dados_de_daño = randint(0, 1)
    if dados_de_daño == 0:
        random_number= 0
        enemyBuffDamage = enemy_1['damage'] + random_number
    elif dados_de_daño == 1:
        random_number = randint (0, 30)
        print('El enemigo se ha bufeado')
        enemyBuffDamage = enemy_1['damage'] + random_number
    
    ### HAY QUE MEJORAR LA SINTAXIS CON ESTRUCTURAS DE DATOS PARA LOOPS
    if decision == 'a':
        hit()
        print(f'Al enemigo le quedan: {enemy_1["hp"]} de vida')
        player['hp'] = player['hp'] - enemyBuffDamage
        print(f'Te quedan: {player["hp"]} puntos de vida')
    elif decision == 'b':
        enemy_1['damage'] -= shield
    elif decision == 'c':
        player['hp'] += cura
    
    if player['hp'] == 0:
        print('haz muerto')
    elif enemy_1['hp'] == 0:
        print('Haz derrotado a tu enemigo felicidades!!')
    
        break