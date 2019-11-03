import sys

""" class atm
Handles basic transactions - withdraw, deposit and transfer.
Privileged transactions createacct and deleteacct are defunct in this class,
and exist only to be extended by the agent class.

class variables:
	account_list: list of account numbers
	summary: list of previous transactions in this session
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
	def __init__(self,accountList,summaryFile):
		self.account_list = accountList
		self.summary = summaryFile
		self.DEP_LIMIT = 200000
		self.WDR_LIMIT = 100000
		self.TRA_LIMIT = 1000000
		self.DAILY_LIMIT = 500000
		self.deleted_accounts = []
		return
		
	'''
	For depositing funds
	Will check whether the account and deposit amount are valid, and if
	the daily deposit limit has been met.
	Valid deposits will return a transaction string detailing the deposit.
	'''
	def deposit(self):
		while True:
			destAccount = self.askForAcct('Please enter the account number to deposit to: ')
			depAmount = self.askForMoney('Enter amount to deposit, in cents: ', self.DEP_LIMIT) 
			
			runningTotal = depAmount + self.getTransactionTotal(destAccount,"WDR")
			if runningTotal > self.DAILY_LIMIT:
				sys.stdout.write("You have exceeded the daily limit for deposits, " + self.DAILY_LIMIT + ", to this account. Please try again.\n")
				continue
			else:
				break
		sys.stdout.write('You have successfully deposited ' + str(depAmount) +' cents to account: '+destAccount)
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
		while True:
			sourceAccount = self.askForAcct('Please enter the account number to withdraw from: ')
			wdrAmount = self.askForMoney('Enter amount to withdraw, in cents: ', self.WDR_LIMIT)
			
			runningTotal = wdrAmount + self.getTransactionTotal(sourceAccount,"WDR")
			if runningTotal > self.DAILY_LIMIT:
				sys.stdout.write("You have exceeded the daily limit for withdrawals, " + self.DAILY_LIMIT + ", from this account. Please try again.\n")
				continue
			else:
				break

		sys.stdout.write('You have successfully withdrawn ' + str(wdrAmount) + ' cents from account: '+ sourceAccount)
		wdrString = 'WDR ' + '0000000' +  str(wdrAmount) + ' ' + str(sourceAccount) + ' ***'
		return wdrString
		
		
	'''
	For transferring funds from one account to another.
	Will check validity of both accounts involved along with the transfer amount,
	including whether the daily transfer limit has been met for the source account.
	Valid transfers will return a transaction string.
	'''
	def transfer(self):
		while True:
			sourceAccount = self.askForAcct('Please enter the account number to transfer from: ')
			destAccount = self.askForAcct('Please enter the account number to transfer to: ')
			traAmount = self.askForMoney('Enter amount to transfer, in cents: ', self.TRA_LIMIT)
			
			runningTotal = traAmount + self.getTransactionTotal(sourceAccount,"TRA")
			if runningTotal > (self.DAILY_LIMIT * 2):
				sys.stdout.write("You have exceeded the daily limit for transfers, " + (self.DAILY_LIMIT*2) + ", from this account. Please try again.\n")
				continue
			else:
				break

		sys.stdout.write('You have successfully transfered: ' + str(traAmount) + ' from account: ' + sourceAccount + 'to account: ' + destAccount)

		traString = 'TRA ' + str(destAccount) + ' ' + str(traAmount) + ' ' + str(sourceAccount) + ' ***'
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
	'''
	def askForAcct(self,prompt):
		while True:
			try:
				accountNum = raw_int(input(prompt))
			except:
				sys.stdout.write('Account numbers must be 7-digit numbers. Please try again.\n.')
				continue
			tempNum = str(accountNum)
			if len(tempNum) != 7 or tempNum[0] == '0':
				sys.stdout.write('Account numbers must be 7 digits long and cannot begin with 0. Please try again.\n')
				continue
			if tempNum not in self.account_list:
				sys.stdout.write('This account does not currently exist. Please try another account.\n')
			if tempNum  in self.deleted_accounts:
				sys.stdout.write('This account has been recently deleted. Please try another account.\n')
				continue
			break
		return tempNum
		
	'''
	A helper method that asks for an amount of money as input. Checks that the input
	is a number and is smaller than the provided transaction limit.
	'''
	def askForMoney(self,prompt,limit):
		while True:
			try:
				money = int(raw_input(prompt))
			except:
				sys.stdout.write('Your inputted amount contained non-numeric characters. Please try again.\n')
				continue
			if money > limit:
				sys.stdout.write('That amount is too large; maximum for this transaction is' + str(limit) +'. Please try again. \n')
				continue
			break
		return money
		
	'''
	A helper method that looks through all transactions processed in this session
	for the given account number and transaction type, returning the total that
	has been processed, to enable ehecks on daily transaction limits.
	
	account is the account number being checked
	type is the transaction type being checked against - WDR,DEP, or TRA
	'''
	
	def getTransactionTotal(self,account,type):
		total = 0
		file = open(self.summary,"r")
		for line in file:
			chunks = line.split(" ")#chop the line into its component words
			if chunks[0] == type:
				if type == "DEP":#for deposits, need the destination account
					cmp = chunks[1]
				else:#withdrawals and transfers use the source account
					cmp = chunks[3]
				if cmp == account:
					total = total + int(chunks[2])#if we match, add total
		return total

