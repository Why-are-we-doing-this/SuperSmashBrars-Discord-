import random
from Character import Character
import discord 
from discord.ext import commands

class Jessica(Character):
    def __init__(self):
        super().__init__("Jessica", title="Fisiks Queen", hp=2000, attack=130, dodge=20, crit=10, defense=10,
                         gender=1, critValue=2, srec = 0)

    async def startpassive(self):
        self.modifiers['attack']['selfadd'] = 5*self.resource
        self.modifiers['crit']['selfadd'] = 5*self.resource
        self.modifiers['dodge']['selfadd'] = 5*self.resource

    async def special(self):
        self.enemy.hp -= 40*self.resource
        self.resource = 0
        await self.chan.send(f"{self.u.user.name}'s Jessica nerds out which hurts her opponent on a spirtual level")

    async def reset(self):
        self.hp = 2000
        await super().reset()

    async def endround(self):
        await super().endround()