class Calculator(): ## lets you add functions to a class, making them unique. EXAMPLE: Calculator.add(1, 2)
    def add(n1, n2):
        print(n1 + n2)
        return n1 + n2
    def addList(list):
        print(sum(list))
        return sum(list)
    def sub(n1, n2):
        print(n1 - n2)
        return n1 - n2

class Hero:
    def __init__(self, name, money, inv):
        self.inventory = inv
        self.money = money
        self.name = name
    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name} purchased {item} and has {self.inventory}")
