import bot_db
class Bot:                                                     # Class Bot
    def __init__(self,bot_name):                               # initializing a bot through its name, mapped from the bot_db
        h = bot_db[bot_name]
        self.attack =  h['attack']
        self.defense = h['defense']
        self.energy = h['energy']
        self.health =  h['health']
        self.xp = h['xp']
        self.level = h['level']
        self.stack = h['stack']

    def attack_bot(self,target):                                # Attack Function onto a target
        if self.energy >= self.attack:  # Sucessful Attack
            self.energy = self.energy - (self.attack*60/100)     # In a Successful Attack, Energy loss of the attacker is equal to 60% of Attack magnitude
            if target.defense + target.health <= self.attack:       # If attack exceeds defense + health = instant death
                target.health = 0
                target.defense = 0
            else:
                if target.defense > self.attack:                   # If defense > attack then no effect on health, decrease defense
                    target.defense = target.defense - self.attack
                    target.energy = target.energy - (target.energy*3/100) # If defense protects 100% of Health then the energy of target decreases by 3% irrespective of the attack magnitude
                    self.stack += 10  # Increase penalty stack by 10
                    # xp(self)
                else:
                    target.defense = 0                             # If defense < attack then decrease health and defense, no effect on energy
                    target.health = abs(self.attack - (target.defense+target.health))
                    self.stack += 10  # Increase penalty stack by 10

                    # xp(self)
        else: # Failed Attack Because of Less Energy
            self.health = self.health - (self.health*10/100)    # If energy is less than attack and an attack is still performed then 10% health of the attacker is decreased
            target.energy = target.energy + (self.energy*15/100) # In this case of a failed attack, the increase in target's energy is equal to 15% of attacker's energy
            target.health = target.health + (self.health*25/100) # In this case of a failed attack the increase in target's health is equal to 25% of attacker's healths


if __name__ == '__main__':
    print ('choose 2 bots from `simplebot` , `masterbot`, `primebot`, `legendbot`, `godbot`, `omnibot`')
    p, q = input('Enter bots a and b such that a will attack b (ex: primebot legendbot): ').split()
    a = Bot(p)
    b = Bot(q)

    print (main(a,b))

