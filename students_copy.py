import json
import os

FILENAME = "students.json"

def load_students():
    if not os.path.exists(FILENAME):
        print("📁 Файл не найден. Начинаем с пустого списка.")
        return {}
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"✅ Загружено {len(data)} студентов")
            return data
    except json.JSONDecodeError:
        print("❌ Файл повреждён. Создаю резервную копию.")
        if os.path.exists(FILENAME):
            os.rename(FILENAME, FILENAME + ".broken")
        return {}
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return {}

def save_students():
    try:
        with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        print(f"✅ Сохранено {len(students)} студентов")
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")

# Загружаем студентов при старте
students = load_students()

def add_student(student_id, name, age):
    students[student_id] = {
        'name': name,
        'age': age,
        'grades': []  
    }

def add_grade():
    student_id = input("\nEnter student's ID: ")
    if student_id not in students:
        print(f"Student {student_id} not found!")
        return
    print('Enter "stop" to end')
    while True:
        try:
            grade = input('Enter grade: ')
            if grade == 'stop':
                break
            if 0 <= int(grade) <= 100:
                students[student_id]['grades'].append(int(grade))
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
                print("Age must be a number!")
                continue

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
        print('''\n1. Add student\n2. Add grade\n3. Show average\n4. Show all\n5. Save to file\n6. Reload from file\n7. Exit''')
        
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
            add_grade()
            
        elif choose == 3:
            student_id = input("\nEnter student's ID: ")  # ✅ ДОБАВЛЕНО
            if student_id in students:
                print(f"Average: {get_average(student_id):.2f}")
            else:
                print(f"Student {student_id} not found!")            
        
        elif choose == 4:
            if students== {}:  # ✅ Проверка на пустоту
                print("No students in the system!")
            else:
                get_all_students()

        elif choose == 5:
            save_students()
            print("💾 Ручное сохранение выполнено") 

        elif choose == 6:
            students = load_students()
            print("📂 Данные перезагружены из файла")        

        elif choose == 7:
            print("Goodbye!")
            break
        else:
            print("Please enter number 1-6!")
start()