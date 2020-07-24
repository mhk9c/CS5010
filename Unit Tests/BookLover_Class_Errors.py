##Module 5 Live Session Exercise: Testing Activity
##Anna Landi, Maureen O’Shea, Michael Kolonay, David Vann
##aol4h, mo2cr, mhk9c, dv6bq


class BookLover:
    # fields: name, email, favGenre, favGenre, numBooks, bookLst (a list of tuples)
    # bookLst[0] = ('book_name', numeric rating)

    def __init__(self, name, email, favGenre, numBooks, bookLst=None,):  # constructor
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        if bookLst is None:
            self.bookLst = []
        else:
            self.bookLst = bookLst

    def __str__(self):
        return "Name: " + self.name + "\n" + \
        "Book List: " + str(self.bookLst)

    def addBook(self, bookName, rating):
        if self.hasRead(bookName):
            return True
        else:
            self.bookLst.append((bookName, rating))
            self.numBooks += 1
            return False

    def hasRead(self, bookName):
        return bookName in [pair[1] for pair in self.bookLst]

    def numBooksRead(self):
        return len(self.bookLst)

    def favBooks(self):
        fav_list = [book[0] for book in self.bookLst if book[1] > 2]
        return fav_list
