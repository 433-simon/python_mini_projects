books = []   #books is a list containing all the books information inside a dictionary
def add_books () :
    while True:
        id_of_book = int(input("Enter Book unique ID : "))
        name_of_book = input("Enter Name of Book : ")
        author_of_book = input("Author of book : ")
        quantity_of_book = int(input("Qulaity of book available : "))
    
        book = {
        "id" : id_of_book,
        "book_name" : name_of_book,
        "book_author" : author_of_book,
        "book_quantity" : quantity_of_book
                }
        
        books.append(book)  # adding that book dictionary in the list

        option = input("do you want to add more books : ")   #asking if more books are to add in the list..if no the current book got saved 
        if option.lower() != "yes" :
            break;
    
def update_book() :
    book_id = int(input("Enter book ID to update: "))

    for book in books:
        if book["id"] == book_id:
            print("Book found:", book)

        ask = int(input('''Which thing you want to update : 
                    1. Book ID
                    2. Book Author
                    3. Book Name
                    4. Book Qunatity : '''))
        if ask == 1:
                book["id"] = int(input("Enter updated book id: "))
        elif ask == 2:
                book["book_author"] = input("Enter updated author name: ")
        elif ask == 3:
                book["book_name"] = input("Enter updated book name: ")
        elif ask == 4:
                book["book_quantity"] = int(input("Enter updated quantity: "))
        else:
                print("Invalid choice")

        print("Book updated successfully!")
        return

    print("Book not found.")

def view_book() :
        print("The records of books are : \n")
        for book in books:
            print(book)

def search_book():
    book_name = input("Enter book name to search: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            print("\nBook Found:")
            print(book)
            return

    print("Book not found.")



#students is a list containing all the students information inside a dictionary
students = []
def add_student() :
    while True:
        student_roll_no = int(input("Enter student's roll no. : "))
        name_of_student = input("Enter student's name : ")
        number_of_student = int(input("Enter student's contact info : "))
        book_issued_by_student = input("Does student issued any book earlier : ")

        student = {
            "student_id" : student_roll_no,
            "student_name" : name_of_student,
            "student_number" : number_of_student,
            "student_issued_book" : book_issued_by_student
        }
        students.append(student)

        student_option = input("Do you want to add more students : ")
        if student_option.lower() != "yes" :
            break;


def issue_book():
    student_id = int(input("Enter student roll no: "))

    student_found = False
    for student in students:
        if student["student_id"] == student_id:
            student_found = True
            break

    if not student_found:
        print("Student not found.")
        return

    book_name = input("Enter book name to issue: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            if book["book_quantity"] > 0:
                book["book_quantity"] -= 1
                print("Book issued successfully.")
            else:
                print("Book out of stock.")
            return

    print("Book not found.")



def return_book():
    book_name = input("Enter name of book you want to return: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            book["book_quantity"] += 1
            print("Book returned successfully.")
            return

    print("Invalid book name.")

                
def student_menu ():
    while True: 
        print('''
1) Issue Book
2) Return Book
3) Search Book
4) Logout
          ''')
        choice = int(input("Please Enter your choice : "))
        if choice == 1:
            issue_book()
        elif choice == 2:
            return_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            print("Looging out...")
            return
        else:
            print("Invalid Selection please try again...")

def librarian_menu ():
    print('''
1)Add Book
2)Update Book
3)View Books
4)Search Book
5)Logout        
          ''')
    choice = int(input("Please Enter your choice : "))
    if choice == 1:
        print("Add book selected")
        add_books()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
            
    elif choice == 2:
        print("Update book selected")
        update_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 3:
        print("View book selected")
        view_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 4:
        print("Search book selected ")
        search_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 5:
        print("Logging out...")
        return

    else:
        print("Invalid Selection please try again...")

print("Welcome to Library Management System !")
print("Let's login : ")
role = input("Please enter your role(student/librarian) : ")
if role.lower() == "student":
    student_menu()
elif role.lower() == "librarian" :
    librarian_menu()
else :
    print("Invalid input")

