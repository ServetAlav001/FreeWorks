import json
import os
class User:
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email

class userRepository:
    def __init__(self):
        self.userlist = []
        self.isloggedin = False
        self.currentuser = {}
        #load users from file DOSYA İŞLEMLERİ
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    userdict = json.loads(user)
                    new_user = User(username=userdict['username'], password=userdict['password'], email=userdict['email'])
                    self.userlist.append(new_user)
                    print(self.userlist[0].username)

    def register(self, new_user : User):
        self.userlist.append(new_user)
        self.savetofile()
        #save to file DOSYA İŞLEMLERİ
        print("kullanici kaydi basarili")
    def login(self,username,password):
        for user in self.userlist:
            if user.username == username and user.password == password:
                self.isloggedin = True
                self.currentuser = user
                print("giris basarili")
                break
        if not self.isloggedin:
            print("kullanici adi veya parola hatali")
    def logout(self):
        self.isloggedin = False
        self.currentuser = {}
        print("cikis yapildi")
        
    def identity(self):
        if self.isloggedin:
            print(f"username: {self.currentuser.username}")
            print(f"email: {self.currentuser.email}")
        else:
            print("giris yapilmadi")
    def savetofile(self):
        userdictlist = []
        for user in self.userlist:
            userdictlist.append(json.dumps(user.__dict__))

        with open("users.json","w",encoding="utf-8") as file:
            json.dump(userdictlist,file)


repository=userRepository()
while True:
    print("menu".center(50,"-"))
    secim = input("1- Register\n2- Login\n3- Save to File\n4- Exit\nSeçiminiz: ")
    if secim == "1":
        name = input("Kullanici adi: ")
        password = input("Parola: ")
        email = input("Email: ")
        new_user = User(username=name, password=password, email=email)
        repository.register(new_user)
        
        print(repository.userlist)

    elif secim == "2":
        name = input("Kullanici adi: ")
        password = input("Parola: ")
        repository.login(name,password)

    elif secim == "3":
        userRepository().savetofile()
    elif secim == "4":
        repository.logout()
        break
    else:
        print("Invalid selection, please try again.")
