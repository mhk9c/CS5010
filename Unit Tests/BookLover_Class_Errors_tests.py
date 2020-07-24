# Module 5 Exercise: Python Unit Testing
##Module 5 Live Session Exercise: Testing Activity
##Anna Landi, Maureen O’Shea, Michael Kolonay, David Vann
##aol4h, mo2cr, mhk9c, dv6bq


import unittest
from BookLover_Class_Errors import *

class BookLoverTestCases(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing adding grades in AStudent_Class.py

    #############################
    #     Testing addBook       #
    #############################
    def test_add_books(self):
        # Are added books being correctly added to the bool list?

        # Set up
        book_lover0 = BookLover( 'Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0) # create instance
        book_lover0.addBook('newBook 1', 4)
        book_lover0.addBook('newBook 2', 9)
        book_lover0.addBook("newBook 3", 3)
        # Test
        self.assertEqual(book_lover0.bookLst, [('newBook 1', 4), ('newBook 2', 9), ('newBook 3', 3)])

    def test_add_existing_books(self):
        # Does adding an existing book correctly fail to add to book list?
        # Set up
        book_lover0 = BookLover('Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0)  # create instance
        book_lover0.addBook('oldBook', 4)
        # Test
        self.assertFalse(book_lover0.addBook('oldBook', 4))

    def test_add_new_books(self):
        # Does adding an new book correctly succeed in adding to book list?
        # Set up
        book_lover0 = BookLover('Michael Kolonay', 'mhk9c@virginia.edu', 'favGenre', 0)  # create instance
        book_lover0.addBook('oldBook', 4)

        # Test
        self.assertTrue(book_lover0.addBook('newBook', 4))

    #############################
    #     Testing favBooks      #
    #############################
    def test_if_favBooks_adding_Favbooks_into_list(self):
        # Is one book being added correctly to favBooks list?
        # Set up
        reader1 = BookLover("Jenny", "jr@aol.com", "mystery", 220)
        reader1.addBook("Othello", 4)
        fav_books = reader1.favBooks()
        # test
        self.assertEqual(fav_books, ["Othello"])

    def test_if_favBooks_adding_multiple_Favbooks_into_list(self):
        # Are 2 books being added correctly to favBooks list?
        # Set up
        reader2 = BookLover("Jane", "j35@gmail.com", "novels", 230)
        reader2.addBook("Mockingjay", 5)
        reader2.addBook("Harry Potter", 4)
        fav_books = reader2.favBooks()
        # test
        self.assertEqual(reader2.favBooks(), ["Mockingjay", "Harry Potter"])




    #############################
    #     Testing numBooksRead      #
    #############################
    def test_is_numBooksRead_working_correctly(self):
        # Set up
        booklover1 = BookLover("Jane", "jane@virginia.edu", "Horror", 2)
        #booklover1.numBooks(2)  # TypeError: 'int' object is not callable
        print(booklover1.numBooksRead())

        # Test
        self.assertEqual(booklover1.numBooksRead(), 2)

    #############################
    #     Testing hasRead      #
    #############################
    def test_is_hasRead_working_correctly(self):
        # Set up
        booklover1 = BookLover("test", "test@virginia.edu", "Horror", 2, [('Some book', 5),('Some book2', 6),('Some book3', 7)])

        # Test
        self.assertTrue(booklover1.hasRead('Some book'))


    def test_is_hasRead_working_correctly(self):
        # Set up
        booklover1 = BookLover("test", "test@virginia.edu", "Horror", 2,[('Some book', 5), ('Some book2', 6), ('Some book3', 7)])

        # Test
        self.assertFalse(booklover1.hasRead('no good book'))



if __name__ == '__main__':
    unittest.main()            