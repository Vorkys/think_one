import weakref

class Animal():

    def __init__(self, name, color, leg_num, tail, size, spec):     #konstruktor
        self.name = name
        self.color = color
        self.leg_num = leg_num
        self.tail = tail
        self.size = size
        self.spec = spec
        
        self._instances.add(weakref.ref(self))
        
    def whatis(self):
        print("Zvire je {}, barvy: {}, koncetin ma {}, ocas: {}, velikost {}, vlastnosti {}".format(self.name, self.color, self.leg_num, self.tail, self.size, self.spec))
        
    @classmethod
    def getInstances(cls):
        dead = set()
        for ref in cls._instances:
            object = ref()
            
            if object is not None:
                yield object
            else:
                dead.add(ref)
                
        cls._instances -= dead
        
i = 0

with open("animals.txt", "r", encoding = "utf-8") as data:
    for _line in data:
        _line = _line.strip()
        line = _line.split(", ")
        exec("animal" + str(i) + " = Animal(line[0], line[1], line[2], line[3], line[4], line[5:])")
        
        i += 1

#only testing data below
print(30 * "#")
animal3.whatis()
animal4.whatis()            #print test zvirata
animal5.whatis()
print(30 * "#")

del animal0                                    #smaze instanci ktera je: zvire, barva,...

for object in Animal.getInstances():            #printne jmena vsech instanci
    print(object.name)                          #ale ne v poradi => wtf

input()
