import os
class Vhbase:
    def __init__(self, tires, type):
        self.tires = tires
        self.type = type

    def __str__(self):
        return self.tires + "   " + self.type

    def start(self):
        print("normal start")


class car(Vhbase):
    def __init__(self, tires, type, colour):
        # type: (object, object, object) -> object
        Vhbase.__init__(self, tires, type)
        self.colour = colour

    def __str__(self):
        return self.tires + "  " + self.type + "  " + self.colour

    def start(self):
        # Vbase.start(self)
        print("Car start")



class truck(Vhbase):
    def __init__(self, tires, type, colour):
        Vhbase.__init__(self, tires, type)
        self.colour = colour

   # def __str__(self):
    #    return self.tires + "  " + self.type + "  " + self.colour

    def start(self):
        # Vbase.start(self)
        print("truck start")


x = truck(4, 't', 'r')
print (x.tires)
#print(x.start())
