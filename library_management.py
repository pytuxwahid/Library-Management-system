import csv
import added_books_file
library_book=[{'title': 'python',
               'authors': 'subin, xayed', 
               'isbn': '34', 
               'publishing year': '2014',
               'quantity': 3, 
               'price': 23.0
               },
              
              {'title': 'java',
               'authors': 'anis', 
               'isbn': '2', 
               'publishing year': '2015',
               'quantity': 2, 
               'price': 12.0
               },
              
              
              {'title': 'data stucture',
               'authors': 'nahin,sara', 
               'isbn': '4', 
               'publishing year': '2017',
               'quantity': 5, 
               'price': 45.0
               },
              
              ]

lent_books={}



    

def view_all_books():
    if not library_book:
        print("No books available in the library.")
        return

    print("\nAvailable Books in the Library:\n")
    print(f"{'Title':<15} {'Authors':<15} {'Year':<5} {'Quantity':<5} {'Price':<5}")
    print("*"*45)
    for book in library_book:
        authors = "".join(book['authors'])
        print(f"{book['title']:<15} {authors:<15} {book['publishing year']:<5} {book['quantity']:<5} ${book['price']:<5.2f}")


def search_books_by_title_or_isbn():
    search_term=input('enter what you want to seacrh by title or isbn :')
    for book in library_book:
        if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
            print(f"Found:title-{book['title']} - isbn:{book['isbn']} -price:{book['price']}")


def search_book_by_author():
    search_term=input('enter what you want to seacrh by author  :')
    for book in library_book:
        if search_term.lower() in book['authors'].lower():
            authors = ", ".join(book['authors'])
            print(f"Found:title-{book['title']} - authors:{book['authors']} -price:{book['price']}")


def remove_book():
    search_term=input('enter the book title you want to remove :')
    for index,book in enumerate(library_book):
        if search_term.lower() in book['title'].lower():
            print(f"{index+1}.{book['title']}")
    
    selected_index=input('enter a book to remove:')
    selected_index=int(selected_index)
    
    library_book.pop(selected_index-1)
    save_book()
    print('book remove succefull')
    
def lend_book():
     search_term=input('enter the book title you want to lend :')
     for index,book in enumerate(library_book):
         if search_term.lower() in book['title'].lower():
            if book['quantity'] > 0:
                borrower_name = input("Enter your name: ")
                borrower_phone = input("Enter your phone number: ")
                book['quantity'] -=1
                if book['isbn'] not in lent_books:
                    lent_books[book['isbn']] = []
                lent_books[book['isbn']].append({
                    'name': borrower_name,
                    'phone': borrower_phone
                })
                save_book()
                print(f"Book '{book['title']}' lent to {borrower_name}.")
            else:
                print('book is not available to lend')
            return
     print('book is not found')


def view_lent_books():
    if not lent_books:
        print("No books have been lent.")
        return

    print("\nLent Books and Borrowers:\n")
    print(f"{'ISBN':<15} {'Title':<20} {'Borrower Name':<20} {'Borrower Phone':<15}")
    print("=" * 70)
    for book in library_book:
        if book['isbn'] in lent_books:
            for borrower in lent_books[book['isbn']]:
                print(f"{book['isbn']:<15} {book['title']:<20} {borrower['name']:<20} {borrower['phone']:<15}")


def return_book():
    isbn = input('Enter the ISBN of the book you want to return: ')
    if isbn in lent_books:
        borrower_name = input("Enter your name: ")
        borrower_phone = input("Enter your phone number: ")
        
        for borrower in lent_books[isbn]:
            if borrower['name'] == borrower_name and borrower['phone'] == borrower_phone:
                lent_books[isbn].remove(borrower)
                if not lent_books[isbn]:
                    del lent_books[isbn]
                for book in library_book:
                    if book['isbn'] == isbn:
                        book['quantity'] += 1
                        save_book()
                        print(f"Book '{book['title']}' returned successfully.")
                        return
        print('Borrower details not found.')
    else:
        print('Book not found in lent records.') 

def save_book():
    try:
        with open('library_books.csv', mode='w', newline='') as file:
            fieldnames = ["title", "authors", "isbn", "publishing year", "quantity", "price"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in library_book:
                writer.writerow({
                    "title": book["title"],
                    "authors": ",".join(book["authors"]),
                    "isbn": book["isbn"],
                    "publishing year": book["publishing year"],
                    "quantity": book["quantity"],
                    "price": book["price"]
                })
            print("Library books saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving library books: {e}")

    try:
        with open('lent_books.csv', mode='w', newline='') as file:
            fieldnames = ["isbn", "name", "phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for isbn, borrowers in lent_books.items():
                for borrower in borrowers:
                    writer.writerow({
                        "isbn": isbn,
                        "name": borrower["name"],
                        "phone": borrower["phone"]
                    })
            print("Lent books saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving lent books: {e}")  


def save_action():
    global library_book, lent_books

    try:
        with open('library_books.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                library_book.append({
                    "title": row["title"],
                    "authors": row["authors"].split(","),
                    "isbn": row["isbn"],
                    "publishing year": row["publishing year"],
                    "quantity": int(row["quantity"]),
                    "price": float(row["price"])
                })
            print("Library books loaded successfully.")
    except FileNotFoundError:
        print("No saved books found. Starting with an empty library.")
    except Exception as e:
        print(f"An error occurred while loading library books: {e}")

    try:
        with open('lent_books.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                isbn = row["isbn"]
                if isbn not in lent_books:
                    lent_books[isbn] = []
                lent_books[isbn].append({
                    "name": row["name"],
                    "phone": row["phone"]
                })
            print("Lent books loaded successfully.")
    except FileNotFoundError:
        print("No saved lent books found. Starting with no lent books.")
    except Exception as e:
        print(f"An error occurred while loading lent books: {e}")  


print("Welcome to the Library Management System")

menu_text = """
Your options:
1. Add Book
2. View All Books
3. Search Book by Title or ISBN
4. Search Book by Author
5. Remove Book
6. Lend Book
7. View Lent Books
8. Return Book
0. Exit
"""

while True:
    print(menu_text)
    choice = input("Enter your choice: ")
    
    if choice == '1':
       library_book=added_books_file.added_books(library_book)
    elif choice == '2':
         view_all_books()
    elif choice == '3':
         search_books_by_title_or_isbn()
    elif choice == '4':
         search_book_by_author()
    elif choice == '5':
         remove_book()
    elif choice == '6':
         lend_book()
    elif choice == '7':
         view_lent_books()
    elif choice == '8':
         return_book()
    elif choice == '0':
         print("Exiting the program.")
         break
    else:
        print("Invalid choice. Please try again.")
        

          
                             
         
    
