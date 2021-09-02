import random
from Character import Character
import discord 
from discord.ext import commands

class Sara(Character):
    def __init__(self):
        super().__init__("Sara", title="Saraline Hooey", hp=1600, attack=150, dodge=20, crit=-100, defense=10,
                         gender=1, critValue=2, srec = 3)
        self.scount = 0
        self.scenemy = " "

    async def startpassive(self):      
        self.modifiers['crit']['selfadd'] += 5
                 
    
    async def special(self):
        await self.chan.send(f"{self.u.user.name}'s Sara randomly yells \"AWWWW YOU\'D LIKE THAT\"")
        self.enemy.modifiers['defense']['otheradd'] -= 110
        self.scount = 5
        self.scenemy = self.enemy.title
        self.resource -= self.srec
        self.srec += 2
    
    
    """
    def onswap(self):
        self.modifiers['crit']['selfadd'] = 0
        self.crit = int(self.crit/2)
    
    """

    async def reset(self):
        self.hp = 1600
        await super().reset()

    async def endround(self):
        if self.scount > 0 and self.enemy.title == self.scenemy:
            self.enemy.modifiers['defense']['otheradd'] += 20
            self.scount -= 1

                
                
        
        """
        if self.isSpecial:
            self.enemy.modifiers['defense']['otheradd'] -= -100
        """
        await super().endround()