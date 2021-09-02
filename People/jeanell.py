import random
from Character import Character
import discord 
from discord.ext import commands


class Jeanell(Character):
    def __init__(self):
        super().__init__("Jeanell", title="Left The Chat", hp=3000, attack=260, dodge=10, crit=0, defense=40,
                         gender=1, critValue=2, srec = 11)
        self.usedSpecial = False
        self.extraDamage = 0
        self.currenthp = 0

    async def startpassive(self):
        self.extraDamage = random.randint(1, 4)
        self.currenthp = self.getHP()

    async def special(self):
        if not self.usedSpecial:
            self.modifiers['attack']['selfmult'] = 3
            await self.chan.send("Jeanell is immune to taking damage this turn")
            self.usedSpecial = True
            self.resource -= self.srec
            self.srec = 100000000
            await self.chan.send(f"{self.opp.user.name} insults {self.u.user.name}'s Jeanell's bisexuality by saying nothing causing her to enter a frenzy")

    async def reset(self):
        self.hp = 3000
        await super().reset()

    async def endpassive(self):
        if self.isSpecial:
            self.hp = self.currenthp
            self.modifiers['attack']['selfmult'] = 1
        if self.extraDamage == 1:
            self.hp -= 2*(self.currenthp - self.getHP())
            await self.chan.send("Jeanell takes 3x damage")

    async def endround(self):
        await super().endround()