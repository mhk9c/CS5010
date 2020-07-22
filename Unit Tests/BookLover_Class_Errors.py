class BookLover:
    # fields: name, email, favGenre, favGenre, numBooks, bookLst (a list of tuples)

    # Local variables

    
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
        return bookName in [pair[0] for pair in self.bookLst]

    def numBooksRead(self):
        return self.numBooks

    def favBooks(self):
        pass
