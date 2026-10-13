class Character:
    def __init__(self,name:str,health:int,attack_power:int):
        self.name = name
        self._health = health
        self._max_health = health
        self.attack_power = attack_power

    @property
    def health(self)->int:
        return self._health

    @property
    def is_alive(self)->bool:
        return self._health > 0

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Damage cannot be negetive")
        self._health = max(0, self._health - amount)

    def describe(self)->str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"

    def attack(self, target: "Character")->None:
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def heal(self,target:"Character",amount : int)->None:
        if amount < 0:
            raise ValueError("Healing amount cannot be negetive")

        target._health = min(target._max_health + amount,target._health + amount)
        print(f"{self.name} heals {target.name} to {target.health} HP")
