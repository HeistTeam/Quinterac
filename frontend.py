import sys
import atm
import agent

""" class frontend
the main interface of the system.
Contains log in, log off, summary writer, and account writer.

class variables:
    account_list: list of account numbers
    summary: filename of transaction summary, type string
    mode: current machine mode, either 'atm' or 'agent'
"""

class frontend:
    """ class constructor
        set up the class variables, and call the main menu interface.
        
        parameters:
            account_list: filename of account list, type string
            summary_file: filename of transaction summary file, type string
    """
    def __init__(self, account_list, summary_file):
        self.account_list = self.account_list_reader(account_list)
        self.summary = summary_file
        self.login()

    """ login interface
        the main menu interface
    """
    def login(self):
        sys.stdout.write('Welcome to Quinterac Banking System.' + '\n')
        while True:
            sys.stdout.write('To start a session, please enter login.')
            i = raw_input('\n')
            if i == 'login':
                self.summary_writer('login')
                break
            
        i = raw_input('Please enter the type of banking today: agent or atm: ')
        if self.mode == 'agent':
            # agent class initization (self.account_list)
			session = agent(self.account_list)
            sys.stdout.write('Please enter the transaction you would like:' + '\n')
            sys.stdout.write('createacct, deleteacct, transfer, deposit, withdraw, logoff')
        elif self.mode == 'atm':
            # atm class initization (self.account_list)
			session = atm(self.account_list)
            sys.stdout.write('Please enter the transaction you would like:' + '\n')
            sys.stdout.write('transfer, deposit, withdraw, logoff')
            
        while True:
            i = raw_input('\n')
            if i == 'creatacct':
                create = session.createacct()
				if create != 0:
					self.summary_writer(session.createacct())
                pass
            elif i == 'deleteacct':
                destroy = session.deleteacct()
				if destroy != 0:
					self.summary_writer(session.deleteacct())
                pass
            elif i == 'transfer':
                self.summary_writer(session.transfer())
                pass
            elif i == 'deposit':
                self.summary_writer(session.deposit())
                pass
            elif i == 'withdraw':
                self.summary_writer(session.withdraw())
                pass
            elif i == 'logoff':
                self.logoff()
                break

    """ log off function
        closes the menu interface
    """
    def logoff(self):
        self.summary_writer('EOS')
        sys.stdout.write('Thank you for using Quinterac! Have a nice day!')
        sys.stdout.write('\n\n')
        # self.login()        

    """ summary writer function
        write a given string to the given summary file
        parameter:
            command: the string to be added to the summary
            summary: the filename of transaction summary file (default value: self.summary)
    """
    def summary_writer(self, command, summary = 0):
        if summary == 0:
            summary = self.summary
        file = open(summary, "a+")
        file.write(command)
        if command != 'EOS':
            file.write('\n')
        file.close()

    """ account list reader function
        reads the given file, and extract the bank account numbers and put
        them into a list
        parameter:
            filename: name of file to read from, type string
    """
    def account_list_reader(self, filename):
        acct_list = []
        file = open(filename, "r")
        for line in file:
            if line != "0000000":
                acct_list.append(line)
        file.close()
        return acct_list

# main function
def main():
    f = frontend(sys.argv[1], sys.argv[2])

# runs the main function if this module is ran
if __name__ == '__main__':
    main()
