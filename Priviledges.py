class Admin():
    def __init__(self , privileges):
        self.privileges = privileges
    def show_privileges(self):
        for p in self.privileges:
            print(p)

class Priviledges():
    def __init__(self , priviledges):
        self.priviledges = priviledges
    def show_priviledges(self):
        priv = Admin(self.priviledges)
        priv.show_privileges()
priviledges = ['can add post' , 'can delete post' , 'can ban user']
p = Priviledges(priviledges)
p.show_priviledges()