import random



class Mag: 
    def __init__(self, name, armor, min_damage, max_damage, hp):
        self.name = name
        self.armor = armor
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hp = hp    

    def run(self):
        print(self.name + "   выходит...")




    def down_health(self, damage):
        if self.hp <= 0:
            print("{} был расщеплен на молекулы!".format(self.name))
        else:
            self.hp = self.hp - damage
            print("У {} осталось {} очков здоровья".format(self.name, self.hp))










    def fire(self, enemy):
        damage = random.randint(self.min_damage, self.max_damage)
        print("Запускает снаряд в {}".format(self.name, enemy.name))
        enemy.down_health(damage)





    def __str__(self):
        return "{} имеет магическую броню в {} едениц, магический урон в диапозоне очков {}-{} и {} hp".format(
        self.name,
        self.armor,
        self.min_damage,
        self.max_damage,
        self.hp )

 
    

mag1 = Mag("Вася", random, 15, 60, 110)

mag2 = Mag("Рома", random, 20, 80, 100)


print(mag1)

mag2.run()

mag1.fire(mag2)



for bullet in range(7):
    mag1.fire(mag2)












































































































































































































































