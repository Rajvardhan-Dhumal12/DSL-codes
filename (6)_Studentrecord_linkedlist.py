class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

head = None
while True:
    print("\n1.Add 2.Delete 3.Update 4.Search 5.Display 6.Sort 7.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        n = Node(int(input("Roll: ")),
                 input("Name: "),
                 int(input("Marks: ")))

        if head == None:
            head = n
        else:
            t = head
            while t.next:
                t = t.next
            t.next = n
    elif ch == 2:
        r = int(input("Roll to delete: "))
        t = head
        while t and t.roll != r:
            t = t.next
        if t:
            if t == head:
                head = head.next
            else:
                p = head
                while p.next != t:
                    p = p.next
                p.next = t.next
            print("Deleted")
    elif ch == 3:
        r = int(input("Roll to update: "))
        t = head
        while t and t.roll != r:
            t = t.next
        if t:
            t.name = input("New name: ")
            t.marks = int(input("New marks: "))
            print("Updated")
    elif ch == 4:
        r = int(input("Roll to search: "))
        t = head
        while t and t.roll != r:
            t = t.next
        if t:
            print(t.roll, t.name, t.marks)
        else:
            print("Not found")
    elif ch == 5:
        t = head
        while t:
            print(t.roll, t.name, t.marks)
            t = t.next
    elif ch == 6:
        a = []
        t = head
        while t:
            a.append(t)
            t = t.next
        a.sort(key=lambda x: x.marks)
        for x in a:
            print(x.roll, x.name, x.marks)
    elif ch == 7:
        break