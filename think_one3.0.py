
class Animal():
    def __init__(self, name, color, leg_num, tail, size, spec):
        self.name = name
        self.color = color
        self.leg_num = leg_num
        self.tail = tail
        self.size = size
        self.spec = spec

    def whatis(self):
        print("Zvire je {}, barv: {}, koncetin ma {}, ocas: {}, velikost {}, vlastnosti {}".format(self.name, self.color, self.leg_num, self.tail, self.size, self.spec))
        #animal1.whatis()

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

    for line in _file:
        line = line.strip()
        radek = line.split(", ")
        exec("animal" + str(i) + " = Animal(radek[0], radek[1], radek[2], radek[3], radek[4], radek[5])")
        i += 1
        print(radek)

animal3.whatis()
animal1.whatis()
