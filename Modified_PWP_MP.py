#-----------------------------------------------------Bank Management System-----------------------------------------------------------------------------------
import mysql.connector
import os
import msvcrt
# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bankmsdb'
}

# Establish database connection
db_conn = mysql.connector.connect(**db_config)
cursor = db_conn.cursor()

# Create table if not exists
'''create_table_query = 
CREATE TABLE IF NOT EXISTS account2 (
    acno INT PRIMARY KEY,
    name VARCHAR(255),
    deposite INT,
    account_type CHAR(1),
    phone_no INT,
);

cursor.execute(create_table_query)
db_conn.commit()'''

#Account Class
class Account:
    #Constructor to initialize the instance variables 
    def __init__(self):
        self.acno = 0
        self.name = ""
        self.deposit = 0
        self.type = ""

    #Method for creating an account
    def create_account(self, no):
        self.acno = no
        self.name = input("\n\nEnter The Name of The account Holder : ")
        self.type = input("\nEnter Type of The account (C/S) : ").upper()
        self.deposit = int(input("\nEnter The initial amount: "))
        if self.deposit < 500:
            print("\n!!!Enable to create an account!!!\n")
            print("\nInitial amount should be greater than 500--\n ")
            self.deposit = int(input("\nAgain Enter The initial amount : "))
        print("\n\nYour account number is ",self.acno)
        print("\n\nAccount Created..\n\n")

    #Method for displaying an account
    def put_account(self):
        print(self.acno, "\t\t", self.name, "\t\t", self.deposit, "\t\t", self.type,"\t\t",self.phone)
    
    def retacno(self):
        return self.acno
    
    def retdeposit(self):
        return self.deposit

#Class object
a=Account()

#Method for adding an account
def add_account(m,p):
    ch = 'y'
    cursor.execute("SELECT * FROM account2")
    result = cursor.fetchall() # fetch all the account with their data
    result.reverse()
    for j in result[0]:
        break
    a.create_account(j+1)
    # Insert account into the database
    cursor.execute("INSERT INTO account2 (acno, name, deposite, account_type,phone_no, pass) VALUES (%s, %s, %s, %s,%s,%s)",
                       (a.acno, a.name, a.deposit, a.type,m,p))
    db_conn.commit()   # Close the database

#Method for displaying all accounts
def show_all():
    cursor.execute("SELECT * FROM account2")
    result = cursor.fetchall() # fetch all the account with their data
    #result.reverse()
    for i in result:
        print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
    
#Method for searching an account
def show_account():
    count=0
    name=input("Enter Customer's Full Name: ")
    # Check if account exists in the database
    cursor.execute("SELECT * FROM account2 WHERE name = %s", (name,))
    search = cursor.fetchall() # Fetch all the data of an account
    #search.reverse()    
    if search:
        print("-----------------------------------------------------------------------------------------------")
        print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
        print("-----------------------------------------------------------------------------------------------")
        for i in search:
            print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
            count+=1
        print("-----------------------------------------------------------------------------------------------")
        if count>1:
            ch=input("\n\nWant to search by Mobile number ? (y/n): ")
            if ch=='y': 
                pno=int(input("Enter Mobile Number: "))
                cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (pno,))
                phone_search = cursor.fetchall() # Fetch all the data of an account
                if phone_search:
                    print("-----------------------------------------------------------------------------------------------")
                    print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
                    print("-----------------------------------------------------------------------------------------------")
                    for i in phone_search:
                        print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
                    print("-----------------------------------------------------------------------------------------------")
                else:
                    print("\n!!!Account does not exist!!!--------\n\n")
            elif ch=='n':
                pass
            else:
                print("\nIncorrect Choice!!!\n\n")
    else:
        print("\n!!!Account does not exist!!!--------\n\n")

