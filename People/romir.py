import random
from Character import Character
import discord 
from discord.ext import commands

class Romir(Character):
    def __init__(self):
        super().__init__("Romir", title="Prophet, Pimp, Maverick", hp=1200, attack=160, dodge=15, crit=15, defense=20,
                         gender=0, critValue=2, srec = 0)
        self.canRespawn = True
   
    
    async def startpassive(self):
        self.modifiers['attack']['selfadd'] = 10*self.resource
        self.modifiers['defense']['selfadd'] = 5*self.resource
        
    async def special(self):
        pass
                  
    async def reset(self):
        self.hp = 1200
        await super().reset()

    async def endround(self): 
        if self.canRespawn and self.getHP() < 0:
            self.hp = 1200
          
            await self.chan.send(f"THE PIMP RETURNS! {self.u.user.name}'s Romir respawned")
            self.canRespawn = False           
        await super().endround()