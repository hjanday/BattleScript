from script import Being, colorcodes # Getting module imports from each class
from magic import Spells
from userinv import Item 
import time as t
import random as rnd

#spaces and gen hp bars for friendly players

 
#Beginner Spells
Zap = Spells("Zap", 20, 300, "Basic")
Wither = Spells("Wither", 40, 200, "Basic")
Fear = Spells("Fear", 50, 350, "Basic")
Burn = Spells("Burn", 60, 500, "Basic")
Poison = Spells("Poison", 10, 100, "Basic")

# Good spells

Solace = Spells("Solace", 10, 15, "Good")
Arise = Spells("Arise", 100, 100, "Good")


#making some items

#healable consumables
superPot = Item("super-potion", "potion", "heals for 200 health", 200)
normPot = Item("normal-potion", "potion", "heals for 35 hp",35)
fullRes = Item("full-res","potion", "Fully restores hp", 9999)

divineElixir = Item("divine-elixir", "elixir", "Elixir made by the gods, refills hp and mana", 9999)

harmPot = Item("harm-pot", "attack", "damages for 150", 150)

#list of spells and items
playerSp = [Zap,Wither,Fear,Burn,Poison,Solace,Arise]
playerIt = [{"item" : superPot, "amt" : 5,}, {"item" : normPot, "amt" : 5}, {"item" : fullRes, "amt" : 5}, {"item" : divineElixir, "amt" : 5},{"item" : harmPot, "amt" : 5} ]


enemySp = [Zap,Fear,Solace]
enemyIt = [{"item" : superPot, "amt" : 3}, {"item" : harmPot, "amt" : 3}]

#make characters
player0 = Being("Kriol",500,100,40,110,playerSp,playerIt) # Give the character the stats listed from Being | username, health, mana, attack, defense, sorcery,items |
player1 =  Being("Adadr",700,110,50,140,playerSp,playerIt)
player2 =  Being("Edgar",600,150,30,90,playerSp,playerIt)

plist = [player0,player1,player2]

enemy = Being("Arthur",10000,150,30,300,[],[])
enemy1 =  Being("Vance",900,210,45,100,playerSp,playerIt)
enemy2 =  Being("Ricardo",300,200,50,150,playerSp,playerIt)

elist = [enemy,enemy1,enemy2]

isRun = True
index = 0
# Initiate battle
print(colorcodes.WARNING + "You're finally awake,", player1.username, ", Now we can battle!" + colorcodes.ENDC)
t.sleep(3)
print(colorcodes.FAIL + colorcodes.BOLD + enemy.username + " tries to attack" + colorcodes.ENDC)

while isRun:
    print("-----------------------------------------------------------------------------")

#get hp and mana of multiple players

    print("\n\n")
    print(colorcodes.BOLD + colorcodes.OKBLUE + "NAME                Health                                Mana" + colorcodes.ENDC)
    for player in plist:
        player.getUserStats()
        
    print("\n")

    enemy.getEnemyStats()

    for player in plist:
        player.whatAction()
        chosen = input("        What do you do?")
        choiceInd = int(chosen) - 1 #able to pass into arr

    # get battle sequence (just attacks)
        if(choiceInd == 0):
            inflict = player.damageGiven()
            enemy.TakeDamage(inflict)
            print(colorcodes.OKBLUE + player.username + " hits for", inflict, "hp" + colorcodes.ENDC)

    # initiate spells
        elif (choiceInd == 1):
            print(colorcodes.OKBLUE + colorcodes.BOLD + "Available Spells\n" + colorcodes.ENDC)
            player.pickSpell()
            playerchoice = int (input("     What spell do you use?")) -1

    #0 for going back
            if playerchoice == -1:
                continue


        #get spell from class
            spell = player.sorcery[playerchoice]
            spelldmg = spell.gen_dmg()

            currentMana = player.getMana()
    # check if spell can cast
            if(spell.costspell > currentMana):
                print(colorcodes.FAIL + "\nYou don't have enough mana to cast\n" + colorcodes.ENDC)
                continue
            player.manaReduce(spell.costspell)

            # get heal spells now
            if spell.spelltype == "Good":
                player.Healing(spelldmg)
                print(colorcodes.OKBLUE + "\n" + spell.name + " heals you for", str (spelldmg), "health" + colorcodes.ENDC)    

                #attack spells
            elif spell.spelltype == "Basic":
                enemy.TakeDamage(spelldmg)
                print(colorcodes.HEADER + "\n" + spell.name + " does", str(spelldmg), "points of damage" + colorcodes.ENDC)

        elif choiceInd == 2:
            player.getItem()
            itemchoose = int(input("    Pick an item :")) -1 #get choice - 1 to get array index

    #lets ppl go back with 0
            if itemchoose == -1:
                continue
    # if item chosen, reduce quantity
            item = player.items[itemchoose]["item"]
            if(player.items[itemchoose]["amt"]==0):
                print(colorcodes.HEADER + colorcodes.FAIL + "\n" + " That item slot is empty.  Choose another item" + colorcodes.ENDC)
                continue

            player.items[itemchoose]["amt"] -=1

        

            if item.type == "potion":
                player.Healing(item.itemproperty)
                print(colorcodes.HEADER + "\n" + item.name + " heals for", str(item.itemproperty), "points of health" + colorcodes.ENDC)
                
            elif item.type == "elixir":
                if item.name == "divine-elixir":
                    for p in plist:
                        p.health = p.totalhealth
                        p.mana = p.totalmana
                    else:
                        player.health = player.totalhealth
                        player.mana = player.totalmana
                    print(colorcodes.OKBLUE + "\n" + item.name + " restores your hp and mana" + colorcodes.ENDC)
            
            elif item.type == "attack":
                enemy.TakeDamage(item.itemproperty)
                print(colorcodes.FAIL + "\n" + item.name + " does " + str(item.itemproperty) + " damage" + colorcodes.ENDC)



# track of hp and mana

            # This lets enemy randomly target other players
    enemy_choice = 1
    atktarget = rnd.randrange(0,3)

    enemy_damage = enemy.damageGiven() 


    plist[atktarget].TakeDamage(enemy_damage)
    print(colorcodes.FAIL + enemy.username + " strikes " + player1.username + " for", enemy_damage, "hp" + colorcodes.ENDC)

    """print("_________________________________")
    print("Opponent Health :", colorcodes.FAIL + str(enemy.getCurrHealth()) + "/" + str(enemy.getMaxHealth()) + colorcodes.ENDC + "\n")
    print("Player Health :", colorcodes.OKBLUE + str(player.getCurrHealth()) + "/" + str(player.getMaxHealth()) + colorcodes.ENDC + "\n")
    print("Player Mana :" , colorcodes.OKGREEN + str(player.getMana()) + "/" + str(player.getMaxMana()) + colorcodes.ENDC + "\n")
    """



# end conditions
    if(enemy.getCurrHealth() == 0):
        print(colorcodes.OKBLUE + enemy.username + " is slain. You are victorious" + colorcodes.ENDC)
        isRun = False
    elif(player.getCurrHealth() == 0):
        print(colorcodes.WARNING + player1.username + " were slain in combat. You lost" + colorcodes.ENDC)
        isRun = False





