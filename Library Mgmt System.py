# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:57:55 2019

@author: tanuj
"""

import sys
class Library:
      def __init__(self,listofbooks):#this init method is the first method to be invoked when you create an object
            #what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")
            

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

def main():            
      library=Library(["Digital Fortress","Angels and Demons","Da Vinci Code"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                print("Thank You! Visit Again")
                  
main()
