class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()









#     def charm(self):
        #match self.patronus:
            #case "Stag":
            #    return "🐴"
            #case "Otter":
           #     return "🦦"
            #case "Jack Russell terrier":
            #    return "🐶"
           # case _:
           #     return "🪄"