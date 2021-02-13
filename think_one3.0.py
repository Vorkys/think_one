import weakref

class Animal():

    _instances = set()                  #dunno

    def __init__(self, name, color, leg_num, tail, size, spec):
        self.name = name
        self.color = color
        self.leg_num = leg_num
        self.tail = tail
        self.size = size
        self.spec = spec

        self._instances.add(weakref.ref(self))

    def whatis(self):                   #print to zvire
        print("Zvire je {}, barvy: {}, koncetin ma {}, ocas: {}, velikost {}, vlastnosti {}".format(self.name, self.color, self.leg_num, self.tail, self.size, self.spec))
        #animal1.whatis()


    @classmethod                        #tohle prej neco dela
    def getInstances(cls):
        dead = set()
        for ref in cls._instances:
            object = ref()
            if object is not None:
                yield object
            else:
                dead.add(ref)

        cls._instances -= dead


### creates new dynamic vyriables
#_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#for x in range(9):
#    exec("animal" + str(x) + " = _list[7], _list[5]")

#print(animal4)
######################################

i = 1

with open("animals.txt", "r", encoding = "utf-8") as _file:
#while 1:
#    _line = _file.readline()

#    x = _line.split(", ")
#    print(x)

#    if not _line:
#        break

    for line in _file:                          #vytvori instance
        line = line.strip()
        radek = line.split(", ")
        exec("animal" + str(i) + " = Animal(radek[0], radek[1], radek[2], radek[3], radek[4], radek[5:])")
        i += 1
        print(radek)

#animal3.whatis()
#animal5.whatis()
for object in Animal.getInstances():            #printne jmena vsech instanci
    print(object.name)                          #ale ne v poradi => wtf
