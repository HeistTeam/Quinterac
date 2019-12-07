import frontend
import backoffice

def main():
    counter = 0
    while (counter < 3):
        counter += 1
        frontend.frontend('account_list.txt', 't_s_'+str(counter)+'.txt')
        if counter >= 3:
            concatfile('t_s_', 3)
            backoffice.backoffice('master_account_list.txt', 'merged_transaction.txt')
            counter = 0
            file = open('merged_transaction.txt', 'w+')
            file.close()
            break
            
def concatfile(filename, filenumber):
    file = open('merged_transaction.txt', 'a+')
    for i in range (1, filenumber + 1):
        if (i != 1):
            file.write('\n')
        file2 = open(filename + str(i) + '.txt', 'r+')
        for line in file2:
            file.write(line)
        file2.close()
        file3 = open(filename + str(filenumber) + '.txt', 'w+')
        file3.close()
    file.write('\n')
    file.write('EOS')
    file.close()

if __name__ == '__main__':
    main()
