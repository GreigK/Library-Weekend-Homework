from models.book import *

book1 = Book('FlashBoys', 'Michael_Lewis', 'finance')
book2 = Book('Do_Androids_Dream_of_Electric_Sheep', 'Philip_Dick', 'Scifi')
book3 = Book('Rogues', 'Patrick_Keefe', 'True_Crime')
book4 = Book('The_Hitchhikers_Guide_to_the_Galaxy', 'Douglas_Adams', 'Scifi')
book5 = Book('Firestarter', 'Stephen_King', 'Scifi')
books = [book1, book2, book3, book4, book5]

def add_book(book):
    books.append(book)

def remove_book(book):
    books.pop(book)