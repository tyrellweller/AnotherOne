from Restaurant import Restaurant as rs
class IceCreamStand(rs):
    def __init__(self , name , type , **creams):
        super().__init__(name , type)
        self.creams = creams
    def get_creams(self):
        cream = {}
        for key , value in self.creams.items():
            cream[key] = value
        return cream
ice = IceCreamStand("senyang" , "utan" , choco = "chocolate" , white = "vanilla")
ice.open_restaurant()
cream = ice.get_creams()
for key , value in cream.items():
    print(key  + " " + value)