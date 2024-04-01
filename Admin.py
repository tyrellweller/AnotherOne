from User import User as u
class Admin(u):
    def __init__(self , first , last , privileges):
        super().__init__(first , last)
        self.privileges = privileges
    def show_privileges(self):
        for p in self.privileges:
            print(p)
