import random
from Character import Character
import discord 
from discord.ext import commands

class Jay(Character):
    selfhit = 12
    hitself = False

    def __init__(self):
        super().__init__("Jay", title="GayJay47", hp=3100, attack=280, dodge=0, crit=10, defense=50, gender=0, critValue=2, srec=11)

    async def startpassive(self):
        #print(self.selfhit)
        if random.uniform(1, 100) < self.selfhit:
            #print("hsbfjsdfbfhsbfhjfbhjsfs")
            self.hitself = True
            self.canHit = False

    async def endpassive(self):
        if self.hitself:
            hp = self.getHP()
            self.canHit = True
            await self.damage(self)
            await self.u.user.send("Jay dealt {} damage to himself!".format(-self.getHP() + hp))


        #self.selfhit = 12

    async def special(self):
        self.isSpecial = True
        self.modifiers['attack']['selfmult'] = 2
        self.modifiers['crit']['selfadd'] = 1000
        self.modifiers['defense']['selfadd'] -= 100
        
        self.enemy.modifiers['dodge']['othermult'] = 0
        self.doesdodge = 1
        self.doescrit = self.critValue
      
        self.resource -= self.srec
        await self.chan.send(f"{self.u.user.name}'s Jay's Hemmeroids cause him to enter a frenzy")
        #return "undodgeable"
        

    async def reset(self):
        self.hp = 3100
        await super().reset()

    async def endround(self):
        self.selfhit += 2
        if self.hitself:
            self.hitself = False
            
        if self.isSpecial:
            self.modifiers['attack']['selfmult'] = 1
            self.modifiers['crit']['selfadd'] = 0
            self.modifiers['defense']['selfadd'] = 0
            self.enemy.modifiers['dodge']['othermult'] = 1
            
        await super().endround()
            
            
