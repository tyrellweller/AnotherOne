class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " restaurant has a " + self.cuisine_type.title() + " dishes type")
    def open_restaurant(self):
        print(self.restaurant_name.title() + " restaurant is now open")
    def set_number_served(self , number):
        self.number_served = number
    def inrement_number_served(self , increment):
        self.number_served += increment

res = Restaurant("senyang" , "utan")
res.set_number_served(10)
res.inrement_number_served(10)
print(res.number_served)