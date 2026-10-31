class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def search(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    if x < root.data:
        return search(root.left, x)
    return search(root.right, x)

def delete(root, x):
    if root is None:
        return root
    if x < root.data:
        root.left = delete(root.left, x)
    elif x > root.data:
        root.right = delete(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def display(root):
    if root:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)

root = None
while True:
    print("\n1.Insert  2.Delete  3.Search  4.Display  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        x = int(input("Enter value: "))
        root = delete(root, x)
        print("Deleted")
    elif ch == 3:
        x = int(input("Enter value: "))
        print("Found" if search(root, x) else "Not Found")
    elif ch == 4:
        print("BST:", end=" ")
        display(root)
        print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")