#uhhhhhh spacer

b_dict = {'a':'42','b':'25','c':'25','d':'08'} #dict k = name v = percent

class bCalculate():
	def __init__(self,amount):
		self.amount = int(amount)
		self.split()

	def __repr__(self):
		return f'amount = {self.amount}'

	def split(self):
		for key, value in b_dict.items():
			sum = int(value)/100 * self.amount
			print(f'{key} owes ${str(round(sum))}')

arse = bCalculate('128')
