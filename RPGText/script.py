import random as rnd
import time as t
import pprint

from magic import Spells

class colorcodes:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#Color Codes


class Being:   #Stats for character
    def __init__(self, username, health, mana, attack, defense, sorcery,items): #list of stats
        self.totalhealth = health  #total stats and current stats defined
        self.health = health

        self.totalmana = mana
        self.mana = mana            

        self.minattack = attack - 15  #Define upper and lower bounds for attack
        self.maxattack = attack + 15

        self.defense = defense

        self.sorcery = sorcery

        self.possiblemoves = ["Attack", "Sorcery", "Items"]

        self.items = items
        
        self.username = username
      
    def damageGiven(self):  #get a random attack value
        return rnd.randrange(self.minattack,self.maxattack)
    

# get damage and healing
    def TakeDamage(self, damageinflict):
        self.health -= damageinflict
        if self.health <= 0:
            self.health = 0
        return self.health

    def Healing(self, dmg):
        self.health+=dmg
        if self.health>self.totalhealth:
            self.health = self.totalhealth

 #helper functions, keeping track of mana and health

    def getCurrHealth(self):   
        return self.health
        
    def getMaxHealth(self):
        return self.totalhealth
        
    def getMana(self):
        return self.mana
        
    def getMaxMana(self):
         return self.totalmana


#subtract mana costs from current mana pool

    def manaReduce(self, manacost):
        self.mana -=manacost



#pick some action for player to do
    def whatAction(self):
        index = 1
        print("\n" + colorcodes.BOLD + self.username + colorcodes.ENDC)
        print(colorcodes.OKGREEN + colorcodes.BOLD + "Your current moves" + colorcodes.ENDC)
        for option in self.possiblemoves:
            print(str(index) + ":", option)
            index+=1



#get spell id and cost

    def pickSpell(self):
        index = 1
        
        for sp in self.sorcery:
            print("\n" + str(index) + ":", sp.name + " -" + " cost:", str(sp.costspell))
            index+=1

            #pick items

    def getItem(self):
        index = 1
        print(colorcodes.WARNING + colorcodes.BOLD + "Your current moves" + colorcodes.ENDC)
        for it in self.items:
            print("\n" + str(index) + ":", it["item"].name + " -" , str(it["item"].desc), " (x" + str(it["amt"]) + ")")   # get items from dict and let quant differ
            index+=1
#dfine the hp and mana bars
    def getEnemyStats(self):
        hp_bar = ""
        bar_ticks = (self.health / self.totalhealth) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.health) + "/" + str(self.totalhealth)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                     __________________________________________________ ")
        print(colorcodes.BOLD + self.username + "  " +
              current_hp + " |" + colorcodes.FAIL + hp_bar + colorcodes.ENDC + "|")
 #user hp
    def getUserStats(self):
        hp_bar = ""
        bar_ticks = (self.health / self.totalhealth) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mana / self.totalmana) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "


        hp_string = str(self.health) + "/" + str(self.totalhealth)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mana) + "/" + str(self.totalmana)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp = mp_string

        print("                    _________________________              __________ ")
        print(colorcodes.BOLD + self.username + "    " +
              current_hp +" |" + colorcodes.OKGREEN + hp_bar + colorcodes.ENDC + "|    " +
              current_mp + " |" + colorcodes.OKBLUE + mp_bar + colorcodes.ENDC + "|")

        

