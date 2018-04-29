class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.name          = restaurant_name
        self.type          = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("the restaurant's name is %s" %self.name.title())
        print("the restaurant's cuisine_type has %s "%self.type)
        print("the restaurant had serverd %s people "%self.number_served)
    def open_restaurant(self):
        print("the restaurant is opening")

    def set_number_served(self,number_served):
        if number_served > self.number_served:
            self.number_served = number_served
        else:
            print("wrong number_served")

    def increment_number_served(self,increment_number_served):
        if increment_number_served >= 0 :
            self.number_served += increment_number_served
        else:
            print("increment number served should > 0")

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["apple","pear","orange","banana"]

    def describe_flavors(self):
        for i in self.flavors:
            print(i)

M_icecreamstand = IceCreamStand("Mr.m's IceCreamStand","IceCream")
M_icecreamstand.describe_flavors()
M_icecreamstand.describe_restaurant()
