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
# A_restaurant = Restaurant('oldmanandsea','fishes')
#
#
# A_restaurant.describe_restaurant()
# A_restaurant.open_restaurant()
#
# A_restaurant.set_number_served(225)
# A_restaurant.describe_restaurant()
# A_restaurant.increment_number_served(5)
# A_restaurant.describe_restaurant()
# A_restaurant.increment_number_served(-5)
# A_restaurant.describe_restaurant()
