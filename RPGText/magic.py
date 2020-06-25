#instance of spells user can call
import random as rnd
class Spells:
    #def spells with identifying stats
    def __init__(self, name, costspell, damagedone, spelltype):
        self.name = name
        self.costspell = costspell
        self.damagedone = damagedone
        self.spelltype = spelltype
        #get dmg for each spell
    def gen_dmg(self):
        lowerbound = self.damagedone - 10
        upperbound = self.damagedone + 10
        return rnd.randrange(lowerbound, upperbound)