def added_books(library_book):
    title = input("Enter the title of the book: ")
    authors = input( "Enter the authors of the book (please use comma to add multiple authors): ")
    authors = authors.split(",")
    isbn = input("Enter the ISBN of the book: ")
    publishing_year = input("Enter the publishing year of the book: ")
    quantity=int(input('Enter the quantity of the book:'))
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid floating number.")
    price = get_float_input("Enter the price of the book: ")
            

    
    
    library={
        "title":title,
        "authors":authors,
        "isbn":isbn,
        "publishing year":publishing_year,
        "quantity":quantity,
        "price":price,
        
        
    }
    
    library_book.append(library)
    save_book()
    print('successfull')
    return library_book