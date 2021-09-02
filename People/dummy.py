from Character import Character

class Dummy(Character):
	def __init__(self):
		super().__init__("Dummy", title="Dummy", hp=2000, attack=400, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2, srec = 0)

class Dummy2(Character):
	def __init__(self):
		super().__init__("Dum", title="Dummy", hp=2000, attack=400, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2, srec = 0)

class Dummy3(Character):
	def __init__(self):
		super().__init__("Dumdum", title="Dummy", hp=2000, attack=4000, dodge=10, crit=20, defense=20,
                         gender=0, critValue=2, srec = 0)

