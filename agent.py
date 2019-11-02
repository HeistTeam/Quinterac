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
		return
	'''
	This is used to create a new account.
	It will check if the account number does not currently
	exist within the accountList.
	If it does not, then the account will be created.
	Valid accounts will be added to the transaction summary file.
	'''
	def createacct(self):
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
		deleteaccount = self.askForAcct('Please enter the account number for the account you would like to delete: ')
		deletename = raw_input('Please enter the account name for the account you would like to delete: ')

		depString = 'DEL ' + str(deleteaccount) + ' ' + '***' + '***' + str(deletename)

		sys.stdout.write('Account deleted with account number: ' + deleteaccount + ' and account name: ' + deletename)

		return depString 
