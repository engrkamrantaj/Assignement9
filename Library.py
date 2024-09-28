# function to display books

def display_books() -> None:

    print("\n\nInput 1.Display all Books")
    print("Input 2.Display Available books only")
    print("Input 3.Display checked out books only")

    display_id = input("\nInput 1,2 or 3 according to your requirement = ")

    if display_id == "1":
        for book in books:
            # imp that you write book not books here because in iteration book is represent a single dictionary
            print(f"\nid:{book['id']} Title:{book['title']
                                             } Status:{book['availability_status']}")
    elif display_id == "2":
        for book in books:
            if book["availability_status"] == "Available":
                print(f"\nid:{book['id']} Title:{book['title']} Status:{
                    book['availability_status']}")

    elif display_id == "3":
        for book in books:
            if book["availability_status"] == "Checked out":
                print(f"\nid:{book['id']} Title:{book['title']
                                                 } Status:{book['availability_status']}")


# *************************************************************************************************************************************
# Function to Borrow a book


def borrow() -> None:
    borrow_id = input("Input the ID Number of the book you want to Borrow = ")
    for book in books:
        if (book["id"] == int(borrow_id)):
            if book["availability_status"] == "Available":
                user_id = input("Enter your user id = ")
            else:
                print("Book has already been issued")
                return
            for user in users:
                if int(user_id) == user["id"]:
                    user["borrowed_books"].append(book)
                    book["availability_status"] = "Checked out"
                    return

# *************************************************************************************************************************************
# Function to return a book


def ret() -> None:
    user_id = input("Enter your user id = ")
    for user in users:
        if int(user_id) == user["id"]:
            print("\n Here is the list of books you have borrowed")
            for book in user["borrowed_books"]:
                print(f"id = {book['id']} Book Name = {book['title']}")

            return_id = input("Enter ID of the Book you want to return = ")

            for book in user["borrowed_books"]:
                if book["id"] == int(return_id):
                    user["borrowed_books"].remove(book)
                    for b in books:
                        if b["id"] == int(return_id):
                            b["availability_status"] = "Available"
                    print(f"\n You have successfully removed book {
                          b['title']}")
                    return
            print("Book not found in borrowed list")
            return
# **************************************************************************************************************************************
# Search Feature


def search() -> None:
    print("\nChoose a Search Method")
    print("Input 1.Search by title")
    print("Input 2.Search by author")
    print("Input 3.Search by genre")

    search_input = input("Choose your search method : ")

    if search_input == "1":
        search_method = input("Input the book title = ")
        for book in books:
            if book["title"] == search_method:
                print(f"id= {book["id"]} tile= {book["title"]} Availability status = {
                      book["availability_status"]}")
                return
        print("\nThis book is not available in the library")

    elif search_input == "2":
        search_method = input("Input the name of the author = ")
        for book in books:
            if book["author"] == search_method:
                print(f"id= {book["id"]} tile= {book["title"]} Author= {book["title"]} Availability status = {
                      book["availability_status"]}")
                return
        print("\nThis authors book is not available in the library")

    elif search_input == "3":
        search_method = input("Input the genre of the book = ")
        for book in books:
            if book["genre"] == search_method:
                print(f"id= {book["id"]} tile= {book["title"]} Genre= {book["genre"]} Availability status = {
                    book["availability_status"]}")
                return
        print("\nThis genre's book is not available in the library")

# *************************************************************************************************************************************
# Function to display all users


def user_search() -> None:
    for user in users:
        print(f"username : {user["name"]}")
        print(f"Books issued to {user["name"]} are mentioned below")
        for book in user["borrowed_books"]:
            print(f" - {book["title"]}")


# *************************************************************************************************************************************
# Library System book data base to start with
books = [

    {
        "id": 1,
        "title": "Harry potter 1",
        "author": "JK Rowling",
        "genre": "fantasy",
        "availability_status": "Available"
    },
    {
        "id": 2,
        "title": "Harry potter 2",
        "author": "Author2",
        "genre": "Action",
        "availability_status": "Available"
    },

    {
        "id": 3,
        "title": "Harry potter 3",
        "author": "Author3",
        "genre": "Magic",
        "availability_status": "Available"
    },
    {
        "id": 4,
        "title": "Harry potter 4",
        "author": "JK Rowling",
        "genre": "English",
        "availability_status": "Checked out"
    }

]
# **********************************************************************************************************
# Library System users to start with
users = [
    {"id": 1, "name": "ali", "borrowed_books": []},
    {"id": 2, "name": "kamran", "borrowed_books": []},
    {"id": 3, "name": "amjad", "borrowed_books": []},
    {"id": 4, "name": "zikria", "borrowed_books": [{  # For checking issued 1 book to id 4
        "id": 4,
        "title": "Harry potter 4",
        "author": "Author4",
        "genre": "English",
        "availability_status": "Assigned"
    }]}
]
list_of_borrowed_books: list = []
# ************************************************************************************************************
# Program Flow

while True:

    print("\n Choose one of the following task")
    print("Input 1.See all,Available or checked out books")
    print("Input 2.Borrow a Book")
    print("Input 3.Return a Book")
    print("Input 4.Search for a Book")
    print("Input 5.View all users and Books they have checked out")

    user_input = input("\nEnter 1,2,3,4,5 or input done to exit = ")

    if user_input == "1":
        display_books()

    elif user_input == "2":
        borrow()

    elif user_input == "3":
        ret()
    elif user_input == "4":
        search()
    elif user_input == "5":
        user_search()

    elif user_input == "done":
        break
# *************************************************************************************************************
