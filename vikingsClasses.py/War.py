from Soldier import Soldier
from Saxon import Saxon
from Viking import Viking
class War(): 
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        import random
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."