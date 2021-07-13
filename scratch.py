#uhhhhhh spacer

b_dict = {'dylan':'42','alex':'25','todd':'25','rickey':'08'} #dict k = name v = percent

class bCalculate():
	def __init__(self,amount):
		self.amount = int(amount)
		self.split()

	def __repr__(self):
		return f'amount = {self.amount}'

	def split(self):
		verify = []
		sum = 0
		for key, value in b_dict.items():
			sum = int(value)/100 * self.amount
			verify.append(round(sum))
			print(f'{key} owes ${str(round(sum))}')

arse = bCalculate('128')
#print(arse)
