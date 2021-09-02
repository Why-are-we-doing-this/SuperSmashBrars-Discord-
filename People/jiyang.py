import random
from Character import Character
import discord 
from discord.ext import commands

class Jiyang(Character):
    def __init__(self):
        super().__init__("Jiyang", title="African American Paragon", hp=700, attack=210, dodge=700, crit=50, defense=3,
                         gender=0, critValue=3, srec = 1)

    async def passive(self):
        if random.uniform(1, 100) <= 30:
            await self.chan.send("Jiyang's attack missed")
            self.modifiers['attack']['selfmult'] = 0


    async def passiveend(self):
        self.modifiers['attack']['selfmult'] = 1
    
    
    async def specialend(self):
        pass

    async def reset(self):
        self.hp = 700
        await super().reset()
    
    async def special(self):
        await self.chan.send(f"{self.u.user.name}'s Jiayng uses his special")
        self.resource -= self.srec
        self.srec += 3 
        if random.randint(1, 6) == 1:
            await self.chan.send(f"{self.u.user.name}'s Jiyang says: We may be equal, but some are more equal than other")
            self.enemy.hp = self.hp

    async def endround(self):
        await super().endround()