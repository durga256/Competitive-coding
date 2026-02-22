class Item:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def print_hell(self):
        print("Hello")

class Item2(Item):
    def print_hell(self):
        print("Helooooooooo")

it1 = Item2('Phone')
it1.print_hell()