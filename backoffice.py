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
        self.account_writer(account_list, True)
        self.account_writer('account_list.txt', False)
        
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
            if line.startswith("0") :
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
            lines = str(line)
            lines = lines.split(' ')
            if lines[0] == 'EOS' or lines[0] == 'login':
                continue
            else:
                if lines[0] == 'DEP':
                    self.deposit(lines[1], lines[2])
                elif lines[0] == 'WDR':
                    self.withdraw(lines[1], lines[2])
                elif lines[0] == 'XFR':
                    self.transfer(lines[1], lines[2], lines[3])
                elif lines[0] == 'NEW' and len(lines) >= 5:
                    self.createacct(lines[1], lines[4])
                elif lines[0] == 'DEL' and len(lines) >= 5:
                    self.deleteacct(lines[1], lines[4])

    """ account writer function
        rewrites the account list using the current class variable list
        parameters:
        filename: string holding the name of file to write to
        includeall: boolean indicating if all information is to be added
        (i.e. balances and account names)
    """
    def account_writer(self, filename, includeall):
        file = open(filename, "w")
        account_list = []
        self.account_list.sort(key=lambda x: x[0])
        for x in range(len(self.account_list)):
            if includeall == True:
                account_list.append(' '.join(self.account_list[x]))
            elif includeall == False:
                account_list.append(self.account_list[x][0])
        account_list.append("0000000")
        account_list = '\n'.join(account_list) 
        file.write(account_list)
        
    def createacct(self, number, name):
        name = name.strip('\n')
        self.account_list.append([number, "000", name])
        pass

    def deleteacct(self, number, name):
        for count, account in enumerate(self.account_list):
            if account[0] == number:
                self.account_list.pop(count)
        pass

    def deposit(self, number, balance):
        pass

    def withdraw(self, number, balance):
        self.deposit(number, - int(balance))

    def transfer(self, numberfrom, balance, numberto):
        pass

# main function                
def main():
    f = backoffice(sys.argv[1], sys.argv[2])

# runs the main function if module is ran
if __name__ == '__main__':
    main()
