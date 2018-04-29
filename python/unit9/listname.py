class Names():
    def __init__(self):
        self.names = []
    def addname(self,name):
        self.names.append(name)
        print(self.names)
    def insertname(self,number,name):
        self.names.insert(number,name)
        print(self.names)
# names = [
#     'Siyang Zhang','Bo yang','Long wan','Qing Teng'
# ]
#
#
# for i in names:
#     print("Dear %s ,nice to meet you ! " %i)
#
# names.insert(2,'hello world!')

myname = Names()
myname.addname("ytt")

myname.insertname(0,'ssss')
print(myname.names)
