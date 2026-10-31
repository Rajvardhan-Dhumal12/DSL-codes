queue = []
while True:
    print("\n1. Add Customer")
    print("2. Book Ticket")
    print("3. Show Customers")
    print("4. Cancel Booking")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Enter customer name: ")
        queue.append(name)
        print("Customer added")
    elif ch == 2:
        if queue:
            print("Ticket booked for:", queue.pop(0))
        else:
            print("No customers")
    elif ch == 3:
        print("Waiting customers:", queue)
    elif ch == 4:
        name = input("Enter name to cancel: ")
        if name in queue:
            queue.remove(name)
            print("Booking cancelled")
        else:
            print("Customer not found")
    elif ch == 5:
        print("Thank You")
        break
    else:
        print("Wrong choice")