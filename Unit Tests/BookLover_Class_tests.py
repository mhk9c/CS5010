# Module 5 Exercise: Python Unit Testing
# Michael Kolonay
# mhk9c


import unittest
from BookLover_Class import *

class BookLoverTestCases(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing adding grades in AStudent_Class.py
    
    def test_add_books(self):
        # Are added grades being correctly added to the grades list?

        # Set up
        book_lover0 = BookLover( 'Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0) # create instance
        book_lover0.addBook('newBook 1', 4)
        book_lover0.addBook('newBook 2', 9)
        book_lover0.addBook("newBook 3", 3)
        # Test
        self.assertEqual(book_lover0.bookLst, [('newBook 1', 4), ('newBook 2', 9), ('newBook 3', 3)])

    def test_add_existing_books(self):
        # Are added grades being correctly added to the grades list?
        # Set up
        book_lover0 = BookLover('Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0)  # create instance
        book_lover0.addBook('oldBook', 4)
        # Test
        self.assertFalse(book_lover0.addBook('oldBook', 4))

    def test_add_new_books(self):
        # Are added grades being correctly added to the grades list?

        # Set up
        book_lover0 = BookLover('Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0)  # create instance
        book_lover0.addBook('oldBook', 4)

        # Test
        self.assertTrue(book_lover0.addBook('newBook', 4))






if __name__ == '__main__':
    unittest.main()            