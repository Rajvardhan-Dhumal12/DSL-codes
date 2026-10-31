print("Rajvardhan Dhumal")

salary = [42500.75, 58000.10, 36500.60, 49500.20, 61000.45, 27500.90]
print("Original Salaries:")
print(salary)

selection_salary = salary.copy()
n = len(selection_salary)

print("\n===== Selection Sort =====")

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if selection_salary[j] < selection_salary[min_index]:
            min_index = j

    selection_salary[i], selection_salary[min_index] = selection_salary[min_index], selection_salary[i]
    print("Pass", i + 1, ":", selection_salary)

print("\nSalaries after Selection Sort (Ascending Order):")
print(selection_salary)

print("\nTop 5 Highest Salaries (Selection Sort):")
print(selection_salary[-5:][::-1])

bubble_salary = salary.copy()

print("\n===== Bubble Sort =====")

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble_salary[j] > bubble_salary[j + 1]:
            bubble_salary[j], bubble_salary[j + 1] = bubble_salary[j + 1], bubble_salary[j]
    print("Pass", i + 1, ":", bubble_salary)

print("\nSalaries after Bubble Sort (Ascending Order):")
print(bubble_salary)
print("\nTop 5 Highest Salaries (Bubble Sort):")
print(bubble_salary[-5:][::-1])