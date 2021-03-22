class Student:
    __counter = 0

    def __init__(self) -> None:
        """构造方法
        """
        self.__counter += 1

    def printCounter(self):
        """输出计数器

        Returns:
            int: 计数器
        """
        return self.__counter


student = Student()
print(student.printCounter())
