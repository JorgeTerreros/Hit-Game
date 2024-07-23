#idea hacer un juego de hit como el que hice hace mucho, empezare por hacer la base de pegarle a un enemigo y bajarle la vida
#debo intentar utilizar estructuras de datos que mejoren el rendimiento
#ultimo paso sera basicamente hacerlo visual
player = {'hp': 100, 'def': 10, 'cura': 5}
Mounstros = [enemy_1 = {'hp': 100, 'name': 'robert', 'damage': 5},
            enemy_2 = {'hp': 100, 'name': 'jose', 'damage': 5}, 
            enemy_3 = {'hp': 100, 'name': 'juan', 'damage': 5}]
def hit():
    attack: 20
    return attack

    
print('Bienvenido a Game Hit: ')

while player['hp'] >= 1:
    decision = input('atacar (a), defender (b), curar (c):')

    if decision == 'a':
        enemy_1['hp'] -= hit