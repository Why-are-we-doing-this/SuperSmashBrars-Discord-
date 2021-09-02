import random
from Character import Character
import discord 
from discord.ext import commands

class Kyle(Character):
    def __init__(self):
        super().__init__("Kyle", title="The Aloof Alpha Male", hp=2000, attack=160, dodge=30, crit=30, defense=25,
                         gender=0, critValue=2, srec = 2)
        self.scount = 0
        self.Atk = 0
        self.OppATk = 0
        self.Def = 0
        self.OppDef = 0
        self.Crit = 0
        self.OppCrit = 0
        self.Dodge = 0 
        self.OppDodge = 0

    async def startround(self):
        self.OppAtk = self.enemy.getActualATK()
        self.OppDef = self.enemy.getActualDEF()
        self.OppCrit = self.enemy.getActualCRIT()
        self.OppDodge = self.enemy.getActualDODGE()
        self.Atk = self.getActualATK()
        self.Def = self.getActualDEF()
        self.Crit = self.getActualCRIT()
        self.Dodge = self.getActualDODGE()

    async def midpassive(self):
        self.enemy.modifiers['attack']['otheradd'] -= (self.enemy.getActualATK() - self.OppAtk)/2
        self.enemy.modifiers['defense']['otheradd'] -= (self.enemy.getActualDEF() - self.OppDef)/2
        self.enemy.modifiers['crit']['otheradd'] -= (self.enemy.getActualCRIT() - self.OppCrit)/2
        self.enemy.modifiers['dodge']['otheradd'] -= (self.enemy.getActualDODGE() - self.OppDodge)/2
        self.modifiers['attack']['selfadd'] -= (self.getActualATK() - self.Atk)/2
        self.modifiers['defense']['selfadd'] -= (self.getActualDEF() - self.Def)/2
        self.modifiers['crit']['selfadd'] -= (self.getActualCRIT() - self.Crit)/2
        self.modifiers['dodge']['selfadd'] -= (self.getActualDODGE() - self.Dodge)/2
        if self.scount > 0:
            self.enemy.doesdodge = 1
            self.scount -= 1

    async def reset(self):
        self.hp = 2000
        await super().reset()

    async def special(self):
        self.scount = 3
        self.resource -= self.srec
        await self.chan.send(f"{self.u.user.name}'s Kyle pulls his opponent's chair like the asshole he is")


    async def endround(self):
        await super().endround()