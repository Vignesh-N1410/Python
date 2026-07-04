subjects = ["Mathematics", "Science", "English", "History", "Computer Science"]

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def get_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def main():
    marks = []

    print("--------------------------------------------")
    print("        STUDENT GRADE CALCULATOR")
    print("--------------------------------------------")

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total, average = get_average(marks)
    percentage = (total / (len(subjects) * 100)) * 100
    grade = get_grade(average)

    print("--------------------------------------------")
    print("               RESULT")
    print("--------------------------------------------")
    print(f"Total Marks  : {total} / {len(subjects) * 100}")
    print(f"Percentage   : {percentage:}%")
    print(f"Average      : {average:}")
    print(f"Grade        : {grade}")
    print("--------------------------------------------")

main()