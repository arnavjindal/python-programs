List_Book_Dict = {}
borrowed_list = {}
avail_books = {}
class Lirary_Managment:


    def __init__(self,NameOfBook,fname ,lname, ):
        self.fname = fname
        self.lname = lname
        self.NameOfBook = NameOfBook
        if NameOfBook in List_Book_Dict:
            print('already in the library ')
        else:
            person_name = fname+" "+lname
            List_Book_Dict[NameOfBook]=person_name
            avail_books[NameOfBook]=person_name
    @classmethod
    def return_book(cls,BookName,fname , lname):
        try:
            person_name = fname+" "+lname
            del borrowed_list[BookName]
            avail_books[BookName]=person_name
            print("successfully Returned")
        except:
            print("NO SUCH BOOK FOUND")

    @classmethod
    def borrow_book(cls, NameOfBook, fname1, lname1):
        if NameOfBook in borrowed_list:
            print("\nBook already Borrowed by "+repr(borrowed_list[NameOfBook]) )
        else:
            del avail_books[NameOfBook]
            person_name = fname1+" "+lname1
            borrowed_list[NameOfBook]=person_name
            print("Successfully Borrowed")
    def add_book(self):
        pass
    def list_books(self):
        return List_Book_Dict


while True:
    What_to_do_var = input("\nENTER (L)ist ,(A)DD,(B)ORROW,(R)ETURN,(E)XIT AS PER REQUIREMENT : \n")
    if What_to_do_var.lower() == "a":
        a=input("Enter your first name: ")
        b=input("Enter your Last name: ")
        book1= input("enter Name of book: ")
        book1 = Lirary_Managment(book1,a,b)
        print("\nAdded successfully")

    elif What_to_do_var.lower() == "l":
        num = input("You need (B)orrower's list OR (O)verall list? OR (C)omplete list with names: \n")
        if num.lower() == "b":
            for i in borrowed_list:
                print(i)
        elif num.lower() == "o":
            for i in List_Book_Dict:
                print(i)
        elif  num.lower() == "c":
            print(List_Book_Dict)
        else:
            print("U had to enter from B or O")


    elif What_to_do_var.lower() =="b":

        c=input("Enter your first name: ")
        d=input("Enter your Last name: ")
        if avail_books == {}:
            print("vro library khali hai.")
        else:
            print("Available Books- ")
            for i in avail_books:
                print(i,end=" ")
            book= input("\nEnter Name of book You want to Borrow: ")
            book = book.lower()
            Lirary_Managment.borrow_book(book, c, d)

    elif What_to_do_var.lower() =="r":
        e=input("Enter your first name: ")
        f=input("Enter your Last name: ")
        book2= input("Enter Name of book You want to return: ")
        if book2 in List_Book_Dict:
            Lirary_Managment.return_book(book2,e,f)
        else:
            print("ADD the book instead of Returning")
    elif What_to_do_var.lower() =="e":
        print("Thank you for interacting with us.")
        exit()
    else:
        print("ENTER FROM ABOVE OPTIONS ONLY")







"""TODO 
UPPERCAST FOR NAMES WHILE PRINTING 
UNITY FOR EVERY INPUT BY MAKING IT LOWER
make the dictionaries (instances) of the class  like - self.lendDict = {}

"""


# # Harry's code -
# class Library:
#     def __init__(self, list, name):
#         self.booksList = list
#         self.name = name
#         self.lendDict = {}
#
#     def displayBooks(self):
#         print(f"We have following books in our library: {self.name}")
#         for book in self.booksList:
#             print(book)
#
#     def lendBook(self, user, book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("Lender-Book database has been updated. You can take the book now")
#         else:
#             print(f"Book is already being used by {self.lendDict[book]}")
#
#     def addBook(self, book):
#         self.booksList.append(book)
#         print("Book has been added to the book list")
#
#     def returnBook(self, book):
#         self.lendDict.pop(book)
#
# if __name__ == '__main__':
#     harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")
#
#     while(True):
#         print(f"Welcome to the {harry.name} library. Enter your choice to continue")
#         print("1. Display Books")
#         print("2. Lend a Book")
#         print("3. Add a Book")
#         print("4. Return a Book")
#         user_choice = input()
#         if user_choice not in ['1','2','3','4']:        # I LIKED THE WAY OF TAKING THE LOOPING INPUT IF THE INPUT WAS NOT APPROPRIATE
#             print("Please enter a valid option")
#             continue
#
#         else:
#             user_choice = int(user_choice)
#
#
#         if user_choice == 1:
#             harry.displayBooks()
#
#         elif user_choice == 2:
#             book = input("Enter the name of the book you want to lend:")
#             user = input("Enter your name")
#             harry.lendBook(user, book)
#
#         elif user_choice == 3:
#             book = input("Enter the name of the book you want to add:")
#             harry.addBook(book)
#
#         elif user_choice == 4:
#             book = input("Enter the name of the book you want to return:")
#             harry.returnBook(book)
#
#         else:
#             print("Not a valid option")
#
#
#         print("Press q to quit and c to continue")
#         user_choice2 = ""
#         while(user_choice2!="c" and user_choice2!="q"):          # I LIKED THE WAY OF TAKING THE LOOPING INPUT IF THE INPUT WAS NOT APPROPRIATE
            # user_choice2 = input()
#             if user_choice2 == "q":
#                 exit()
#
#             elif user_choice2 == "c":
#                 continue

