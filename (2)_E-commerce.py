print("-----------Linear Solution-----------")

lst = [134, 205, 639, 300, 200]

key = int(input("Enter account ID to search: "))

found = False

for i in range(len(lst)):
    if lst[i] == key:
        print("Account ID found at position", i + 1)
        found = True
        break

if not found:
    print("Account ID not found in the list")




print("-----------Binary Solution-----------")

lst = [101, 223, 140, 394, 900]
lst.sort()

key = int(input("Enter account ID to search: "))

low = 0
high = len(lst) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if lst[mid] == key:
        print("Account ID found at position", mid + 1)
        found = True
        break
    elif key < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("Account ID not found in the list")