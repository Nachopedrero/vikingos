import random
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

def attack(self):
    return self.strength

def receive_damage(self, damage):
    self.health -= damage
class Viking(Soldier):




    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

def attack(self):
    return self.strength

def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
        return f"{self.name} has received {damage} points of damage"
    else:
        return f"{self.name} has died in act of combat"

def battle_cry(self):
    return("Odin ows you all")

class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
def attack(self):
    return self.strength

def receive_damage(self, damage):
    self.health -= damage
    if self.health > 0:
        return f"A Saxon has received {damage} points of damage"
    else:
        return f"A Saxon has died in combat"    

class War:
    
        def __init__(self):
            self.viking_army = []
            self.saxon_army = []


def add_viking(self, Viking):
    self.viking_army.append(Viking)


def add_saxon(self, Saxon):
    self.saxon_army.append(Saxon)

def viking_attack(self):
    viking = random.choice(self.viking_army)
    saxon = random.choice(self.saxon_army)
    result = saxon.receive_damage(viking.strength)
    if saxon.health <= 0:
        self.saxon_army.remove(saxon)
    return result

def saxon_attack(self):
    viking = random.choice(self.viking_army)
    saxon = random.choice(self.saxon_army)
    result = viking.receive_damage(saxon.strength)
    if viking.health <= 0:
        self.viking_army.remove(viking)
    return result

def show_status(self):
    if len(self.saxon_army) == 0:
        return "Vikings have won the war of the century!"
    elif len(self.viking_army) == 0:
        return "Saxons have fought for their lives and survive another day..."
    elif len(self.saxon_army) >= 1 and len(self.viking_army) >= 1:
        return "Vikings and Saxons are still in the thick of battle."


viking1 = Viking("Harald", 100, 50)
viking2 = Viking("Ragnar", 100, 50)
viking3 = Viking("Lagertha", 100, 50)

saxon1 = Saxon(100, 50)
saxon2 = Saxon(100, 50)
saxon3 = Saxon(100, 50)

war = War()
war.add_viking(viking1)
war.add_viking(viking2)
war.add_viking(viking3)
war.add_saxon(saxon1)
war.add_saxon(saxon2)
war.add_saxon(saxon3)

print(war.viking_army)
print(war.saxon_army)

print(war.viking_attack())
print(war.saxon_attack())
print(war.show_status())

