from domain.classes  import Warrior,Mage,Cleric

if __name__=="__main__":

    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric("Anbu")

    warrior.take_damage(50)
    cleric.special_ability(warrior)

    print(warrior.health)



    
