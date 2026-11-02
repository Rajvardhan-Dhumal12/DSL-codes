n = int(input("Enter number of books: "))

books = []
count = []

for i in range(n):
    name = input(f"Enter name of book {i+1}: ")
    borrow_count = int(input(f"{name} borrowed - "))

    books.append(name)
    count.append(borrow_count)


# Step 1: Average borrow count

total = 0

for i in range(n):
    total += count[i]

average = total / n


# Step 2: Find highest and lowest

highest = lowest = count[0]
highest_book = lowest_book = books[0]

for i in range(1, n):
    if count[i] > highest:
        highest = count[i]
        highest_book = books[i]

    if count[i] < lowest:
        lowest = count[i]
        lowest_book = books[i]


# Step 3: Count highest and lowest books

count_high = count_low = 0

for i in range(n):
    if count[i] == highest:
        count_high += 1

    if count[i] == lowest:
        count_low += 1


# Step 4: Count members who borrowed zero books

zero = 0

for i in range(n):
    if count[i] == 0:
        zero += 1


# Step 5: Display frequency of each book

print("\nBook borrowing frequency:")

for i in range(n):
    print(books[i], ":", count[i])


# Display results

print("\nAverage books borrowed:", average)

print("Highest borrowed:", highest_book,
      "(", highest, "times) -", count_high, "book(s) tied")

print("Lowest borrowed:", lowest_book,
      "(", lowest, "times) -", count_low, "book(s) tied")

print("Members who borrowed zero books:", zero)