import random
from Character import Character
import discord 
from discord.ext import commands

class Michael(Character):
    def __init__(self):
        super().__init__("Mikey", title="Simply Milky", hp=1900, attack=150, dodge=10, crit=10, defense=10,
                         gender=0, critValue=2, srec = 1)

    async def special(self):
        self.enemy.forceSwapped = True
        self.resource -= self.srec
        self.srec += 2
        await self.chan.send(f"{self.u.user.name}'s Mikey spams and pings some cuck on {self.opp.user.name}'s team to get online making him come out")

    async def reset(self):
        self.hp = 1900
        await super().reset()

    async def endpassive(self):
        if self.enemy.swappedin:
            self.enemy.modifiers['attack']['othermult'] = 0.8
            self.enemy.modifiers['defense']['othermult'] = 0.8
            self.enemy.modifiers['crit']['othermult'] = 0.8
            self.enemy.modifiers['dodge']['othermult'] = 0.8

    async def endround(self):
        await super().endround()