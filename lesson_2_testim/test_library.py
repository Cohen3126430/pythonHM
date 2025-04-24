from library import Library
from book import Book
# import pytest

#בדיקה שהפונקציה מוסיפה ספר חדש לרשימת הספרים במערכת.
def test_add_book():
    library = Library()
    new_book = Book("myBook", "Someone")
    library.add_book(new_book)
    assert len(library.books)==1
    assert library.books[0]==new_book


 # בדיקה שהפונקציה מוסיפה משתמש חדש לרשימת המשתמשים.
def test_add_user():
    library = Library()
    library.add_user("Riki")
    assert len(library.users)==1
    assert library.users[0]=="Riki"

# בדיקה שהספר הושאל בהצלחה למשתמש רשום.
def test_check_out_book():
    library = Library()
    new_book = Book("myBook", "Someone")
    library.add_book(new_book)
    library.add_user("Riki")
    library.check_out_book("Riki",new_book)
    assert library.checked_out_books["Riki"] == new_book
    assert new_book.is_checked_out == True

#בדיקה שהספר מוחזר בהצלחה לאחר שהושאל.
def test_return_book():
    library = Library()
    new_book = Book("myBook", "Someone")
    library.add_book(new_book)
    library.add_user("Riki")
    library.check_out_book("Riki",new_book)
    library.return_book("Riki", new_book)
    assert library.checked_out_books.__contains__(new_book)==0
    assert new_book.is_checked_out == False

#בדיקה שהפונקציה מחפשת ספרים לפי שם מדויק.
def test_search_books():
    library = Library()
    new_book = Book("myBook", "Someone")
    library.add_book(new_book)
    library.search_books("myBook")
    assert [book for book in library.books if "myBook".lower() in book.title.lower()]

