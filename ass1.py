class Hashtable:
    def __init__(self):
        self.m = int(input("Enter size of hash table: "))
        self.hashTable = [None] * self.m
        self.elecount = 0

    def hashFunction(self, key):
        return key % self.m

    def isFull(self):
        return self.elecount == self.m

    def insert(self, key, data, probing_method):
        if self.isFull():
            print("Table is full.")
            return
        index = self.hashFunction(key)
        compare = 0

        # Insert using the specified probing method (Linear or Quadratic)
        while self.hashTable[index] is not None:
            compare += 1
            index = probing_method(index, compare)

        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}.")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    def search(self, key, data, probing_method):
        index = self.hashFunction(key)
        compare = 0

        # Search using the specified probing method (Linear or Quadratic)
        while self.hashTable[index] is not None:
            compare += 1
            if self.hashTable[index] == [key, data]:
                return index
            index = probing_method(index, compare)
        return None

    def linearProbe(self, index, compare):
        return (index + 1) % self.m

    def quadraticProbe(self, index, compare):
        return (index + compare * compare) % self.m


def menu():
    obj = Hashtable()

    while True:
        print("************************")
        print("1. Linear Probe Insert/Search")
        print("2. Quadratic Probe Insert/Search")
        print("3. Exit")
        print("************************")

        ch = int(input("Enter Choice: "))
        if ch == 1:
            while True:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter choice: "))
                if ch2 == 1:
                    key = int(input("Enter key (phone number): "))
                    data = input("Enter data (name): ")
                    obj.insert(key, data, obj.linearProbe)
                elif ch2 == 2:
                    key = int(input("Enter key to be searched: "))
                    data = input("Enter data (name): ")
                    result = obj.search(key, data, obj.linearProbe)
                    if result is None:
                        print("Key not found.")
                    else:
                        print(f"Key found at index {result}.")
                else:
                    break
        elif ch == 2:
            while True:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter choice: "))
                if ch2 == 1:
                    key = int(input("Enter key (phone number): "))
                    data = input("Enter data (name): ")
                    obj.insert(key, data, obj.quadraticProbe)
                elif ch2 == 2:
                    key = int(input("Enter key to be searched: "))
                    data = input("Enter data (name): ")
                    result = obj.search(key, data, obj.quadraticProbe)
                    if result is None:
                        print("Key not found.")
                    else:
                        print(f"Key found at index {result}.")
                else:
                    break
        else:
            break


menu()
