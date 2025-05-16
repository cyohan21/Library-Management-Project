# Python Library Management Project

## Overview

This application allows users to:

- View the availability of a book  
- Borrow a book  
- Return a book  
- View the entire catalog of books

## How It Works

When you launch the program, you will see the following prompt:  

> Welcome to the Library App! Please enter one of the following:
>> 1: View Book Availability
>> 
>> 2: Borrow Book
>> 
>> 3: Return Book
>> 
>> 4: View Catalog
>> 
>> 5: Exit

If you enter `1`, the program will prompt you to enter the name of a book. If the book exists in the library, its availability status will be displayed. If the book is not found, an error message will appear.  

If you enter `2`, you will be prompted to enter the name of a book. If the book is available, you will receive a confirmation message that you have successfully borrowed it. If the book is already borrowed, an appropriate message will be displayed. 
If the book does not exist, an error message will appear.  

If you enter `3`, you will be asked to enter the name of the book you wish to return. If the book is currently borrowed, it will be returned successfully. 
If the book is already available, a message will notify you that it is still in the library. If the book does not exist, an error message will be displayed. 

If you enter `4`, the application will display the complete catalog of books along with their **author, genre, and availability status**. 

If you enter `5`, the program will close with a farewell message:  

> Goodbye!
