# Sample digits to arrange into the largest possible number.
digits = [9, 8, 9, 6, 1]


def max_salary(digits):
    salary = ""

    while len(digits) > 0:
        # Place the largest remaining digit next.
        biggest_number = max(digits)
        salary = salary + str(biggest_number)
        # Remove the chosen digit so each occurrence is used once.
        digits.remove(biggest_number)

    return salary


print(max_salary(digits))
