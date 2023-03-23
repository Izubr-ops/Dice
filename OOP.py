class Human():
    def __init__(self, name, age=None, height=170):
        self.name = name
        self.age = age
        self.height = height

    def print_name(self):
        print(self.name)
    def print_height(self):
        print(self.height)



human1 = Human("n", "6", "mic")
human2 = Human("Ivan", height=180)

print(human2.name, human2.age, human2.height)
"""human1.print_height()"""
human2.print_height()