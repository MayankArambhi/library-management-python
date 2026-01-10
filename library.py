import time
def add_book(ISBNCode):
    title = input('Title of the Book: ')
    author = input('Author Name: ')
    year = input('Year of Publication: ')
    
    with open('library.csv','a') as f:
        f.write(f'\n{title},{author},{year},True,*{ISBNCode}')
    print(f"Book titled '{title}'({ISBNCode}) added SUCCESSFULLY!")

def borrow_book(ISBNCode):
    with open('library.csv','r') as f:
        lines = f.readlines()

    found = False

    for i in range(len(lines)):
        parts = lines[i].strip().split(',')

        if parts[4] == '*' + ISBNCode:
            found = True
            title = parts[0]

            if parts[3].lower() == "true":
                parts[3] = "False"
                lines[i] = ','.join(parts) + '\n'
            else:
                print('Book NOT available right now!')
                return
            break

    if not found:
        print('Book NOT found!')
        return

    with open('library.csv','w') as f:
        f.writelines(lines)

    print(f"Book titled '{title}'({ISBNCode}) borrowed SUCCESSFULLY!")


def return_book(ISBNCode):
    with open('library.csv','r') as f:
        lines = f.readlines()

    found = False

    for i in range(len(lines)):
        parts = lines[i].strip().split(',')
        if parts[4] == '*' + ISBNCode:
            found = True
            if parts[3].lower() == 'true':
                print('Book already returned!')
                return
            parts[3] = "True"
            title = parts[0]
            
            lines[i] = ','.join(parts) + '\n'
            break
    
    if not found:
        print('Book does not exist in library!')
        return
    
    with open('library.csv','w') as f:
        f.writelines(lines)
    print(f"Book titled '{title}'({ISBNCode}) returned SUCCESSFULLY!")

import pandas as pd
def view_books():
    print(pd.read_csv('library.csv',header=0))

print('Welcome To The Library!\n')

print('''Commands: 
      1 | Add Book
      2 | Borrow Book
      3 | Return Book
      4 | View All Available Books
      Q | Quit
      ''')

i = input('Your input: ')

while True:
    if i == '1': #add
        ISBNCode = input("\nISBN Code of the book(Without '*'): ")
        add_book(ISBNCode)
        time.sleep(3)
    elif i == '2': #borrow
        ISBNCode = input("\nISBN Code of the book(Without '*'): ")
        borrow_book(ISBNCode)
        time.sleep(3)
    elif i == '3': #return
        ISBNCode = input("\nISBN Code of the book(Without '*'): ")
        return_book(ISBNCode)
        time.sleep(3)
    elif i == '4': #view
        view_books()
        time.sleep(3)
    elif i.lower() == 'q':
        break
    else:
        print('\nInvalid Input!')
        time.sleep(3)
    
    print('''\nCommands: 
      1 | Add Book
      2 | Borrow Book
      3 | Return Book
      4 | View All Available Books
      Q | Quit
      ''')
    i = input('Your input: ')