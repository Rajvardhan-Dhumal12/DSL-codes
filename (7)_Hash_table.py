hash_table = [[] for _ in range(10)]
key = int(input("Enter key to insert: "))
value = input("Enter value: ")
index = key % 10
found = False
for i in range(len(hash_table[index])):
    if hash_table[index][i][0] == key:
        hash_table[index][i][1] = value
        found = True
        break
if not found:
    hash_table[index].append([key, value])

print("Key inserted successfully.")
key = int(input("Enter key to search: "))
index = key % 10
found = False
for pair in hash_table[index]:
    if pair[0] == key:
        print("Value:", pair[1])
        found = True
        break
if not found:
    print("Key not found.")
key = int(input("Enter key to delete: "))
index = key % 10
found = False
for i in range(len(hash_table[index])):
    if hash_table[index][i][0] == key:
        hash_table[index].pop(i)
        print("Key deleted successfully.")
        found = True
        break
if not found:
    print("Key not found.")
print("\nHash Table:")
for i in range(10):
    print(i, ":", hash_table[i])