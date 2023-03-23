import webbrowser
import mysql.connector
import os,time
os.system('cls')

conn = mysql.connector.connect(user="root", passwd= "123456",host="localhost",database='hosp_finder',auth_plugin='mysql_native_password')
list_hosp=[]

def get_hosp(loc):
    os.system('cls')
    x1 = """SELECT hosp_Name,hosp_domain FROM details where hosp_location like '{0}'""".format(loc)
    cursor = conn.cursor()
    cursor.execute(x1,loc)
    result = cursor.fetchall()
    print("Hospitals in {} :".format(loc))
    print(" ")
    for i in result:

        print(*i)
        list_hosp.append(i[0])
    print(" ")
    enter=input("Enter to Continue".rjust(25," "))
    
    get_illness(list_hosp)

def get_illness(list_hosp):
    os.system('cls')
    x5="""Select ill1,ill2,ill3,ill4,ill5,ill6 from illness"""
    cursor=conn.cursor()
    cursor.execute(x5)
    li=cursor.fetchall()
    no=1
    for p in li:
        for x in p:
            print(no,".",x)
            no+=1
        print()
            
    
    
    c=input("What is your need?:").lower()
 
    
    x2="""SELECT pri_no FROM illness WHERE ill1 like '{0}' or ill2 like '{0}' or ill3 like '{0}' or ill4 like '{0}' or ill5 like '{0}' or ill6 like '{0}' """.format(c)
    cursor=conn.cursor()
    cursor.execute(x2,c)
    ans=cursor.fetchall()
    print(ans)
    os.system('cls')
    print("Your Hospital".rjust(20," "))
    for i in ans:
        x3="""select hosp_name from details where hosp_id like '{0}'""".format(i[0])
        cursor= conn.cursor()
        cursor.execute(x3,i[0])
        fin=cursor.fetchall()
        for y in fin:
            if y[0] in list_hosp:
                print(*y)
    show_location()
def show_location():
    h=input("Choose your hospital from above: ")
    x4="""select hosp_address from details where hosp_name like '{0}'""".format(h)
    cursor=conn.cursor()
    cursor.execute(x4,h)
    l=cursor.fetchall()
    webbrowser.open(*l[0])
while(True):
    os.system('cls')
    print("***Welcome***".rjust(20," "))
    hosp_location=input("Enter your location:",)
    loc=hosp_location
    get_hosp(loc)
    exit()
