#importing the dependencies
import mysql.connector as sq
import matplotlib.pyplot as plt
import pandas as pd
import csv

#setting up the dicts to be used in the program for retrieving ids and file names
comp_names = ["Equity Name :  Equity Code",
              "Mahindra & Mahindra Financial Services Limited , BSE : MMT",
              "Reliance Industries Limited , NSE : RIL",
              "Aditya Birla Capital Limited , NSE : ABC",
              "Tata Consultancy Services Limited , BSE : TCS",
              "LIC Housing Finance Limited , BSE : LIC"]

comp_names_dict = {'MMT': 'Mahindra & Mahindra Financial Services Limited',
                   'RIL': 'Reliance Industries Limited',
                   'ABC': 'Aditya Birla Capital Limited',
                   'TCS': 'Tata Consultancy Services Limited',
                   'LIC': 'LIC Housing Finance Limited'}

comp_ids_csv = {'MMT': 'M&MFIN.BO.csv',
                'RIL': 'RELIANCE.NS.csv',
                'ABC': 'ABCAPITAL.NS.csv',
                'TCS': 'TCS.BO.csv',
                'LIC': 'LICHSGFIN.BO.csv'}

comp_ids = {'MMT': 'M&MFIN.BO',
            'RIL': 'RELIANCE.NS',
            'ABC': 'ABCAPITAL.NS',
            'TCS': 'TCS.BO',
            'LIC': 'LICHSGFIN.BO'}


#function for adding new users to the user id database
def uss_datb(xaa, ybb):
    hq_uss = sq.connect(host='localhost', user='root', passwd='root', database= 'user_id_data')
    cus_uss = hq_uss.cursor()

    cus_uss.execute("INSERT INTO USERS VALUES(%s, %s)", (xaa, ybb,))
    hq_uss.commit()
    hq_uss.close()

#fucntion to check for if the password entered during the login is correct or not
def pass_check(xa, yb):
    hq_pass = sq.connect(host='localhost', user='root', passwd='root', database='user_id_data')
    cus_pass = hq_pass.cursor()
    cus_pass.execute("SELECT * FROM USERS WHERE username = %s  AND password = %s", (xa, yb,))
    data = cus_pass.fetchone()
    if data is None:
        print("Wrong Credentials, Try again")      #in case the data is a none type which can happen only if the credentials were wrong
    else:
        val = 1
        return val            #when the credentials are correct this val counter used in a while loop below will break the loop
    hq_pass.close()

#function to set up database and tables for a new user
def new_user():
    #to create a new database
    hq_newuser = sq.connect(host='localhost', user='root', passwd='root')
    cus_newuser = hq_newuser.cursor()

    username = input('Enter a username: ')
    password = input('Enter a password: ')

    database_create = "CREATE DATABASE " + username
    cus_newuser.execute(database_create)
    hq_newuser.close()

    #this is for adding the tables in the newly created database
    hq_newuser2 = sq.connect(host='localhost', user='root', passwd='root', database = username)
    cus_newuser2 = hq_newuser2.cursor()

    #this table is for the current shares the user holds
    cus_newuser2.execute("CREATE TABLE CURRENT_SHARES(SHARE_ID CHAR(20), COMPANY_NAME VARCHAR(50), NUMBER_OF_SHARES INT(5),SHARE_PRICE DECIMAL(10,4) ,SHARE_BOUGHT_FOR DECIMAL(10,4))")

    #this table is for the shares the user sold
    cus_newuser2.execute("CREATE TABLE TRANSACTION_HISTORY(SHARE_ID CHAR(20), COMPANY_NAME VARCHAR(50), SHARE_SOLD_AT DECIMAL(10,4) ,NUMBER_OF_SHARES_SOLD INT(5),RETURNS DECIMAL(10,4))")

    hq_newuser2.close()
    uss_datb(username, password)

    print("Database has been registered, please enter the newly created credentials again")  #giving the final output

#function to get the latest share price from the csv files
def get_cost(a):
    f = open(a, 'r')
    c = csv.reader(f)       #opening and then reading the file specified in the argument
    list2 = []
    next(c)

    for itt in c:
        list2.append(itt[4])       #appending the share prices to a list

    list2.reverse()                #reverse sort the list and slice the first element to get the last price
    co = list2[0]
    return float(co)

