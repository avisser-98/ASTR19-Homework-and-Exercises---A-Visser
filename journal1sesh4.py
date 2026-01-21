class Clown:
	eyes=int(2)
	tail = bool(False) #boolian is a True/False statement, 1=True, 2=False
	furry = bool(False)

	def __init__(self, leg_length, arm_length, name): #__init__ 
		self.leg_length = float(leg_length) # unique, in inches
		self.arm_length = float(arm_length) # unique, in inches
		self.name = str(name)

	def honk_honk(self):
		# introduction to what a clown is
		print("Honk honk! I'm a Clown! My name is " + self.name + "!")
		print("I have " + str(self.eyes) + " eyes.")
		if self.tail == False:
			print("I have no tail!")
		if self.furry == False:
			print("I am not furry!")
		print("My arms are " + str(self.arm_length) + " inches long.")
		print("My legs are " + str(self.leg_length) + " inches long.")
		return "Honk honk!"

Harlan = Clown(4, 4, "Harlan")
print(Clown.honk_honk(Harlan))