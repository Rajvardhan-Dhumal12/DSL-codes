
# Hash Table using Division Method and Chaining

size = 10
hash_table = [[] for i in range(size)]

# Insert operation
def insert(key, value):
    index = key % size

    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key updated successfully")
            return

    hash_table[index].append([key, value])
    print("Inserted successfully")


# Search operation
def search(key):
    index = key % size

    for pair in hash_table[index]:
        if pair[0] == key:
            print("Value:", pair[1])
            return

    print("Key not found")


# Delete operation
def delete(key):
    index = key % size

    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Deleted successfully")
            return

    print("Key not found")


# Display operation
def display():
    for i in range(size):
        print(i, ":", hash_table[i])


# Main program
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")
