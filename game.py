import discord 
from copy import deepcopy
from discord.ext import commands
from People.dummy import Dummy
from People.dummy import Dummy2
from People.dummy import Dummy3
from People.arvin import Arvin
from People.emily import Emily
from People.jeanell import Jeanell
from People.sean import Sean
from People.jay import Jay
from People.mikey import Michael
from People.jiyang import Jiyang
from People.jessica import Jessica
from People.kyle import Kyle
from People.peter import Peter
from People.philip import Philip
from People.rahul import Rahul
from People.romir import Romir
from People.sara import Sara
from People.yash import Yash
from player import Player

class Battle(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.characters = [Dummy(), Dummy2(), Dummy3(), Arvin(), Emily(), Jay(), Jeanell(), Sean(), Michael(), Jiyang(), Jessica(), Kyle(), Peter(), Philip(), Rahul(), Romir(), Sara(), Yash()]

	@commands.command(aliases = ["b"])
	async def battle(self, ctx, opponent: discord.Member, ts):
		u1 = Player(ctx.author)
		u2 = Player(opponent)

		#It doesn't fucking work make a reset 
		#Picking your characters
		async def pickChar(u, n, i, c, opp, characters):
			await ctx.send(f"Player {n}, select Character {len(u.Characters)+1}")
			char = await self.bot.wait_for('message', check = lambda m: m.author == u.user)
			for x in characters:
				if x.name == char.content and x not in u.Characters:
					y = x
					y.u = u
					y.opp = opp
					y.chan = ctx.message.channel
					u.Characters.append(y)
					c = len(u.Characters) 
			if len(u.Characters) < c:
				await ctx.send("Pleeeeease put in a Valid name of a Char you haven't already selected")
			if len(u.Characters) < i:
				c += 1
				await pickChar(u, n, i, c, opp, characters)
		await pickChar(u1, 1, int(ts), 1, u2, self.characters)
		await pickChar(u2, 2, int(ts), 1, u1, self.characters)


		#Displaying your characters
		await u1.user.send("Player 1, your characters are:")
		for i in range(len(u1.Characters)):
			await u1.user.send(f"{u1.Characters[i].name}\n")

		await u2.user.send("Player 2, your characters are:")
		for i in range(len(u2.Characters)):
			await u2.user.send(f"{u2.Characters[i].name}\n")

		await ctx.send("battle beginning")

		t1 = u1.Characters
		t2 = u2.Characters
		d1 = u1.Dcharacters
		d2 = u2.Dcharacters
		p1 = t1[0]
		p2 = t2[0]

		turn = 0
		while True:
			turn += 1

			p1.setEnemy(p2)
			p2.setEnemy(p1)
			p1.team = t1
			p2.team = t2

			if turn == 1:
				await ctx.send("** **")
				hp1 = await ctx.send(f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				hp2 = await ctx.send(f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")
				await ctx.send("** **")

				await u1.user.send("** **")
				dm1hp1 = await u1.user.send(f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				dm1hp2 = await u1.user.send(f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")
				await u1.user.send("** **")

				await u2.user.send("** **")
				dm2hp1 = await u2.user.send(f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				dm2hp2 = await u2.user.send(f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")
				await u2.user.send("** **")
				
			else:
				await hp1.edit(content=f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				await hp2.edit(content=f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")

				await dm1hp1.edit(content=f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				await dm1hp2.edit(content=f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")

				await dm2hp1.edit(content=f"***{u1.user.name}'s {p1.name} has {p1.getHP()} hp left***")
				await dm2hp2.edit(content=f"***{u2.user.name}'s {p2.name} has {p2.getHP()} hp left***")

			#Loss checks
			if len(t1) == len(t2) and 0:
				await ctx.send("Match was a tie")
				for x in u1.Characters:
					await x.reset()
				for x in u1.Dcharacters:
					await x.reset()
				for y in u2.Dcharacters:
					await y.reset()
				for y in u2.Characters:
					await y.reset()
				break
			if len(t1) == 0:
				await ctx.send(f"{u2.user.name} wins")
				for x in u1.Characters:
					await x.reset()
				for x in u1.Dcharacters:
					await x.reset()
				for y in u2.Dcharacters:
					await y.reset()
				for y in u2.Characters:
					await y.reset()
				break
			if len(t2) == 0:
				await ctx.send(f"{u1.user.name} wins")
				for x in u1.Characters:
					await x.reset()
				for x in u1.Dcharacters:
					await x.reset()
				for y in u2.Dcharacters:
					await y.reset()
				for y in u2.Characters:
					await y.reset()
				break

			await ctx.send(f"turn {turn}")
			await ctx.send("** **")
			await u1.user.send(f"turn {turn}")
			await u1.user.send("** **")
			await u2.user.send(f"turn {turn}")
			await u2.user.send("** **")

			#Starting the round
			await p1.startround()
			await p2.startround()

			#Start passives
			await p1.startpassive()
			await p2.startpassive()

			#Deciding moves
			async def decideMove(c, u, p):
				if c.canSpecial() and c.canActive:
					await u.user.send(f"Player {p}, will {c.name} punch(p), kamikaze(k), throw a haymaker(h), defend(d) special(s), change character(c),or use their active(a)")
					choice = await self.bot.wait_for('message', check = lambda m: m.author == u.user and (m.content == "p" or "k" or "h"  or "d" or "s" or "c" or "a"))
				elif c.canActive:
					await u.user.send(f"Player {p}, will {c.name} punch(p), kamikaze(k), throw a haymaker(h), defend(d) change character(c), or use their active(a)")
					choice = await self.bot.wait_for('message', check = lambda m: m.author == u.user and (m.content == "p" or "k" or "h" or "d" or "c" or "a"))
				elif c.canSpecial():
					await u.user.send(f"Player {p}, will {c.name} punch(p), kamikaze(k), throw a haymaker(h), defend(d), special(s), or change character(c)")
					choice = await self.bot.wait_for('message', check = lambda m: m.author == u.user and (m.content == "p" or "k" or "h" or "d" or "s" or "c"))
				else:
					await u.user.send(f"Player {p}, will {c.name} punch(p), kamikaze(k), throw a haymaker(h), defend(d), or change character(c)")
					choice = await self.bot.wait_for('message', check = lambda m: m.author == u.user and (m.content == "p" or "k" or "h" or "d" or "c"))
				return choice.content

			c1 = await decideMove(p1, u1, 1)
			c2 = await decideMove(p2, u2, 2)

		
			#Character Switches
			async def Switch(p, u, t):
				await u.user.send("Pick who you want to switch with their index or name")
				i = await self.bot.wait_for('message', check = lambda m: m.author == u.user and ((any(m.content == x.name for x in t1)) or (m.content == "1" or "2" or "3")))
				op = p
				for x in t:
					print("works 1")
					if x.name == i.content:
						print("works 2")
						p = x 
						return p
						break
					elif i.content.isdigit():
						if x.name == t[int(i.content)-1].name:
							p = x
							return p
				if p == op:
					await u.user.send("Please pick a different character that exists")
					await Switch(p, u, t)
				
			#Swaps
			if c1 == "c":
				p1 = await Switch(p1, u1, t1)
				p1.swappedin = True
			if c2 == "c":
				p2 = await Switch(p2, u2, t2)
				p2.swappedin = True

			#Pre-actives
			if c1 == "a":
				await p1.preactive()
			if c2 == "a":
				await p2.preactive()

			#Specials
			if c1 == "s":
				await p1.special()
				p1.isSpecial = True
			if c2 == "s":
				p2.isSpecial = True
				await p2.special()

			#ForceSwaps
			if p1.forceSwapped:
				p1.forceSwapped = False
				p1 = await Switch(p1, u2, t1)
				p1.swappedin = True
				await ctx.send(f"{u2.user.name}'s Mikey forces {u1.user.name} to swap to {p1.name}")
			if p2.forceSwapped:
				p2.forceSwapped = False
				p2 = await Switch(p2, u1, t2)
				p2.swappedin = True
				await ctx.send(f"{u1.user.name}'s Mikey forces {u2.user.name} to swap to {p2.name}")

			#Haymaker, Kamikaze, and Defend start
			if c1 == "d":
				p1.defend(p2)
				await ctx.send(f"{u1.user.name}'s {p1.name} defended")
			if c2 == "d":
				p2.defend(p1)
				await ctx.send(f"{u2.user.name}'s {p2.name} defended")

			if c1 == "h":
				p1.haymaker(p2)
				await ctx.send(f"{u1.user.name}'s {p1.name} threw a haymaker")
			if c2 == "h":
				p2.haymaker(p1)
				await ctx.send(f"{u2.user.name}'s {p2.name} threw a haymaker")

			if c1 == "k":
				p1.kamikaze(p2)
				await ctx.send(f"{u1.user.name}'s {p1.name} did a kamikaze attack")
			if c2 == "k":
				p2.kamikaze(p1)
				await ctx.send(f"{u2.user.name}'s {p2.name} did a kamikaze attack")

			p1.testdodged()
			p2.testdodged()
			p2.testcrit()
			p1.testcrit()

			#Mid passives
			await p1.midpassive()
			await p2.midpassive()

			if c1 == "c":
				await ctx.send(f"Player 1 switched to {p1.name}\n ")
			if c2 == "c":
				await ctx.send(f"Player 2 switched to {p2.name}\n ")

			#Damage
			await p1.damage(p2)
			await p2.damage(p1)

			#Haymaker, Kamikaze, and Defend end
			if c1 == "d":
				p1.defendend(p2)
			if c2 == "d":
				p2.defendend(p1)

			if c1 == "h":
				p1.haymakerend(p2)
			if c2 == "h":
				p2.haymakerend(p1)

			if c1 == "k":
				p1.kamikazeend(p2)
			if c2 == "k":
				p2.kamikazeend(p1)

			#End passives
			await p1.endpassive()
			await p2.endpassive()

			#Endround
			await p1.endround()
			await p2.endround()

			#Death checks
			if p1.getHP() <= 0:
				await ctx.send(f"{u1.user.name}'s {p1.name} died")
				await u1.user.send(f"{u1.user.name}'s {p1.name} died")
				d1.append(t1.pop(t1.index(p1)))
				if len(t1) > 0:
					p1 = t1[0]


			if p2.getHP() <= 0:
				await ctx.send(f"{u2.user.name}'s {p2.name} died")
				await u2.user.send(f"{u2.user.name}'s {p2.name} died")
				d2.append(t2.pop(t2.index(p2)))
				if len(t2) > 0:
					p2 = t2[0]









def setup(bot):
	bot.add_cog(Battle(bot))









