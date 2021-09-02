import random
from Character import Character
import discord 
from discord.ext import commands


class Arvin(Character):
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2000, attack=160, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2, srec = 1)


    async def endpassive(self):
        o = random.randint(40, 60)
        self.modifiers['hp']['selfadd'] += o
        #self.hp = min(2100, self.hp + o)
        
        await self.u.user.send(f"Arvin heals {o} hp")

    async def special(self):
        self.modifiers['attack']['selfadd'] += 20*self.resource
        self.resource -= self.resource
        await self.chan.send(f"{self.u.user.name}'s Arvin eats his veggies")

    async def reset(self):
        self.hp = 2000
        await super().reset()


    async def endround(self):
        await super().endround()

























