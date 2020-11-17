class Student:
    def __init__(self, name , rollno , Aim):
        self.name = name
        self.rollno = rollno
        self.Aim = Aim
    def printdetails(self):
        print(f"Hello Mr.{self.name}. your Roll Number is {self.rollno} and Aim is to be {self.Aim}. \nPlease press enter to verify details \nTo change details press C ")
        inpu_ = input()
        if inpu_ == "":
            print("details verified")
        elif inpu_.lower() == "c":
            num = int(input('enter 1 for name change, 2 for roll number change , 3 for Aim change\n: '))
            if num == 1:

                New_name =input(f"enter the New Name to replace this - {aj.name}  :")
                aj.name = New_name
            elif num == 2:
                New_rollno =input(f"enter the New roll Number to replace this - {aj.rollno}  :")
                aj.rollno = New_rollno

            elif num == 3:
                New_Aim =input(f"enter the New Aim to replace this - {aj.Aim}  :")
                aj.Aim = New_Aim
            aj.printdetails()
    pass



aj = Student("Arnav Jindal", "7" , "Successful")

aj.printdetails()


