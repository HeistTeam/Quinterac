import sys

""" class backend
the back end of the system.
Contains log in, log off, summary writer, and account writer.

class variables:
    account_list: two dimensional list of accounts. including account number, account balance,
        account name, in that order.
"""

class backoffice:
    """ class constructor
        set up the class variables, and call the main menu interface.
        
        parameters:
            account_list: filename of account list, type string
            summary_file: filename of transaction summary file, type string
    """
    def __init__(self, account_list, summary_file):
        self.account_list = self.account_list_reader(account_list)
        self.summary_reader(summary_file)
        self.account_writer(summary_file)
        
    """ account list reader function
        reads the given file, and extract the account numbers, account balances,
        accound names, and put them into a 2D list
        parameter:
            filename: name of file to read from, type string
    """    
    def account_list_reader(self, filename):
        acct_list = []
        file = open(filename, "r")
        for line in file:
            line = line[:-1]
            if line == '0000000':
                break
            acct_list.append(line.split(' '))
        file.close()
        return acct_list
    
    """ summary reader function
        reads the given summary file
        parameter:
            filename: name of merged transaction summary file
    """
    def summary_reader(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line[:1]
            if line == 'EOS' or line == 'login':
                continue
            else:
                line = line.split(' ')
                if line[0] == 'DEP':
                    self.deposit(line[1], line[2])
                elif line[0] == 'WDR':
                    self.withdraw(line[1], line[2])
                elif line[0] == 'XFR':
                    self.transfer(line[1], line[2], line[3])
                elif line[0] == 'NEW':
                    self.createacct(line[1], line[2])
                elif line[0] == 'DEL':
                    self.deleteacct(line[1], line[2])

    """ account writer function
        rewrites the account list using the current class variable list
    """
    def account_writer(self, filename):
        file = open(filename, "w")
        account_list = []
        for x in range(len(self.account_list)):
            account_list.append(' '.join(self.account_list[x])) 
        account_list = '/n'.join(account_list) 
        file.write(account_list)
            
    def createacct(self, number, name):
        pass

    def deleteacct(self, number, name):
        pass

    def deposit(self, number, balance):
        pass

    def withdraw(self, number, balance):
        self.deposit(number, -balance)

    def transfer(self, numberfrom, balance, numberto):
        pass

# main function                
def main():
    f = backoffice(sys.argv[1], sys.argv[2])

# runs the main function if module is ran
if __name__ == '__main__':
    main()
