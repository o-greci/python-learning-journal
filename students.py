
students = {
    "001": {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    "002": {"name": "Bob", "age": 21, "grades": [92, 88, 95]}
}
def add_student(student_id, name, age):
    students[student_id] = {
        'name': name,
        'age': age,
        'grades': []  
    }

def add_grade(student_id, grade):
    if student_id not in students:
        print(f"Student {student_id} not found!")
        return
    if 0 <= grade <= 100:
        students[student_id]['grades'].append(grade)
    else:
        print("Grade must be between 0 and 100!")  # 

def get_average(student_id):
    grades = students[student_id]['grades']
    if not grades:
        return 0  #  Защита от пустого списка
    return sum(grades) / len(grades)
def get_all_students():
    for student_id, info in students.items():
        name = info["name"]
        age = info["age"]
        grades = info["grades"]
        average = get_average(student_id)  # Уже есть защита в функции
        
        print(f"ID: {student_id}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print("-" * 20)


def start():
    while True:
        print('''\n1. Add student\n2. Add grade\n3. Show average\n4. Show all\n5. Exit''')
        
        try:
            choose = int(input('Choose (1-5): '))
        except ValueError:
            print("Please enter a number 1-5!")
            continue
            
        if choose == 1:
            student_id = input("\nEnter student's ID: ")
            if student_id in students:
                print(f"Student ID {student_id} already exists!")
                continue
            name = input("Enter name: ")
            
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Age must be a number!")
                continue
                
            add_student(student_id, name, age)
            print(f"Student {name} added successfully!")
            
        elif choose == 2:
            student_id = input("\nEnter student's ID: ")
            
            try:
                grade = int(input('Enter grade: '))
            except ValueError:
                print("Grade must be a number!")
                continue
                
            add_grade(student_id, grade)
            
        elif choose == 3:
            student_id = input("\nEnter student's ID: ")  # ✅ ДОБАВЛЕНО
            if student_id in students:
                print(f"Average: {get_average(student_id):.2f}")
            else:
                print(f"Student {student_id} not found!")
                
        elif choose == 4:
            if not students:  # ✅ Проверка на пустоту
                print("No students in the system!")
            else:
                get_all_students()
                
        elif choose == 5:
            print("Goodbye!")
            break
            
        else:
            print("Please enter number 1-5!")

start()