import gspread

gc = gspread.service_account('<full path to .json google credentials. make sure that file is named service_account>')

#file name
file_name = 'budget_py'

file = gc.open(file_name)
s1 = file.get_worksheet(0)

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

# initialize list for first main account
check = []

# initialize all sub accounts with default value
school = subacct('school', check, 0)
necess = subacct('necess', check, 0)
car = subacct('car', check, 0)
subscrip = subacct('subscrip', check, 0)
general = subacct('general', check, 0)

#initialize first main account with input of list from above
checking = acct('checking', check)


#do the same for all other accounts
sav = []

save = subacct('save', sav, 0)
give = subacct('give', sav, 0)
reserve = subacct('reserve', sav, 0)

saving = acct('saving', sav)
