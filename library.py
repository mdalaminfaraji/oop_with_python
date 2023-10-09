class Book:
    def __init__(self, id, name, quantity) -> None:
        self.id=id
        self.name=name
        self.quantity=quantity

class User:
    def __init__(self, id, name, password) -> None:
        self.id=id
        self.name=name
        self.password=password
        self.borrowedBooks=[]
        self.returnedBooks=[]

class Library:
    def __init__(self, name) -> None:
        self.name=name
        self.users=[]
        self.books=[]

    def addBook(self, id, name, quantity):
        book=Book(id, name, quantity)
        self.books.append(book)
        print(f'{book.name} added successfully!\n')

    def addUser(self, id, name, password):
        user=User(id, name, password)
        self.users.append(user)
        return user
    
    def borrowBook(self, user, token):
        for book in self.books:
            if book.name==token:
                if book in user.borrowedBooks:
                    print("already borrowed !\n")
                    return
                elif book.quantity==0:
                    print("No copy available!\n")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -=1
                    print("borrowed book Successfully !\n")
                    return
        print(f"Not found  ant book with name {token}! \n")


    def returnBook(self, user, token):
        for book in self.books:
            if book.name==token:
                if book in user.borrowedBooks:
                    book.quantity +=1
                    user.returnedBooks.append(book)
                    user.borrowedBooks.remove(book)
                    print("Returned book Successfully !\n")
                    return
                elif book.quantity==0:
                    print("No copy available!\n")
                    return
            
            user.borrowedBooks.append(book)
            book.quantity -=1
            return
        print(f"Not found  ant book with name {token}! \n")
        

bsk=Library('Bishwa Shahitja Kendro')
admin=bsk.addUser(1000, "admin", "admin")
ratin=bsk.addUser(17, "ratin", "123")
cpBook=bsk.addBook(11, "cp book", "5")
currentUser=admin

while True:
    if currentUser==None:
        print("No loggen in user\n")

        option=input("Login or Register(L/R) :")

        if option=="L":
            id=int(input("Enter Id: "))
            password=input("Enter Password : ")

            match=False
            for user in bsk.users:
                if user.id==id and user.password==password:
                    currentUser=user
                    match=True
                    break
            if match==False:
                print("No user Found ! \n")

        elif option=="R":
            id=int(input("Enter Id: "))
            name=input("Enter name : ")
            password=input("Enter Password : ")

            for user in bsk.users:
                if user.id==id:
                    print("user already exists!\n")
                    break
                user=bsk.addUser(id, name, password)

                currentUser=user
        
    else:
            print(f"Welcome Back {currentUser.name}")
            if currentUser.name=="admin":
                print("Options : \n")
                print("1: add book")
                print("2: Add user")
                print("3. Show all Books")
                print("4. Logout")

                ch=int(input("Enter option: "))

                if ch==1:
                    id=int(input("Enter book id: "))
                    name=input("Enter book name: ")
                    quan=input("Enter No of books")
                    bsk.addBook(id, name, quan)
                elif ch==3:
                    for book in bsk.books:
                        print(f'{book.id}\t {book.name} \t {book.quantity}')
                    print('\n')
                elif ch==4:
                    currentUser=None
            else:
                print("Options : \n")
                print("1: borrow book")
                print("2: return book")
                print("3. Show Borrowed books")
                print("4. Show History")
                print("5. Logout")

                ch=int(input("Enter option: "))

                if ch==1:
                     name=input("Enter book name: ")
                     bsk.borrowBook(currentUser, name)
                elif ch==2:
                     name=input("Enter book name: ")
                     bsk.returnBook(currentUser, name)
                elif ch==3:
                    print("\n Borrowed Books: \n")
                    for book in currentUser.borrowedBooks:
                         print(f'{book.id}\t {book.name} \t {book.quantity}')
                    print('\n')
                elif ch==4:
                    print("\n History: \n")
                    for book in currentUser.returnedBooks:
                         print(f'{book.id}\t {book.name} \t {book.quantity}')
                    print('\n')
                elif ch==5:
                    currentUser=None




            
