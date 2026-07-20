# Q2. Classes, Objects, Encapsulation
# Problem Statement
# Title: Library Book Management System
# Description
# Design a class named Book to represent a library book.
# Each book has the following attributes:
# • book_id
# • title
# • author
# • total_copies
# • available_copies
# When a book object is created:
# • available_copies should initially be equal to total_copies.
# Implement the following methods:
# borrow_book()
# • If at least one copy is available:
# o Reduce available copies by 1.
# o Print:
# o Book borrowed successfully.
# • Otherwise print:
# • No copies available.
# return_book()
# • If available copies are less than total copies:
# o Increase available copies by 1.
# o Print:
# o Book returned successfully.
# • Otherwise print:
# • All copies are already in the library.
# display_details()
# Display the information exactly in the following format:
# Book ID : 101
# Title : Python Programming
# Author : Guido
# Available Copies : 2/3

class Book:
    def __init__(self, book_id,title,author,total_copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.total_copies=total_copies
        self.available_copies=total_copies
        
    def borrow_book(self):
        if self.available_copies>=1:
            self.available_copies=self.available_copies-1
            print("Book Borrowed Successfully!")
        else:
            print("No Copies Available")
            
    def return_book(self):
        if self.available_copies<self.total_copies:
            self.available_copies=self.available_copies+1
            print("Book Returned Successfully!")
        else:
            print("All copies are already in the library")
            
    def display_details(self):
        print("\n===== Book Details =====\n")
        print("Book ID: ",self.book_id)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Total Copies: ",self.total_copies)
        print("Available Copies: ",self.available_copies)
        print("\n========================\n")
        

book1=Book(101,"Python Programming", "Pavan Kumar", 3)
book1.display_details()
book1.borrow_book()
book1.borrow_book()
book1.display_details()
book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.display_details()


        