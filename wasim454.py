class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show(self):
        print("Book Is=",self.bookid)
        print("Title=",self.title)
        print("Price=",self.price)
b=Book(12,"Let Us C",1009.9)
b.show()