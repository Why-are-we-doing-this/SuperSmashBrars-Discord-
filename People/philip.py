import random
from Character import Character
import discord 
from discord.ext import commands

class Philip(Character):
    def __init__(self):
        super().__init__("Phillip", title="Erik Rygh", hp=1000, attack=200, dodge=50, crit=10, defense=10,
                         gender=0, critValue=2, srec=0)
        self.specialKill = False
        self.buff = 0

    async def startpassive(self):
        #print(self.team)
        if self.specialKill: # this happens in the passive and endround so that it doesn't circumvent kyles passive
            await self.chan.send(f"{self.u.user.name}'s Philip tells {self.opp.user.name} to cope harder")
            self.modifiers['attack']['selfmult'] *= 2
            self.specialKill = False
        
        for p in self.team:
            print("furry shift")
            if p.gender == 1:
                self.buff += 1
        self.modifiers['attack']['selfadd'] = self.buff*50
        self.modifiers['defense']['selfadd'] = self.buff*30
        self.buff = 0

        if self.enemy.gender == 1:
            self.modifiers['dodge']['selfadd'] = -20
        else:
            self.modifiers['dodge']['selfadd'] = 0

    
    async def special(self):
        pass
    
    async def reset(self):
        self.hp = 1000
        await super().reset()

    async def endround(self):
        if self.isSpecial and self.enemy.onDeath():
            self.specialKill = True
        buff = 0
        await super().endround()
