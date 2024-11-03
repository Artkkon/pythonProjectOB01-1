class Store:
    def __init__(self, name, adress, items):
        self.name = name
        self.adress = adress
        self.items = items

    def add_item(self, key, value):
        self.items[key] = value

    def remove_item(self, key):
        del self.items[key]

    def get_item(self, key):
        try:
            return self.items[key]
        except KeyError:
            return None


store1 = Store("My Store", "123 Main Street", {"apple": 1.99, "banana": 0.99})
store2 = Store("Your Store", "456 Second Street", {"orange": 2.99, "pineapple": 3.99})
store3 = Store("Our Store", "789 Third Street", {"grape": 4.99, "kiwi": 5.99})

store1.add_item("cherry", 6.99)
store1.remove_item("banana")
store1.add_item("apple", 7.99)

print(store1.get_item("apple"))
print(store1.get_item("banana"))
print(store1.get_item("cherry"))
