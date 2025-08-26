#Library Management System in Python

class Library:
    def __init__(self):
        self.books = {}
        self.members = []
        self.loans = {}
        
    def addMember(self,name):
        if name not in self.members:
            self.members.append(name)
            print("New member added!")
            self.loans[name] = []
        else:
            print("Member already exists!")
        
        
    def addBook(self,book,copies):
        if book in self.books:
            self.books[book] += copies
        else:
            self.books[book] = copies
        
    def Borrow(self,name,book):
        if book in self.books and self.books[book]>0 :
            self.books[book] -= 1
            self.loans[name].append(book)
            print(book, " borrowed!")
            
        else:
            print("Book doesn't exist!")
            
        
    def Return(self,name,book):
        if book in self.loans:
            self.books[book] += 1
            self.loans[name].remove(book)
            print(book, " returned!")
            
        else:
            print("Book not borrowed!")
            
    def showBooks(self):
        print("Books: ")
        for i in self.books:
            print(i)
            
    def showMembers(self):
        print("Members: ")
        for i in self.members:
            print(i)
            
def main():
    
    lib = Library()
    
    while True:
        
        
        print("Library Menu: \n")
        print("1. Add Member \n")
        print("2. Add Book \n")
        print("3. Borrow Book \n")
        print("4. Return Book \n")
        print("5. Show all members \n")
        print("6. Show all books \n")
        print("7. Exit \n")
        choice = str(input("Enter your choice: "))
    
    
    
        if(choice == "1"):
            name = str(input("Enter member name: "));
            lib.addMember(name)
            
        elif(choice == "2"):
            book = str(input("Enter book name: "))
            quantity = int(input("Enter quantity: "))
            lib.addBook(book , quantity)
            
        elif(choice =="3"):
            book_name = str(input("Enter book you wish to borrow: "))
            member = str(input("Enter member name: "))
            lib.Borrow(member , book_name)
            
        elif(choice =="4"):
            book_name = str(input("Enter book you wish to return: "))
            member = str(input("Enter member name: "))
            lib.Return(member , book_name)
            
        elif(choice == "5"):
            lib.showMembers()
            
        elif(choice == "6"):
            lib.showBooks()
            
        elif(choice == "7"):
            print("Thank you for visiting!")
            break
            
        else:
            print("Invalid choice!")
            
        
    
        
if __name__ == "__main__":
    main()