#Method to delete an account
def delete_account():
    count=0
    name=input("Enter Customer's Full Name: ")
    # Check if account exists in the database
    cursor.execute("SELECT * FROM account2 WHERE name = %s", (name,))
    search = cursor.fetchall() # Fetch all the data of an account    
    if search:
        print("-----------------------------------------------------------------------------------------------")
        print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
        print("-----------------------------------------------------------------------------------------------")
        for i in search:
            print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
            count+=1
        print("-----------------------------------------------------------------------------------------------")
        if count==1:
            c=input("\n\nAre you sure, you want to close this account ? (y/n): ")
            if c=="y":
                print("\n\nThe available balance of the account is ",search[0][2])
                b=0
                cursor.execute("UPDATE account2 SET deposit = %s WHERE phone_no = %s", (0, search[0][4]))   # Updating the account with new available balance
                db_conn.commit()    # Close the database
                print("\nThe amount has been withdrawn.\n")
                cursor.execute("DELETE FROM account2 WHERE phone_no = %s", (search[0][4],))
                db_conn.commit()   # Close the database
                print("\n--Account is Closed--\n\n")
            elif c=="n":
                pass
            else:
                print("\nIncorrect Choice!!!\n\n")
        elif count>1:    
            ch=input("\n\nWant to search by Mobile number ? (y/n): ")
            if ch=='y': 
                pno=int(input("Enter Mobile Number: "))
                cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (pno,))
                phone_search = cursor.fetchall() # Fetch all the data of an account
                if phone_search:
                    print("-----------------------------------------------------------------------------------------------")
                    print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
                    print("-----------------------------------------------------------------------------------------------")
                    for i in phone_search:
                        print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
                    print("-----------------------------------------------------------------------------------------------")
                    d=input("\n\nAre you sure, you want to close this account ? (y/n): ")
                    if d=="y":
                        print("\n\nThe available balance of the account is ",phone_search[0][2])
                        b=0
                        cursor.execute("UPDATE account2 SET deposite = %s WHERE phone_no = %s", (0, phone_search[0][4]))   # Updating the account with new available balance
                        db_conn.commit()    # Close the database
                        print("\nThe amount has been withdrawn.\n\n")
                        cursor.execute("DELETE FROM account2 WHERE phone_no = %s", (phone_search[0][4],))
                        db_conn.commit()   # Close the database
                        print("\n--Account is Closed--\n\n")
                    elif d=="n":
                        pass
                    else:
                        print("\nIncorrect Choice!!!\n\n")
                else:
                    print("\n!!!Account does not exist!!!--------\n\n")
            elif ch=='n':
                pass
            else:
                print("\nIncorrect Choice!!!\n\n")
    else:
        print("\n!!!Account does not exist!!!--------\n\n")

#Method for depositing amount
def deposite(p):
    amt = 0 
    cursor.execute("SELECT deposite FROM account2 WHERE phone_no = %s", (p,))
    rup = cursor.fetchone()  # Fetch the total amount of an account
        # Type of "rup" is tuple so converting tuple value into a new variable of type int
    for i in rup:         
        re=i
    print("\n\n\tTO DEPOSITE AMOUNT ")
    amt = int(input("\n\nEnter the amount to be deposited: "))
    res=re+amt   # Addition of available balance + new amount 
    cursor.execute("UPDATE account2 SET deposite = %s WHERE phone_no = %s", (res, p))  # Updating the account with new amount
    db_conn.commit()    # Close the database
    print("\n\n\tAmount Deposited\n")
    cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (p,))
    account = cursor.fetchall() # Fetch all the data of an account
    if account:
        print("-----------------------------------------------------------------------------------------------")
        print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
        print("-----------------------------------------------------------------------------------------------")
        for i in account:
            print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
        print("-----------------------------------------------------------------------------------------------") 

#Method for withdraw
def withdraw(p):
    amt=0
    # Check if account exists in the database
    cursor.execute("SELECT deposite FROM account2 WHERE phone_no = %s", (p,))
    rup = cursor.fetchone()   # Fetch the total amount of an account
    # Type of "rup" is tuple so converting tuple value into a new variable of type int
    for i in rup:
        re=i
    print("\n\n\tTO WITHDRAW AMOUNT ")
    amt = int(input("\n\nEnter the amount to be withdraw: "))
    bal = re - amt   # Substraction of withdrawable amount from the available balance
    b = re - 500
    # Check the balance is less than 500 or not
    if bal < 500:
           print("\nInsufficient balance!!!---\n")
           print("!!!You can withdraw ", b, " amount from Account!!!\n\n")
    else:
        cursor.execute("UPDATE account2 SET deposite = %s WHERE phone_no = %s", (bal, p))   # Updating the account with new available balance
        db_conn.commit()    # Close the database
        print("\nRecord Updated---\n\n")
        cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (p,))
        account = cursor.fetchall() # Fetch all the data of an account
        print("-----------------------------------------------------------------------------------------------")
        print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
        print("-----------------------------------------------------------------------------------------------")
        for i in account:
            print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
        print("-----------------------------------------------------------------------------------------------")

#Method for hiding password
def hide_pass(message):
    print(message, end='', flush=True)
    passwd = []
    while True:
        chh = msvcrt.getch()
        if ord(chh) == 10 or ord(chh) == 13:
            break
        if ord(chh) == 8:
            if len(passwd) > 0:
                passwd = passwd[:-1]
                print(f'\b \b', end='', flush=True)
        else:
            print("*", end="", flush=True)
            passwd.append(chr(ord(chh)))
    print("")  # Move to the next line
    return "".join(passwd)

