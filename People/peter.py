import random
from Character import Character
import discord 
from discord.ext import commands

class Peter(Character):
    def __init__(self):
        super().__init__("Peter", title="Thicc Booty", hp=2500, attack=160, dodge=20, crit=10, defense=25,
                         gender=0, critValue=2, srec=0)
    
    async def special(self):
        for i in self.enemy.team:
            i.modifiers['attack']['othermult'] -= self.resource * 0.11
            i.modifiers['dodge']['othermult'] -= self.resource * 0.11
            i.modifiers['crit']['othermult'] -= self.resource * 0.11
            i.modifiers['defense']['othermult'] -= self.resource * 0.11
        
            await self.chan.send(f"{self.opp.user.name}'s stats drop ")
        self.resource = 0
    
    async def reset(self):
        self.hp = 2500
        await super().reset()

    async def endround(self):
        if random.uniform(1, 100) <= 40:
            self.resource += 2 
            
        if self.doescrit != 1:
            self.resource += 3
        
        if self.doesdodge != 1:
            self.resource += 3  
            
            
            
        await super().endround()
        
        
