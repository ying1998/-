class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
        
    def describe_user(self):
        print("%s's first name is %s "%(self.last_name,self.first_name))
        print("%s's last name is %s "%(self.last_name ,self.last_name))

    def greet_user(self):
        print("hello ,%s ,nice to meet you " %self.last_name)

class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     for i in self.privileges:
    #         print(i)

# A_admin=Admin("lan","ying")
# A_admin.privileges.show_privileges()
# A_admin.describe_user()