#function to get the share at which an existing share was brought which will be used for entry in transaction history
def get_og_share_price(y):

    idd = comp_ids[y]
    cus.execute("SELECT SHARE_BOUGHT_FOR FROM CURRENT_SHARES WHERE SHARE_ID = %s ", (idd,))
    data = cus.fetchone()
    list3 = []
    for ik in data:
        list3.append(float(ik))     #appending to a list and taking the first element

    og_cost = list3[0]
    return og_cost

#function to get returns if a share is to be sold
def returns(y):
    y1 = comp_ids_csv[y]
    curr_cost = get_cost(y1)          #using get cost to get the current share price
    idd = comp_ids[y]
    cus.execute("SELECT SHARE_PRICE FROM CURRENT_SHARES WHERE SHARE_ID = %s ", (idd,))
    data = cus.fetchone()
    list3 = []
    for ik in data:
        list3.append(float(ik))         #appending the values and taking out the first element

    og_cost = list3[0]
    diff = float(curr_cost - og_cost)    #calculating the returns
    return diff

#function to connect the user's dmat account to get the bank balance
def bank_connection(a, b):
    hq_bank = sq.connect(host='localhost', user='root', passwd='root', database='dmat')
    cus_bank = hq_bank.cursor()

    cus_bank.execute("SELECT BALANCE FROM USERS WHERE USERID = %s AND PIN = %s", (a, b,))
    bal = cus_bank.fetchone()
    list1 = []
    for d in bal:
        list1.append(float(d))

    bank_bal = list1[0]        #appending values to the list and taking the first element which will be the balance
    hq_bank.close()
    return bank_bal

#function to update bank balance after selling and buying shares
def update_bal():
    hq_bal = sq.connect(host='localhost', user='root', passwd='root', database='dmat')
    cus_bal = hq_bal.cursor()
    cus_bal.execute("UPDATE users SET BALANCE = %s WHERE USERID = %s", (dmat_balance, bank_uss))
    hq_bal.commit()
    hq_bal.close()

#function to show graphs of the stock prices of the specified equity
def show_graph():

    print("The list of available companies are:")
    print("Please enter the company code to view the chart")


    inp_5 = input('').upper()
    comp_id = comp_ids_csv[inp_5]   #getting the csv file
    g = pd.read_csv(comp_id, index_col=0, parse_dates=True)      #we parse the date stamps for the x axis

    g['Adj Close'].plot()   #plotting the graph
    plt.show()


#here we take the bank details for the dmat account balance
print("Enter your bank details for DMAT account connection to continue")
bank_uss = int(input('Enter your LOGIN_ID: '))
bank_pin = int(input("Enter your account PIN: "))

dmat_balance = bank_connection(bank_uss, bank_pin)

print("...")
print()
print("Sucessfully connected your bank account")
print()
print()
print()


#this is now for setting up the database for the user
user_check = input("Login(1) Or SignUp(2)? : ")

#when the user has a database already
if user_check == "1":
    val = 0
    while val == 0:      #this is looped in order to let the user enter the credentials again if they are entered wrong
        uss = input("Enter your username: ")
        pas = input("Enter your password: ")
        val = pass_check(uss, pas, )        #this is used for checking the password with the username

#when the user has to make a new database
elif user_check == "2":
    new_user()
    print()
    print()
    val = 0
    while val == 0:  #this is also looped in order to let the user enter the credentials again if they are entered wrong
        uss = input("Enter your username: ")
        pas = input("Enter your password: ")
        val = pass_check(uss, pas,)


#connecting to the database of the specified user
hq = sq.connect(host = 'localhost', user = 'root', passwd = 'root', database = uss)
cus = hq.cursor()

print()
print()
print()

