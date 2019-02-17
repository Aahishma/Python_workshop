def fileread():#to read text file 
    file = open("inventory.txt","r")#this open the inventory file in read mode
    a = file.read()
    file.close()
    s = "   WELCOME TO OUR SHOP!!  \n"
    s = s +"   HOW MAY I HELP YOU ??  \n"
    s = s = s +"************************************\n"
    s = s+"product\tprice\tquantity\n"
    s = s + a
    s = s+"************************************"
    return s
def list():#read text file and store each line as object of list
    file = open("inventory.txt","r")
    a = file.readlines()
    file.close()
    return a
def iterate():# converts the output of list() to two dimensional list
    A = []
    for i in range (len(list())):
        A.append(list()[i].split())# 'split' inbuilt function to split string to list
    return A
def writefile(a,f): # this function writes a file. This function takes two parameters.
    file = open(a,"w")# this opens the file named a which is parameter of this function in write mode 
    file.write(f)
    file.close()


    
