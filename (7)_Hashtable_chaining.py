class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None or self.table[pos] == "DELETED":
                self.table[pos] = key
                print("Key inserted.")
                return

            if self.table[pos] == key:
                print("Key already exists.")
                return

        print("Hash table is full.")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                print("Key not found.")
                return

            if self.table[pos] == key:
                print("Key found at index", pos)
                return

        print("Key not found.")

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Key deleted.")
                return

            if self.table[pos] is None:
                print("Key not found.")
                return

        print("Key not found.")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


h = HashTable()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        h.insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        h.search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        h.delete(key)

    elif choice == 4:
        h.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice.")