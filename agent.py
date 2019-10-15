import sys

""" class agent
This class handles all tranactions a user can make - create account, delete account
withdrawm deposit, and transfer.

class variables:
	account_list: list of account numbers
	DEP_LIMIT: maximum deposit size for agent mode
	WDR_LIMI: maximum withdrawal for agent mode
	TRA_LIMIT: maximum transfer size for agent mode
	DAILY_LIMIT: maxima for deposit to and withdrawal from one account in a single
	session; also half of daily transfer limit

"""
class agent:
	"""class constructor
		sets up the class variables.
	"""
	def __init__(self,accountList):
		self.account_list = accountList
		self.DEP_LIMIT = 99999999999
		self.WDR_LIMIT = 99999999999
		self.TRA_LIMIT = 99999999999
		self.DAILY_LIMIT = 99999999999
		return
	'''
	This is used to create a new account.
	It will check if the account number does not currently
	exist within the accountList.
	If it does not, then the account will be created.
	Valid accounts will be added to the transaction summary file.
	'''
	def createacct_1(self):
		newaccount  = raw_input('Please enter the account number for new account: ')
		newname = raw_input('Please enter the account name for new account: ')

		'''
		while True:
			if newaccount in accountList:
				sys.stdout.write('This account number already exists. Please try again ')
                pass
            break #If the account number does not exist  in account list, continue
		'''
		depString = "NEW " + str(newaccount) + ' ' + '***' + ' ' + '***' + str(newname)

		return 0

	'''
	This is used to delete an existing account.
	It will check if the account number does currently
	exist within the accountList.
	If it does, then the account will be deleted.
	Valid accounts will be added to the transaction summary file.
	'''
		
	def deleteacct(self):
		deleteaccount = self.askForAcct('Please enter the account number for the account you would like to delete: ')
		deletename = raw_input('Please enter the account name for the account you would like to delete: ')

		depString = 'DEL ' + str(deleteaccount) + ' ' + '***' + '***' + str(deletename)

		return 0 

	'''
	For depositing funds
	Will check whether the account and deposit amount are valid, and if
	the daily deposit limit has been met.
	Valid deposits will return a transaction string detailing the deposit.
	'''

	def deposit(self):
		destAccount = self.askForAcct('Please enter the account number to deposit to: ')
		depAmount = raw_input('Enter amount to deposit, in cents: ')
		'''
		while True:
			depAmount = raw_input('Enter amount to deposit, in cents: ')
			if depAmount > DEP_LIMIT:
				sys.stdout.write('That amount is too large; maximum deposit is' + str(self.DEP_LIMIT))
				pass
			break#If the amount is legal, keep going
		'''

		depString = 'DEP ' + str(destAccount) + ' ' +  str(depAmount) + ' ' + '0000000  ***'
		return depString
		
	'''
	For withdrawing funds
	Will check validity of source account number and withdrawal amount, and whether
	the daily withdrawal limit has been met.
	Valid withdrawals will return a transaction string.
	'''
	def withdraw(self):
		sourceAccount = self.askForAcct('Please enter the account number to withdraw from: ')
		wdrAmount = raw_input('Enter amount to withdraw, in cents: ')
		'''
		while True:
			wdrAmount = raw_input('Enter amount to withdraw, in cents: ')
			if wdrAmount > WDR_LIMIT:
				sys.stdout.write('That amount is too large; maximum withdrawal is' + str(self.WDR_LIMIT))
				pass
			break
		'''
		wdrString = 'WDR ' +  + '0000000' +  str(wdrAmount) + ' ' + str(sourceAccount) + ' ***'
		return wdrString
		
		
	'''
	For transferring funds from one account to another.
	Will check validity of both accounts involved along with the transfer amount,
	including whether the daily transfer limit has been met for the source account.
	Valid transfers will return a transaction string.
	'''
	def transfer(self):
		sourceAccount = self.askForAcct('Please enter the account number to transfer from: ')
		destAccount = self.askForAcct('Please enter the account number to transfer to: ')
		traAmount = raw_input('Enter amount to transfer, in cents: ')
		'''
		while True:
			traAmount = raw_input('Enter amount to transfer, in cents: ')
			if traAmount > TRA_LIMIT:
				sys.stdout.write('That amount is too large; maximum transfer is' + str(self.TRA_LIMIT))
				pass
			break
		'''
		traString = 'TRA ' + str(destAccount) + ' ' + str(traAmount) + ' ' + + str(sourceAccount) + ' ***'
		return traString
		
		
	'''
	A helper method that asks for an account number and checks for its existence
	in the account list.
	Or at least it will at some point!
	'''
	def askForAcct(self,prompt):
		while True:
			accountNum = raw_input(prompt)
			#if acctNum not in accountList, stop and ask again
			break
		return accountNum
		
	'''
	For future reference, have a method to take an acct number and transaction
	type and return total money moved by that transaction
	To test for daily limits
	'''
