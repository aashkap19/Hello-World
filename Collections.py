# Function to find the letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Test data (name, [grades])
students = [
    ("Jeremiah", [47, 59, 93, 70, 89]),
    ("Torrance", [94, 72, 91, 67, 100]),
    ("Mary", [92, 44, 94, 83, 79]),
    ("Beth", [77, 32, 27, 100, 92]),
    ("John", [100, 100, 100, 99, 82]),
    ("Larry", [44, 89, 77, 66, 100]),
    ("Megan", [50, 85, 75, 95, 95])
]

# Run each test case without using loops → just repeating manually
# (so we stick to assignment rules)
def process_student(name, grades):
    average = sum(grades) / len(grades)
    letter = get_letter_grade(average)
    print(name)
    print("List:", *grades)
    print("Average:", round(average, 1))
    print("Letter Grade:", letter)
    print()  # blank line for spacing

# Call function for each student (no loop)
process_student("Jeremiah", [47, 59, 93, 70, 89])
process_student("Torrance", [94, 72, 91, 67, 100])
process_student("Mary", [92, 44, 94, 83, 79])
process_student("Beth", [77, 32, 27, 100, 92])
process_student("John", [100, 100, 100, 99, 82])
process_student("Larry", [44, 89, 77, 66, 100])
process_student("Megan", [50, 85, 75, 95, 95])