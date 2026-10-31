undo_stack = []
redo_stack = []
document = "My Name is Rajvardhan"

while True:
    print("\n--- Text Editor ---")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_text = input("Enter new document text: ")
        undo_stack.append(document)
        document = new_text
        redo_stack.clear()
        print("Change made successfully.")

    elif choice == 2:
        if len(undo_stack) == 0:
            print("Nothing to undo.")
        else:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Undo successful.")

    elif choice == 3:
        if len(redo_stack) == 0:
            print("Nothing to redo.")
        else:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Redo successful.")

    elif choice == 4:
        print("Current Document:", document)

    elif choice == 5:
        print("Exiting...")
        break