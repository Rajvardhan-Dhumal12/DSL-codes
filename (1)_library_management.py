n = int(input("Enter number of books: "))
books = []
count = []

for i in range(n):
    name = input(f"Enter name of book {i+1}: ")
    borrow_count = int(input(f"{name} borrowed - "))
    books.append(name)
    count.append(borrow_count)

# Step: average borrow count
total = 0
for i in range(n):
    total += count[i]
average = total / n

# Step: find highest & lowest
highest = lowest = count[0]
highest_book = lowest_book = books[0]

for i in range(1, n):
    if count[i] > highest:
        highest = count[i]
        highest_book = books[i]
    if count[i] < lowest:
        lowest = count[i]
        lowest_book = books[i]

# Step: count how many books share the highest/lowest count
count_high = count_low = 0
for i in range(n):
    if count[i] == highest:
        count_high += 1
    if count[i] == lowest:
        count_low += 1

# Display
print(f"\nAverage books borrowed: {average}")
print(f"Highest borrowed: {highest_book} ({highest} times) - {count_high} book(s) tied")
print(f"Lowest borrowed: {lowest_book} ({lowest} times) - {count_low} book(s) tied")