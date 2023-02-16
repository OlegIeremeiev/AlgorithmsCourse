from student_dataclass import Student


if __name__ == "__main__":

    st = Student("Тарас", "Тарасов", "АСД", 88)
    print(st.get_info())
    print(st.get_message())
    st = Student("Петро", "Стеценко", "АСД", 67,"залік")
    print(st.get_info())
    print(st.get_message())
    st = Student("Сергій", "Тимошко", "АСД", 145)
    print(st.get_info())
    print(st.get_message())
