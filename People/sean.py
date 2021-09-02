from Character import Character
import discord 
from discord.ext import commands

class Sean(Character):
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=33, crit=33, defense=20,
                         gender=0, critValue=2, srec=3)

    async def startpassive(self):
        self.modifiers['crit']['selfadd'] += 3
        self.modifiers['dodge']['selfadd'] += 3
        
    
    
    async def special(self):

        #self.modifiers['dodge']['selfmult'] = 100000
        #self.modifiers['crit']['selfmult'] = 100000
        self.modifiers['dodge']['selfmult'] = 1000
        self.modifiers['crit']['selfmult'] = 1000 
        self.resource -= self.srec
        await self.chan.send(f"{self.u.user.name}'s Sean's megamind gives him enhanced precision and reflexes")
    
    async def reset(self):
        self.hp = 1200
        await super().reset()

    async def endround(self):
        if self.isSpecial:
            self.modifiers['dodge']['selfmult'] = 1
            self.modifiers['crit']['selfmult'] = 1
            
        await super().endround()
        
        
