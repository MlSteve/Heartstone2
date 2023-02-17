class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina
        self.__attack_power = 3

    def _get_health(self):
        return self.__health

    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def introduces(self):
        print("----------------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.__health}\n'
              f'Stamina: {self.__stamina}')
        print("----------------")

    def heals(self, target):
        if self.__stamina >= 20:
            print("----------------")
            print(f'{self.__class__.__name__} накладывает повязку из лечебных трав на {target.__class__.__name__}')
            target._set_health(10)
            self.__stamina -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}\n'
                  f'У {self.__class__.__name__} осталось {self.__stamina} выносливости')
            print("----------------")
        else:
            print("Недостаточно сил для использования способности")

    def attacks(self, target):
        target._set_health(-self.__attack_power)
        if target._get_health() <= 0:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
            return
        print("----------------")
        print(f'{self.__class__.__name__} наносит удар мечом по {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target._get_health()}')
        print("----------------")


class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.__mana = mana

    def _get_health(self):
        return self.__health

    def _set_health(self, points):
        self.__health += points
        if self.__health > 60:
            self.__health = 60
        elif self.__health < 0:
            self.__health = 0

    def introduces(self):
        print("----------------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.__health}\n'
              f'Mana: {self.__mana}')
        print("----------------")

    def heals(self, target):
        if self.__mana < 20:
            print("Недостаточно маны для использования способности")
            return
        print("----------------")
        print(f'{self.__class__.__name__} применяет заклинание лечения к {target.__class__.__name__}')
        target._set_health(10)
        self.__mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}\n'
              f'У {self.__class__.__name__} осталось {self.__mana} маны')
        print("----------------")

    def attacks(self, target):
        target._set_health(-3)
        if target._get_health() <= 0:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
            return
        print("----------------")
        print(f'{self.__class__.__name__} наносит урон магией по {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} уменьшено до {target._get_health()}')
        print("----------------")

#
# unit1 = Warrior(10, 50)
# unit2 = Mage(10, 50)
#
# unit2.attacks(unit1)
# unit2.attacks(unit1)
# unit2.attacks(unit1)
# unit2.attacks(unit1)