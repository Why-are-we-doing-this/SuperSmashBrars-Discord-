import discord 
import random
import math
from discord.ext import commands

class Character(object):
    def __init__(self, name, title, hp, attack, dodge, crit, defense, gender, critValue, srec):
        self.name = name
        self.title = title
        self.hp = hp
        self.attack = attack
        self.dodge = dodge
        self.crit = crit
        self.defense = defense
        self.gender = gender
        self.resource = 0
        self.critValue = critValue
        self.srec = srec 
        self.u = None
        self.opp = None
        self.chan = None

        self.doescrit = 1
        self.doesdodge = 1
        self.isSpecial = False
        
        self.categories = []

        self.swappedin = False
        
        self.enemy = None
        self.team = None

        self.isParalyzed = False
        self.isSimping = False
        self.forceSwapped = False
        self.canActive = False

        self.modifiers = {'hp' :      {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}, 
                        'attack' :    {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'dodge' :     {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}, 
                        'crit' :      {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'defense' :   {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0},
                        'critValue' : {"selfmult" : 1, "othermult" : 1, "selfadd" : 0, "otheradd" : 0}}

    def setEnemy(self, opp):
        self.enemy = opp

    def onDeath(self):
        if self.getHP() <= 0:
            return True

    def testdodged(self):
        self.doesdodge = 1 if random.uniform(1, 100) > self.getActualDODGE() else 0

    def testcrit(self):
        self.doescrit = self.critValue if random.uniform(1, 100) < self.getActualCRIT() else 1

    def getActualATK(self):
        return math.floor((self.attack * self.modifiers['attack']['selfmult'] * self.modifiers['attack']['othermult']) + self.modifiers['attack']['selfadd'] + self.modifiers['attack']['otheradd'])
        
    def getActualDODGE(self):
        return math.floor((self.dodge * self.modifiers['dodge']['selfmult'] * self.modifiers['dodge']['othermult']) + self.modifiers['dodge']['selfadd'] + self.modifiers['dodge']['otheradd'])
        
    def getActualCRIT(self):
        return math.floor((self.crit * self.modifiers['crit']['selfmult'] * self.modifiers['crit']['othermult']) + self.modifiers['crit']['selfadd'] + self.modifiers['crit']['otheradd'])
        
    def getActualDEF(self):
        return math.floor((self.defense * self.modifiers['defense']['selfmult'] * self.modifiers['defense']['othermult']) + self.modifiers['defense']['selfadd'] + self.modifiers['defense']['otheradd'])

    def getHP(self):
        return math.floor((self.hp * self.modifiers['hp']['selfmult'] * self.modifiers['hp']['othermult']) + self.modifiers['hp']['selfadd'] + self.modifiers['hp']['otheradd'])

    def canSpecial(self):
        return self.srec <= self.resource

    def defend(self, opp):
        self.modifiers['defense']['selfadd'] += 50
        opp.modifiers['attack']['selfmult'] *= 0.75
        self.modifiers['dodge']['selfmult'] -= 1000
        self.modifiers['attack']['selfmult'] *= 0.33
        opp.modifiers['dodge']['selfmult'] *= 0.5

    def haymaker(self, opp):
        self.modifiers['attack']['selfmult'] *= 1.5
        self.modifiers['dodge']['selfmult'] *= 0.5
        opp.modifiers['dodge']['selfmult'] *= 2

    def kamikaze(self, opp):
        self.modifiers['attack']['selfmult'] *= 1.5
        opp.modifiers['attack']['selfmult'] *= 2

    def defendend(self, opp):
        self.modifiers['defense']['selfadd'] -= 50
        opp.modifiers['attack']['selfmult'] /= 0.75
        self.modifiers['dodge']['selfmult'] += 1000
        self.modifiers['attack']['selfmult'] /= 0.33
        opp.modifers['dodge']['selfmult'] /= 0.5

    def haymakerend(self, opp):
        self.modifiers['attack']['selfmult'] /= 1.5
        self.modifiers['dodge']['selfmult'] /= 0.5
        opp.modifiers['dodge']['selfmult'] /= 2

    def kamikazeend(self, opp):
        self.modifiers['attack']['selfmult'] /= 1.5
        opp.modifiers['attack']['selfmult'] /= 2

    async def reset(self):
        for stats, mods in self.modifiers.items():
            for key, values in mods.items():
                if values > 1:
                    self.modifiers[stats][key] = 1 if "mult" in key else 0
        print(self.getHP())

    async def canHit(self):
        if self.isParalyzed:
            await self.chan.send(f"{self.u.user.name}'s {self.name} is Paralyzed and cannot attack")
            return False
        else:
            return True

    async def damage(self, opp):
        if await self.canHit():
            if opp.getActualDEF() >= 0:
                opp.hp -= opp.doesdodge*(self.doescrit*self.getActualATK() - opp.getActualDEF())
            else:
                opp.hp -= 2*opp.doesdodge*(self.doescrit*self.getActualATK() - opp.getActualDEF())
            if self.doescrit > 1:
                await self.chan.send(f"{self.u.user.name}'s {self.name} hit a crit")
            if opp.doesdodge == 0:
                await self.chan.send(f"{opp.u.user.name}'s {opp.name} dodged")

    async def special(self):
        pass 

    async def preactive(self):
        pass 

    async def postactive(self):
        pass

    async def startround(self):
        pass

    async def startpassive(self):
        pass 

    async def midpassive(self):
        pass 

    async def endpassive(self):
        pass 

    async def endround(self):
        self.resource += 1

        if self.isSpecial:
            self.isSpecial = False
















           