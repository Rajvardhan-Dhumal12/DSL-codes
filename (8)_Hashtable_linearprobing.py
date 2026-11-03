
# Hash Table using Linear Probing

size = 10
hash_table = [None] * size
DELETED = "DELETED"

# Insert operation
def insert(key, value):
    index = key % size
    first_deleted = -1

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is not None and hash_table[pos] != DELETED:
            if hash_table[pos][0] == key:
                hash_table[pos][1] = value
                print("Key updated successfully")
                return

        elif hash_table[pos] == DELETED:
            if first_deleted == -1:
                first_deleted = pos

        else:
            if first_deleted != -1:
                pos = first_deleted

            hash_table[pos] = [key, value]
            print("Inserted successfully")
            return

    if first_deleted != -1:
        hash_table[first_deleted] = [key, value]
        print("Inserted successfully")
    else:
        print("Hash table is full")


# Search operation
def search(key):
    index = key % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            print("Key not found")
            return

        if hash_table[pos] != DELETED:
            if hash_table[pos][0] == key:
                print("Value:", hash_table[pos][1])
                return

    print("Key not found")


# Delete operation
def delete(key):
    index = key % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            print("Key not found")
            return

        if hash_table[pos] != DELETED:
            if hash_table[pos][0] == key:
                hash_table[pos] = DELETED
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
