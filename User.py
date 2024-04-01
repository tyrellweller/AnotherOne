class User():
    def __init__(self , first ,last):
        self.first = first
        self.last = last
        self.age = 0
    def describe_user(self):
        print("Name : " + self.first.title() + " " + self.last.title())
    def greet_user(self):
        print("Hello there " + self.first.title() + " " + self.last.title())
    def get_age(self , age):
        self.age = age
        return self.age
