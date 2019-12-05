import sys
import atm
""" class agent
This class handles all tranactions a user can make - create account, delete account
withdrawm deposit, and transfer.

class variables:
	account_list: list of account numbers
	summary: list of previous transactions in this session
	DEP_LIMIT: maximum deposit size for agent mode
	WDR_LIMI: maximum withdrawal for agent mode
	TRA_LIMIT: maximum transfer size for agent mode
	DAILY_LIMIT: maxima for deposit to and withdrawal from one account in a single
	session; also half of daily transfer limit

"""
class agent(atm.atm):
	"""class constructor
		sets up the class variables.
	"""
	def __init__(self,accountList,summaryFile):
		self.account_list = accountList
		self.summary = summaryFile
		self.DEP_LIMIT = 99999999
		self.WDR_LIMIT = 99999999
		self.TRA_LIMIT = 99999999
		self.DAILY_LIMIT = 99999999
		self.deleted_accounts = []
		return
	'''
	This is used to create a new account.
	It will check if the account number does not currently
	exist within the accountList.
	If it does not, then the account will be created.
	Valid accounts will be added to the transaction summary file.
	'''
	def createacct(self):
		newaccount  = self.askForNewAcct('Please enter the account number for new account: ')
		newname = self.askForName('Please enter the account name for new account: ') 

		depString = "NEW " + str(newaccount) + ' ' + '***' + ' ' + '*** ' + str(newname)

		sys.stdout.write('New account created with account number: ' + newaccount + ' and account name: ' + newname)

		return depString

	'''
	This is used to delete an existing account.
	It will check if the account number does currently
	exist within the accountList.
	If it does, then the account will be deleted.
	Valid accounts will be added to the transaction summary file.
	'''
		
	def deleteacct(self):
		deleteaccount = self.askForDelAcct('Please enter the account number for the account you would like to delete: ')
		deletename = self.askForName('Please enter the account name for the account you would like to delete: ')

		depString = 'DEL ' + str(deleteaccount) + ' ' + '*** ' + '*** ' + str(deletename)

		self.deleted_accounts.append(deleteaccount)

		sys.stdout.write('Account deleted with account number: ' + deleteaccount + ' and account name: ' + deletename)

		return depString 
	'''
	A helper method that asks for an account number and compares it to account list
	to determine if it is unique and does not currently exist.
	'''
	def askForNewAcct(self,prompt):
		while True:
			try:
				accountNum = int(input(prompt))
			except:
				sys.stdout.write('Account numbers must be 7-digit numbers. Please try again.\n.')
				continue
			accountNum = str(accountNum)
			if len(accountNum) != 7 or accountNum[0] == '0':
				sys.stdout.write('Account numbers must be 7 digits long and cannot begin with 0. Please try again.\n')
				continue
			if accountNum in self.account_list:
				sys.stdout.write('This account currently exists. Please enter a new unique account number.\n')
				continue
			if accountNum in self.deleted_accounts:
				sys.stdout.write('This account has been recently deleted. Please enter a new unique account number.\n')
				continue
			break
		return accountNum
	'''
	A helper method that asks for an account number to delete and checks for its existence in account list.
	'''
	def askForDelAcct(self,prompt):
		while True:
			try:
				accountNum = int(input(prompt))
			except:
				sys.stdout.write('Account numbers must be 7-digit numbers. Please try again.\n.')
				continue
			accountNum = str(accountNum)
			if len(accountNum) != 7 or accountNum[0] == '0':
				sys.stdout.write('Account numbers must be 7 digits long and cannot begin with 0. Please try again.\n')
				continue
			if accountNum not in self.account_list:
				sys.stdout.write('This account does not currently exist. Please try another account.\n')
				continue
			if accountNum in self.deleted_accounts:
				sys.stdout.write('This account has already been deleted. Please try another account.\n')
				continue
			break
		return accountNum
	'''
	A helper method that asks for an account name and validates various checks.
	'''
	def askForName(self,prompt):
		while True:
			accountName = input(prompt)
		
			if len(accountName) < 3 or len(accountName) > 30:
				sys.stdout.write('Account Name must be between 3 and 30 digits long. Please try again.\n')
				continue
			if accountName[0] == " " or accountName[-1] == " ":
				sys.stdout.write('Account Name cannot start or end with an empty space value. Please try again.\n')
				continue
			break
		return accountName

