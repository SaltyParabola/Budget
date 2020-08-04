import gspread

gc = gspread.service_account(<path to google doc credentials>)


file_name = 'budget_py'

file = gc.open(file_name)
s1 = file.sheet1

class subacct:
	def __init__(self, name, lst, total):
		self.name = name
		self.total = total
		lst.append(self)
	def info(self):
		print(self.name + ', $' + str(self.total) + '\n')
		
class acct:
	def __init__(self, name, lst):
		self.name = name
		self.subs = lst
	def tot(self):
		self.total = 0
		for sub in self.subs:
			self.total += sub.total
		return(self.total)
	def info(self):
		print(self.name + ', $' + str(self.tot()) + '\n')
			


def transac(subacct, amount, desc, acct, dt):
	subacct.total += amount
	receipt = [dt, amount, desc, subacct.name, subacct.total, acct.name, acct.tot()]
	s1.append_row(receipt)

def transfer(subacctfrom, subacctto, amount, desc, acctfrom, acctto, dt):
	subacctfrom.total -= amount
	subacctto.total += amount
	receipt1 = [dt, -amount, desc, subacctfrom.name, subacctfrom.total, acctfrom.name, acctfrom.tot()]
	receipt2 = [dt, amount, desc, subacctto.name, subacctto.total, acctto.name, acctto.tot()]
	s1.append_row(receipt1)
	s1.append_row(receipt2)


check = []

travel = subacct('travel', check, 0)

school = subacct('school', check, 0)

necess = subacct('necess', check, 0)

car = subacct('car', check, 0)

subscrip = subacct('subscrip', check, 0)

general = subacct('general', check, 0)

checking = acct('checking', check)

sav = []

save = subacct('save', sav, 0)
give = subacct('give', sav, 0)

saving = acct('saving', sav)
