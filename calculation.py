def calculation(A):# function to calculate amount 
    totalAmount = 0
    for i in A: # iterate through a list
        amount = int(i[1])*int(i[2])
        totalAmount += amount
    TotalAmountDiscount , disc  = discount(totalAmount)# cals discount function
    return totalAmount,TotalAmountDiscount , disc 
def discount(a):#function that calculate amount with discount
    ans = True
    while ans == True:# to continue loop untill the user input correct value
        try:
            ask = input("Do you want to give discount if yes press 'Yes' or 'Y' else press 'No' or 'N'")
            if ask == "Yes" or ask == "YES" or ask == "Y" or ask == 'y':
                disc = int(input("this is for seller \n How many discount do you want to give ? "))
                ans = False
                if disc > 100:
                    print("discount Percentage is not valid")
                    ans = True
            elif ask == "no" or ask == 'No' or ask == 'N' or ask == "n":
                disc = 0
                ans = False
            else:
                print("Type 'yes' or 'no'")
                ans = True
        except:
            print("discount shound be in number")
            ans = True
    TotalAmountDiscount = a - (a*disc)/100
    return TotalAmountDiscount , disc 


                

