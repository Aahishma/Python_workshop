import readfile # this import readfile module
def ask():# this function is to ask what customers need
    A = []
    list = readfile.iterate() # it calls the iterate function of readfile and store its return type in list
    ans = True
    while ans == True:# to run the loop if user want another product
        a = 0
        prod = input("What do you want to buy ? ")
        prod = prod.upper()# to ignore case sensative
        for i in range (len(list)):# to iterate through list
            if prod ==list[i][0]: # compare wheather the input product is in list or not
                
                amount = list[i][1]
                quantity = list[i][2]
                if int(quantity) == 0: # check wheather the quantity is zero
                      print("NO STOCk. Try another!")
                else:
                    ans = False
                    want = need(prod,quantity)# it calls need function by passing two parameter
                    newQuantity = int(list[i][2]) - int(want)
                    list[i][2] = str(newQuantity)# update the inventory list after change
                    if A == []:# check is list is empity
                        A.append([prod,amount,str(want)])# store product,amount and quantity in a list
                    else:
                        for j in A:
                            if j[0] == prod:
                                j[2]= str(int(j[2]) + want)
                            else:
                                A.append([prod,amount,str(want)]) # store product,amount and quantity in a list                           
            else:
                a += 1
                if a == len(list):
                    print("We dont have this product Try another.")
        BB = ''
        for i in list:
            AA ='\t'.join(i)+"\n"
            BB = BB + AA
        readfile.writefile("inventory.txt",BB)# it calls the writefile function of readfile module
            
        
        while ans == False:# to cotinue loop if user input wrong value
            try:# for exceptional handinling
                aa = input("Do you want to buy another thing. \n If yes press 'Yes' or 'y' and 'No' or 'n' to continue ")
                if aa == 'yes' or aa == 'Yes' or aa == 'YES' or aa == 'Y' or aa == 'y':
                    ans = True
                elif aa == 'N' or aa == "n" or aa == 'No' or aa == 'no' or aa == 'NO':
                    break
            except:
                print("press 'Yes' or 'No'")
    return A
def need(prod,quantity): # function toask need
    ans = True
    while ans == True:
        try:
            need = int(input("how many "+prod+" do you want to buy ? "))
            if need>int(quantity):
                print("We dont have that much product. Try another !")
            else:
                ans = False
        except:
            print("It shound be in number")
            ans = True
    return need

             
