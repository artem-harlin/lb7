# realizaciya modulya namedtuple

from collections import namedtuple

class Skidki():
    Skidki_Dlya = namedtuple("Skidki_Dlya", "name surname skidka")
    Alex = Skidki_Dlya(name = "Alex", surname = "Ivanov", skidka = 10000)
    Sasha = Skidki_Dlya(name = "Sasha", surname = "Smirnov", skidka = 20000)
    Artem = Skidki_Dlya(name = "Artem", surname = "Popov", skidka = 500000)
    Nikita = Skidki_Dlya(name = "Nikita", surname = "Sokolov", skidka = 9000)
    print(Alex)
    print(Nikita)



# realizaciya modulya OrderedDict

from collections import OrderedDict

class Skidki2():
    name = OrderedDict([("Sasha =", 20000), ("Artem =", 500000), ("Nikita =", 9000)])
    for key, value in name.items():
        print(key, value)
