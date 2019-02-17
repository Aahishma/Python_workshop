from ask import ask # from ask module ask function is call
import readfile # whole readfile module is call
from random import randint # from random module randint function is call
rand = randint(1,100000000)# set random number for every time program runs
import calculation
def bill(totalAmount,TotalAmountDiscount , disc,a,date): # define a function to write bill Which accepts 3 parameter
    name = input("What is the name of buyer ? ")
    s = '============================================================================\n'
    s = s+"*****************************ABC Kathmandu*******************************\n"
    s = s+"                        contact number 987654321                            \n"
    s = s+ "                          New Road,Kathmandu                               \n\n\n"
    s = s+str(date)+"                    "+str(rand)+"\n\n"
    s = s+"buyer's Name "+name+"\n"
    s = s + "goods"+"\t"+"price"+"\t"+"quantity"+"\t\n"
    for i in range(len(a)):
        s = s + '\t'.join(a[i])+"\n"
    s = s+"\n\ngrand total "+ str(totalAmount)+"\n"
    if int(disc)!= 0:
        s = s+ "Discount given is "+str(disc)+"%\n"
    s = s+ "Total amount to pay %.00f"%TotalAmountDiscount+"\n\n\n"
    s = s+ "***************************************************************************\n"
    s = s+ "                Thank You for Purchase\n"
    s = s+'============================================================================\n'
    readfile.writefile("bill/"+name+" "+str(rand)+".txt",s)
    return str(s)
ans = True
aa = True
while ans == True: # to continue prodram untill the user wants it
    from datetime import datetime
    now =datetime.now()
    date = now.strftime("%c")
    print(readfile.fileread())
    a = ask()
    
    totalAmount,TotalAmountDiscount , disc= calculation.calculation(a)
    print(bill(totalAmount,TotalAmountDiscount , disc , a,date))
    Ask = input("Do you want to continue./n 'y' to continue and 'n' to exit program ")
    while aa == True: # To check the input of user
        try:
            if Ask == 'y' or Ask == 'yes' or Ask == 'Y' or Ask == 'Yes' or Ask == 'YES':
                ans = True
            elif Ask == 'n' or Ask == 'no' or Ask == 'No' or Ask == 'NO' or Ask == 'N':
                ans = False
            aa = False
        except:
            print("Invalid input")
    
        
        
        
