class Animal:
    name = ''

    def eat(self):
        print("Я могу поесть")


class Dog(Animal):
    def display(self):
        print('Меня зовут ', self.name)

    def eat(self):
        super().eat()
        print("Я могу много поесть")


collei = Dog()
# print(Dog.__dict__)
collei.name = "Max"
# print(collei.__dict__)

tax = Dog()
# print(collei.__dict__)
# print(Dog.__dict__)
tax.name = "Rex"
#
# # print(collei.__dict__)
collei.display()
# tax.display()
#
collei.eat()
