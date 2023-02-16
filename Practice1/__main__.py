from student_classic import Student
# from student_dataclass import Student


if __name__ == "__main__":
    # Демонстраційну частину коду винесено окремо для забезпечення коректних результатів покриття тестів

    st = Student("Тарас", "Тарасов", "АСД", 88)
    print(st.get_info())
    print(st.get_message())
    st = Student("Петро", "Стеценко", "АСД", 67,"залік")
    print(st.get_info())
    print(st.get_message())

    # Варіант з помилкою
    st = Student("Сергій", "Тимошко", "АСД", 145)
    print(st.get_info())
    print(st.get_message())
