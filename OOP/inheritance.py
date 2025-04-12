

#Inheritance in Python

class Vehicle:
    
    def __init__(self,engine,type):
        self.engine=engine
        self.type=type
    
    def Vehicle_type(self):
        print(f'type: {self.type}')

class Mehran(Vehicle):
 

    def __init__(self,engine,type):
        self.engine=engine
        self.type=type

    def MehranCar(self):
        print(f'This is mehran car')


m=Mehran('1.0','Car')
m.Vehicle_type()