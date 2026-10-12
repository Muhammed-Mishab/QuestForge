from domain.character import Character

if __name__=="__main__":
    """hero = Character("Araia",100,15)
    goblin = Character("Goblin",30,15)

    print(hero.describe())
    print(goblin.describe())

    hero.attack(goblin)
    print(goblin.describe())

    goblin.heal(goblin)
    print(goblin.describe())

    hero.heal(hero)
    print(hero.describe()) """

    hero = Character("Araia",100,15)
    hero.take_damage(150)
    print(hero.health)