import random
from Character import Character
import discord 
from discord.ext import commands

class Yash(Character):
    def __init__(self):
        super().__init__("Yash", title="TikTokThot", hp=1600, attack=170, dodge=20, crit=10, defense=10,
                         gender=0, critValue=2, srec=1)
        self.scount = -1
        self.turncount = 0
        self.buffs = ["hp", "attack", "defense", "crit", "dodge"]

    async def startpassive(self):
        if self.turncount%3 == 0 and self.turncount != 0: 
            stat = random.randint(0,4)
            await self.chan.send(f"BLM, ACAB, CAL 2025-{self.u.user.name}'s Yash:nerd:")
            await self.u.user.send(f"{self.u.user.name}'s Yash's {self.buffs[stat]} was increased by 10%.")

            if stat == 0:
                self.modifiers[self.buffs[stat]]['selfadd'] += 160
            elif stat < 3 and stat > 0:
                self.modifiers[self.buffs[stat]]['selfmult'] += 0.1
            else: 
                self.modifiers[self.buffs[stat]]['selfadd'] += 10
                
    async def special(self):
        await self.chan.send(f"{self.u.user.name} sends {self.opp.user.name}'s {self.enemy.name} one of their Yash's tiktoks")
        self.enemy.isParalyzed = True
        self.scount = 2
        self.resource -= self.srec
        self.srec += 2

    async def reset(self):
        self.hp = 1600
        await super().reset()

    async def endround(self):
        if self.scount > 0:
            self.scount -= 1
        if self.scount == 0:
            self.enemy.isParalyzed = False
            self.scount -= 1
        self.turncount += 1

        await super().endround()