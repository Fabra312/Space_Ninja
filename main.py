import time as ti
import datetime as dti
import random
class Alien:
    race_alien = {
        'Марсианин':(100,20),
        'Твелек':(60,40),
        'Забрак':(120,40),
        'Тогрут':(80,35),
        'Вонг':(150,60),
        'Дазур':(90,45)
    }

    def __init__(self):
        self.name = random.choice(list(self.race_alien.keys()))
        self.hp, self.damage = self.race_alien[self.name]

    def attack_alien(self):
        side = ('Слева','Справа','Сверху','Снизу')
        words = ['Разрез','Удар','Луч','Прорубание']
        action = random.choice(random.choice((side,words)))
        return action


def time_stamp():
    now = dti.datetime.now().timestamp()
    return now


score = 0
print('Добро пожаловать в игру космический ниндзя.')
while True:
    alien = Alien()
    print(f'Вы встретили представителя расы {alien.name}, его HP {alien.hp}, его урон {alien.damage}.')
    attack=alien.attack_alien()
    print(f'{alien.name} наносит тебе удар: {attack}')
    ti.sleep(2)
    time1 = time_stamp()
    unt = input('Отрази атаку: ')
    time2 = time_stamp()
    if time2 - time1 >= 5:
        print('Вы не успели отразить атаку врага, вы останетесь на этой планете навсегда, город под твоей защитой пал.')
        break
    elif attack != unt:
        print('Вы использовали не ту атаку.')
        break
    else:
        score += 1
        print(f'Молодец ты отразил атаку,твой счёт: {score}')
    ti.sleep(2)


print('Игра окончена')