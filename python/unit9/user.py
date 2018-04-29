class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def describe_user(self):
        print("%s's first name is %s "%(self.last_name,self.first_name))
        print("%s's last name is %s "%(self.last_name ,self.last_name))

    def greet_user(self):
        print("hello ,%s ,nice to meet you " %self.last_name)

A_user = User(first_name='Mingjun Chen', last_name='Dun A')
B_user = User(first_name='Qing Teng', last_name='Teng Qing')

A_user.describe_user()
A_user.greet_user()
B_user.describe_user()
B_user.greet_user()
