class User():
    def __init__(self , first ,last):
        self.first = first
        self.last = last
        self.login_attempt = 0
    def describe_user(self):
        print("Name : " + self.first.title() + " " + self.last.title())
    def greet_user(self):
        print("Hello there " + self.first.title() + " " + self.last.title())
    def increment_login_attempts(self):
        self.login_attempt += 1
    def reset_login_attempts(self):
        self.login_attemp = 0
user = User("sian daniel" , "loreto")
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempt)
user.reset_login_attempts()
print(user.login_attemp)