#the main program now begins
while True:

    #loop is used to make it easier for the user to handle multiple tasks in one go
    #the available choices are displayed for the user
    print("What do you want to do?")

    print()
    print()

    print("Enter B TO BUY")
    print("Enter I to show company IDs")
    print("Enter S TO SELL")
    print("Enter V TO view stock chart")
    print("Enter T To show tables")
    print("Enter D to show bank balance")
    print("Enter E to exit")
    print()

    #asking the user to enter what task to do
    inp_1 = input(">").lower()

    #directly used the show graph function here
    if inp_1 == "v":
        show_graph()

    #using for loop to show company ids which will be needed to be entered by the user in the next other options
    elif inp_1 == 'i':
        for i in comp_names:
            print(i)

    #for when the user wants to buy shares
    elif inp_1 == "b":

        inp_6 = input('Enter the company ID of whose shares are to be bought: ').upper()
        print()
        comp_buy = comp_ids_csv[inp_6]
        vol = int(input("How many shares: "))

        cost = get_cost(comp_buy)
        t_cost = round(vol*cost, 4)   #calculating the total price that would be cut from the bank account
        sp_1 = round(get_cost(comp_ids_csv[inp_6]), 4)
        print()
        print("Share price is ", cost)
        print("Total Cost is: ", t_cost)
        print()

        #this is for if the total price is more than what the user has in the bank
        if t_cost > dmat_balance:
            print()
            print("Insufficient funds")


        else:
            print("Your account balance is ", dmat_balance, ", are you sure you want to proceed?")
            inp_2 = input(">").lower()      #getting the final confirmation from the user
            if inp_2 == "yes":
                id_1 = comp_ids[inp_6]
                id_2 = comp_names_dict[inp_6]              #setting values to be entered in the table
                cus.execute("INSERT INTO CURRENT_SHARES VALUES(%s, %s, %s, %s, %s)", (id_1, id_2, vol, sp_1, t_cost,))
                hq.commit()
                dmat_balance = round(dmat_balance - t_cost, 4)   #updating the bank balance after the shares have been bought

    #for when the user wants to sell shares
    elif inp_1 == "s":
        comp_sell = input("Enter the company ID whose shared are to be sold: ").upper()
        count = int(input("How many shares are to be sold: "))
        re = returns(comp_sell)
        rounded_re = round(re, 4)             #rounding the returns according to the table's returns data type
        t_rounded_re = rounded_re*count       #totalling the returns for the number of shares bought
        sp_2 = get_og_share_price(comp_sell)   #this is the previous cost at which the shares were bought
        ss_a = round(get_cost(comp_ids_csv[comp_sell]), 4)   #to get the latest cost of share
        print()
        print("The returns are: ", rounded_re)

        id_3 = comp_ids[comp_sell]
        id_4 = comp_names_dict[comp_sell]

        #adding record to the transaction history and deleting the sold share from the current shares table
        cus.execute("INSERT INTO TRANSACTION_HISTORY VALUES(%s, %s, %s, %s, %s)", (id_3, id_4, ss_a, count, t_rounded_re,))
        cus.execute("DELETE FROM CURRENT_SHARES WHERE SHARE_ID = %s", (id_3,))
        hq.commit()
        dmat_balance = round(dmat_balance + sp_2 + t_rounded_re, 4)       #updating the bank balance after shares have been sold

    #for when the user wants to view both the tables
    elif inp_1 == "t":
        cus.execute("SELECT * FROM CURRENT_SHARES")
        r1 = cus.fetchall()
        print("Your Current Shares; ")                       #printing the current shares table
        print()

        for i in r1:
            print(i)
        cus.execute("SELECT * FROM TRANSACTION_HISTORY")
        r2 = cus.fetchall()
        print("Your Transaction History; ")                     #printing the transaction history
        print()

        for k in r2:
            print(k)

        inp_4 = input("Would like to see the returns?(yes/no): ").lower()
        if inp_4 == "yes":
            inp_7 = input("Enter company ID: ").upper()
            x = returns(inp_7)
            print(x)

    #for when the user wants to view the bank balance
    elif inp_1 == 'd':
        print("Your dmat balance is: ")
        print(dmat_balance)


    #for when the user wants to exit the application
    elif inp_1 == 'e':

        hq.close()
        update_bal()      #closing the sql connection, updating the bank balance and breaking the loop
        break

