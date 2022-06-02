class book:
    
    def __init__(self,name,author,price,publishing_year):
        self.book_name=name
        self.book_author=author
        self.book_price=price
        self.book_publishing_year=publishing_year
        
    def book_print(self):
        print("Book Name:"+self.book_name)
        print("Book Author:"+self.book_author)
        print("Book Price:"+str(self.book_price))
        print("Book Publishing year:"+str(self.book_publishing_year))
        
    def book_years_published(self):
        years_published=2022-self.book_publishing_year
        print("This book was published "+str(years_published)+" years ago")
        
book1=book("Battle Bugs","Jack Patton",10.99,1990)
book1.book_print()
book1.book_years_published()
        

