"""Список студентов и отбор по среднему баллу."""
import math

groupmates = [
    {"name": "Алексей", "surname": "Морозов",
     "patronymic": "Ильич", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [4, 3, 5]},
    {"name": "Иван", "surname": "Петров",
     "patronymic": "Сергеевич", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [4, 4, 4]},
    {"name": "Кирилл", "surname": "Смирнов",
     "patronymic": "Андреевич", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [5, 5, 5]},
    {"name": "Анна", "surname": "Соколова",
     "patronymic": "Викторовна", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [5, 4, 5]},
    {"name": "Мария", "surname": "Кузнецова",
     "patronymic": "Олеговна", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [3, 3, 4]},
    {"name": "Дмитрий", "surname": "Волков",
     "patronymic": "Павлович", "group": "БСТ0001",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [4, 5, 4]},
]


def average_mark(student):
    marks = student["marks"]
    if not marks:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(marks) / len(marks)


def filter_students(students, threshold):
    """Вернуть студентов со средним баллом строго выше threshold."""
    if not math.isfinite(threshold):
        raise ValueError("Порог должен быть конечным числом")
    return [s for s in students if average_mark(s) > threshold]


def print_students(students):
    print(f"{'ФИО':<34} {'Группа':<8} {'Экзамены':<30} {'Оценки':<9} Средний")
    print("-" * 94)
    for student in students:
        exams = ", ".join(student["exams"])
        marks = ", ".join(map(str, student["marks"]))
        full_name = f"{student['surname']} {student['name']} {student['patronymic']}"
        print(f"{full_name:<34} {student['group']:<8} "
              f"{exams:<30} {marks:<9} {average_mark(student):.2f}")


def read_threshold():
    while True:
        raw = input("Введите порог среднего балла от 0 до 5: ").strip()
        try:
            value = float(raw.replace(",", "."))
            if not math.isfinite(value) or not 0 <= value <= 5:
                raise ValueError
            return value
        except ValueError:
            print("Ошибка: введите конечное число от 0 до 5.")


def main():
    print("Список студентов группы БСТ0001")
    print_students(groupmates)
    try:
        threshold = read_threshold()
    except (EOFError, KeyboardInterrupt):
        print("\nВвод отменён.")
        return 1
    selected = filter_students(groupmates, threshold)
    print(f"\nСтуденты со средним баллом строго выше {threshold:g}:")
    if selected:
        print_students(selected)
    else:
        print("Подходящих студентов нет.")
    print(f"Найдено студентов: {len(selected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