#Main Method
def main():
    ch = 0
    num = 0
    au=0
    while au <=2 :
        print("\n----------------------------------------------------------")
        print("\n           Bank Management System   ")
        print("\n----------------------------------------------------------")
        print("\n\n\n\tMAIN MENU")
        print("\n\n\t01. Admin")
        print("\n\n\t02. Customer")
        au = int(input("\n\n\tSelect the type(1 or 2): "))
        os.system("cls")
        if(au==1):
            psw = hide_pass("Enter admin password: ")
            if(psw=="admin@123"):
                while ch <= 7:
                    os.system("cls")
                    print("\n----------------------------------------------------------")
                    print("\n           Bank Management System - Admin Panel   ")
                    print("\n----------------------------------------------------------")
                    print("\n\n\n\t\tMENU")
                    print("\n\n\t01. ALL ACCOUNT HOLDER LIST")
                    print("\n\n\t02. SEARCH AN ACCOUNT")
                    print("\n\n\t03. CLOSE AN ACCOUNT")
                    print("\n\n\t04. Log-Out")
                    ch = int(input("\n\n\tSelect Your Option (1-5): "))
                    os.system("cls")
                    if ch == 1:
                        print("-------------------------------------------------------------------------------------------------------")
                        print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
                        print("-------------------------------------------------------------------------------------------------------")
                        show_all()  
                        print("-------------------------------------------------------------------------------------------------------")
                        print("Press any key for main menu---")
                        input()
                    elif ch == 2:
                        show_account()  
                        print("Press any key for main menu---")
                        input()
                    elif ch == 3:
                        delete_account()  
                        print("Press any key for main menu---")
                        input()
                    elif ch == 4:
                        break
                    else:
                        print("\nIncorrect Choice!!!\n\n")
                        print("Press any key for main menu---")
                        input()
            else:
                print("\n\tPlease check password!!!")
                continue
        elif (au==2):
            u=0
            while u <= 3:
                print("\n----------------------------------------------------------")
                print("\n           Bank Management System - Customer Panel   ")
                print("\n----------------------------------------------------------")
                print("\n\n\n\t\tMENU")
                print("\n\n\t01. Create User/New account")
                print("\n\n\t02. Already have an account")
                print("\n\n\t03. Log-Out")
                u=int(input("\n\n\tSelect Your Option (1-2): "))
                if u==1:
                   phone=int(input("Enter your Mobile number: "))
                   cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (phone,))
                   at = cursor.fetchall()
                   if at:
                       print("\n\n!!!Duplicate number entry!!!\nPlease check the entered mobile number.")
                       continue
                   else:
                        user_psw = hide_pass("Create your account password: ")
                        confirm_psw = hide_pass("Confirm password: ")
                        if user_psw==confirm_psw:
                           print("\n\n----Enter your details to create an account----- ")
                           add_account(phone,confirm_psw)
                        else:
                           print("\n\n\tPlease check your password!!!")
                           continue
                elif u==2:
                        phoneno=int(input("Enter your Mobile number: "))
                        check_psw = hide_pass("Enter your account password: ")
                        cursor.execute("SELECT * FROM account2 WHERE phone_no = %s", (phoneno,))
                        account = cursor.fetchall()
                        if account:
                            print("-----------------------------------------------------------------------------------------------")
                            print("Account No.", "\t", "Name", "\t\t\t    ", "Balance", "\t    ", "Type","\t    ","Mobile Number")
                            print("-----------------------------------------------------------------------------------------------")
                            for i in account:
                                print("{:<15} {:<30} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4]))
                            print("-----------------------------------------------------------------------------------------------")
                            print("\n----------------------------------------------------------")
                            print("\n\n\n\t\t\t\tMENU")
                            print("\n----------------------------------------------------------")
                            print("\n\n\t01. DEPOSITE AMOUNT")
                            print("\n\n\t02. WITHDRAW AMOUNT")
                            c = int(input("\n\n\tSelect Your Option (1-2): "))
                            os.system("cls")
                            if c == 1:
                                deposite(phoneno)
                                break
                            elif c == 2:
                                withdraw(phoneno)
                                break
                            else:
                                print("\nIncorrect Choice!!!\n\n")
                                print("Press any key for main menu---")
                                input()       
                        else:
                            print("\n\n\t!!Incorrect password!!\n\n")
                            print("Press any key for retrying the password---")
                            input()
                elif u==3:
                    print("\n***Thank You for Banking with us***---------\n\n")
                    break
                else:
                    print("\nIncorrect Choice!!!\n\n")
                    print("Press any key for main menu---")
                    input()
        else:
            print("\nIncorrect Choice!!!\n\n")
            continue
            
            

main() #main method call
# Close database connection
db_conn.close()
#---------------------------------------------------------------------End of code---------------------------------------------------------------------------
