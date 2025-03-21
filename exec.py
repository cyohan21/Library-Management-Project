class LibraryDatabase:
    library_dict = {
        'The Night Of The Living Dead': {'Author': 'Alexandre Guimault', 'Genre': 'Horror', 'Availability': 'Available'},
        'Measure For Measure': {'Author': 'William Shakespeare', 'Genre': 'Comedy', 'Availability': 'Not Available'},
        'The Three Musketeers': {'Author': 'Alexandre Dumas', 'Genre': 'Comedy', 'Availability': 'Available'}
    }
    @classmethod
    def view_availability(cls, book_name):
        print(cls.library_dict[book_name]['Availability'])
    @classmethod
    def return_book(cls, book_name):
        cls.library_dict[book_name]['Availability'] = 'Available'
    @classmethod
    def borrow_book(cls, book_name):
        cls.library_dict[book_name]['Availability'] = 'Not Available'

    def view_catalog(self):
        print(LibraryDatabase.library_dict)

class LibraryApp:
    def main(self):
        prompt = """Welcome to the Library App! Please enter one of the following:
            1: View Book Availability
            2: Borrow Book
            3: Return Book
            4: View Catalog
            5: Exit
            """
        valid_responses = ['1', '2', '3', '4', '5']

        while True:
            welcome_input = get_valid_input(prompt, valid_responses)
        
            if welcome_input == '1':
                self.view_availability_input()
            elif welcome_input == '2':
                self.borrow_book_input()
            elif welcome_input == '3':
                self.return_book_input()
            elif welcome_input == '4':
                self.view_catalog()
            elif welcome_input == '5':
                print('Goodbye!')
                exit()

    def view_availability_input(self):
        book_name = input('Enter book name: ')
        book_name = book_name.title()
        if book_name in LibraryDatabase.library_dict:
            LibraryDatabase.view_availability(book_name)
            return
        else:
            print(f'{book_name} not found.')
    
    def borrow_book_input(self):
        book_name = input('Enter book name: ')
        book_name = book_name.title()
        if book_name in LibraryDatabase.library_dict and LibraryDatabase.library_dict[book_name]['Availability'] == 'Available':
            print(f'{book_name} borrowed successfully.')
        elif book_name in LibraryDatabase.library_dict and LibraryDatabase.library_dict[book_name]['Availability'] == 'Not Available':
            print(f'{book_name} has already been already borrwed.')
            return
        else:
            print(f'{book_name} not found.')

    def return_book_input(self):
        book_name = input('Enter book name: ')
        book_name = book_name.title()
        if book_name in LibraryDatabase.library_dict and LibraryDatabase.library_dict[book_name]['Availability'] == 'Not Available':
            print(f'{book_name} returned successfully.')
        elif book_name in LibraryDatabase.library_dict and LibraryDatabase.library_dict[book_name]['Availability'] == 'Available':
            print(f'{book_name} is already in our library.')
            return
        else:
            print(f'{book_name} not found.')
    
    def view_catalog(self):
        LibraryDatabase.view_catalog(self)


def get_valid_input(prompt, valid_responses):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_responses:
            return user_input
        else:
            print("I didn't get that, sorry. Please try again.")



if __name__ == '__main__':
    LibraryApp().main()
