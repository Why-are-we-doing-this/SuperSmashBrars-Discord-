import random
from Character import Character
import discord 
from discord.ext import commands
class Emily(Character):
    def __init__(self):
        super().__init__("Emily", title="2-Dimensional", hp=1300, attack=220, dodge=20, crit=20, defense=20,
                         gender=1, critValue=2, srec = 6)

    async def startpassive(self):
        if self.enemy.gender == 0:
            self.modifiers['attack']['selfmult'] = 1.5
        

    async def special(self):
        self.modifiers['attack']['selfmult'] *= 3
        self.enemy.doesdodge = 1
        await self.chan.send(f"{self.u.user.name}'s Emily throws a snowflake tantrum")
        self.resource -= self.srec

    async def reset(self):
        self.hp = 1300
        await super().reset()

    async def endround(self):
        if self.isSpecial:
            self.modifiers['attack']['selfmult'] /= 3
            self.hp = self.hp/10 
        await super().endround()