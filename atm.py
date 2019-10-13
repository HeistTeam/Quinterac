import sys

""" class atm
Handles basic transactions - withdraw, deposit and transfer.
Privileged transactions createacct and deleteacct are defunct in this class,
and exist only to be extended by the agent class.

class variables:
	account_list: list of account numbers
	DEP_LIMIT: maximum deposit size for ATM mode
	WDR_LIMI: maximum withdrawal for ATM mode
	TRA_LIMIT: maximum transfer size for ATM mode
	DAILY_LIMIT: maxima for deposit to and withdrawal from one account in a shole
	session; also half of daily transfer limit

"""

class atm:
	"""class constructor
		sets up the class variables.
	"""
	def __init__(self,accountList):
		self.account_list = accountList
		self.DEP_LIMIT = 200000
		self.WDR_LIMIT = 100000
		self.TRA_LIMIT = 1000000
		self.DAILY_LIMIT = 500000
		return
		
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
		#here we set up the transaction string
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
	Stub methods for createacct and deleteacct.
	These operations are only available in agent mode.
	They exist here so that erroneous calls to them in ATM mode can be handled.
	'''
	def createacct(self):
		sys.stdout.write('That transaction is not available in ATM mode.')
		return 0
		
	def deleteacct(self):
		sys.stdout.write('That transaction is not available in ATM mode.')
		return 0
		
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

