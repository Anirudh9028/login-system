import re

    
def access ():
    pass

def pwd_validate():

    password = input('create password: ')
    
    while True:
        if (len(password)<5 or len(password)>16)is None:
            print("length of pwd should be mi 5 and max 16")
            pwd_validate()
            break
        
        elif re.search("[A-Z]",password)is None:
            print("pwd should contained at least one uppercase ")
            pwd_validate()
            break
        
        elif re.search('[a-z]',password) is None:
            print("pwd should contained at least one lowercase")
            pwd_validate()
            break
        
        elif re.search("[0-9]",password)is None:
            print("pwd should contained at least one digit")
            pwd_validate()
            break
    
        elif re.search("[$#@!]",password)is None:
            print("pwd should contained at least one special character")
            pwd_validate()
            break

        elif re.search("\s",password) :
            print("pwd should not contained space")
            pwd_validate()
            break

        
        else:
            file = open("C:\\Users\\admin\\Desktop\\database",'a')
            file.write(password+ "\n")
            file.close()
            print ("pwd set succsess fully ")
            print ("Register Succsesful")
            break
            








def register ():
    
    file = open("C:\\Users\\admin\\Desktop\\database","r")
    username = input('enter username: ')
    

    user =[]
    pwd =[]

    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        user.append(a)
        pwd.append(b)
        data = dict(zip(user, pwd))
        
    while True:
        if username in user:
            print("user name exist:",user)
            register ()
            break
                    
        else:
            if re.search("(^[A-za-z\d\.\-]+)@([\w]+)(\.[a-z]{2,8}$)",username)is None:
                print ("""email id should contain:\n"@" and followed by "."\neg:- sherlock@gmail.com\nit should not start with special characters and numbers\neg:- @gmail.com
there should not be any "." immediate next to "@"\neg:- my@.in""")
                register ()
                break

            else:
                file = open("C:\\Users\\admin\\Desktop\\database",'w')
                file.write(username+", ")
                file.close()
                print ("username set sucsess fully ")
                pwd_validate()
                break
                
        


def login():
    
    file = open("C:\\Users\\admin\\Desktop\\database","r")
    username = input('enter username: ')
    password = input('enter password: ')

    if not len(username or password)<1:
        user =[]
        pwd =[]

        for i in file:
            a,b = i.split(",")
            a = a.strip()
            b = b.strip()
            user.append(a)
            pwd.append(b)
        data = dict(zip(user, pwd))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("login success")
                    else:
                        print("password OR username is incorrect")
                except:
                    print("incorrect password or username")               
            else:
                print("usrname and password doesn't exist")            
        except:
            print("do register first")
    else:
        print("enter username and password")


def forgot_password():
    
    file = open("C:\\Users\\admin\\Desktop\\database","r")
    username = input('enter username: ')
    user =[]
    pwd =[]
    for i in file:
        a,b = i.split(",")
        a = a.strip()
        b = b.strip()
        user.append(a)
        pwd.append(b)
        data = dict(zip(user, pwd))
        

        while True:
            
            if username in user:
                print("hi your password is : ", pwd)
                login_system()
                break
            else:
                print("\nusername doesn't exist, do register\n")
                login_system()
                break
            





            
def login_system():

    a = int(input("press 1 for register\npress 2 for login\npress 3 for forgot password\n "))

    if a == 1:
        register()

    elif a==2:
        login()
        
    elif a==3:
        forgot_password()
        
    else:
        print("press 1 or 2")



login_system()





































    

    

