import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="ranjith",password="TN120204009",database="test1")
print(mydb)
cursor=mydb.cursor()
def user(): #to create a new user
    name = input('enter your name:')
    account_no = int(input("enter your account number:"))
    passcode=input("enter your password:")
    cnm_passcode=input("confirm your password:")
    if(name==""):
        print("name is missing")
        exit()
    if passcode=="":
        print("enter password")
        exit()
    if cnm_passcode!=passcode:
        print("password does not match")   
        exit()
    cursor.execute('select * from user_account_details')
    datacheck=cursor.fetchall()
    len_users=cursor.rowcount
    table_name="user"+str(len_users+1)
    bene_table_name="bene"+str(len_users+1)      
    sql = 'INSERT INTO user_account_details (name,passcode,account_no,table_used,bene_table_used) VALUES(%s,%s,%s,%s,%s)'
    val=(name,passcode,account_no,table_name,bene_table_name)
    print(val)
    cursor.execute(sql, val)
    
    sql='create table {tab}(TRANSACTION_DATE date,DESCRIPTION varchar(100),DEBIT_CREDIT varchar(10),AMOUNT float(20,5),BALANCE float(20,5))'.format(tab=table_name)
    cursor.execute(sql)
    sql='create table {tab}(BENEFICIARY_NAME char(30),NICKNAME CHAR(10),ACCOUNT_NO int(30),NAME_OF_THE_BANK char(30),BRANCH char(30),IFSC_CODE varchar(12),CONFIRMATION_STATUS char(20))'.format(tab=bene_table_name)
    cursor.execute(sql)
    mydb.commit()
def login():#used to login 
    global username
    username=(input("enter your name:"))
    password=input("enter your password")
    cursor.execute("select name,passcode,account_no,table_used,bene_table_used from user_account_details ")
    datacheck=cursor.fetchall()
    len_users=cursor.rowcount
    print(len_users)
    for row in datacheck:
        if username==row[0]:
            if password==row[1]:
                print("login complete")
                global acc_no
                global bene_tab
                global user_tab
                acc_no=row[2]
                user_tab=row[3]
                bene_tab=row[4]
                
               
            else:
                print("password incorrect")
                print("please try again")
        elif username=="":
            print("name not found")
            ans=input("Do you want to create a new user(Y/N)")
            if ans=="y":
                print("place users function here")#do not forget it and erase the comment when finished
            else:
                exit()
        elif username!=row[0]:
            continue
def transfer(transfer_amount, source_account_num, target_account_num):#to transfer amount from one user to another
    cursor.execute("update ACCOUNT set BALANCE = BALANCE - %s where ACCOUNT_NUM = %s", (transfer_amount, source_account_num))
    cursor.execute("update ACCOUNT set BALANCE = BALANCE + %s where ACCOUNT_NUM = %s", (transfer_amount, target_account_num))
    cursor.close()
    #yet to be finished
#program starts here
print("Welcome to Bank of India")
print("If you want to create a new user select 1")
print("Registered users select 2")
choice=int(input(">>"))
if choice==1:
    user()
elif choice==2:
    login()#if user logins continues to functions else exits 
    print("Welcome",username)
    print("1.NEFT Transaction")
    print("2.IMPS Transaction")
    print("3.RTGS Transaction")
    print("4.Transaction Details")
    print("5.Add/Remove Beneficiaries")
    print("6.Show Beneficiaries")
    choiceuser=int(input(">>"))
    if choiceuser==1:
        transfer_amount=int(input("enter the amount to be transferred"))
        source_account_num=acc_no
        sql='select * from {tab}'.format(tab=bene_tab)
        cursor.execute(sql)
        datacheck=cursor.fetchall()
        print(datacheck)
        #yet to be finished        
    elif choiceuser==2:
        transfer_amount=int(input("enter the amount to be transferred"))
        source_account_num=acc_no
        sql='select * from {tab}'.format(tab=bene_tab)
        cursor.execute(sql)
        datacheck=cursor.fetchall()
        print(datacheck)
         #yet to be finished 
    elif choiceuser==3:
        transfer_amount=int(input("enter the amount to be transferred"))
        source_account_num=acc_no
        sql='select * from {tab}'.format(tab=bene_tab)
        cursor.execute(sql)
        datacheck=cursor.fetchall()
        print(datacheck)
         #yet to be finished 
    elif choiceuser==4:
        sql='select * from {tab}'.format(tab=user_tab)
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
         #yet to be finished 
    elif choiceuser==5:
        username=input("enter the beneficiary name : ")
        nickname=input("enter the nickname : ")
        ben_acc_no=int(input("enter beneficiary account number : "))
        bank_name=input("enter bank name : ")
        branch=input("enter the branch : ")
        ifsc_code=input("IFSC code : ")
        confirmation_status="waiting"
         #yet to be finished 
    elif choiceuser==6:
        sql='select * from {tab}'.format(tab=bene_tab)
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data) 
        #yet to be finished
    else:
        print("invalid selection")
        exit()
else:
    exit()