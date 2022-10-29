"""Simple OOP task."""


class Student:
    """Student class."""
    def __init__(self, name, finished=False):
        """Constructor."""
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False
