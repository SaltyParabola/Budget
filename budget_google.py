from datetime import datetime
import gspread

#lets you use Google Docs
gc = gspread.service_account(<PATH TO FILE WITH CREDENTIALS. NAME THAT FILE service_account>)


file_name = 'budget_py' # file name

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
			


def transac(subacct, amount, desc, acct):
	subacct.total += amount
	date = datetime.now().strftime('%Y-%m-%d')
	receipt = [date, subacct.name, desc, amount, subacct.total, acct.name, acct.tot()]

	file = gc.open(file_name).sheet1
	file.append_row(receipt)

def transfer(subacctfrom, subacctto, amount, desc, acct):
	subacctfrom.total -= amount
	subacctto.total += amount
	date = datetime.now().strftime('%Y-%m-%d')
	receipt1 = [date, subacctfrom.name, desc, -amount, subacctfrom.total, acct.name, acct.tot()]
	receipt2 = [date, subacctto.name, desc, amount, subacctto.total, acct.name, acct.tot()]

	file = gc.open(file_name).sheet1
	file.append_row(receipt1)
	file.append_row(receipt2)
