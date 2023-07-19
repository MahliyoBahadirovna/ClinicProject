from LibraryBook.ClassBasic.main import Category, Book


def category_CRUD():
    text="""
    1)Add
    2)Delete
    3)Update
    4)Show
    5)Back <-
      >>>"""
    key=int(input(text))
    obj=Category()
    match key:
        case 1:
            obj.add_category()
            category_CRUD()
        case 2:
            obj.delete_category()
            category_CRUD()
        case 3:
            obj.update_category()
            category_CRUD()
        case 4:
            obj.show_category()
            category_CRUD()
        case 5:
            admin_menu()


def book_CRUD():
    text = """
        1)Add
        2)Delete
        3)Update
        4)Show
        5)Back <-
          >>>"""
    key = int(input(text))
    obj=Book()
    match key:
        case 1:
            obj.add_book()
            book_CRUD()
        case 2:
            obj.delete_book()
            book_CRUD()
        case 3:
            obj.update_book()
            book_CRUD()
        case 4:
           Book().show_book()
           book_CRUD()
        case 5:
            admin_menu()


def admin_menu():
    text = """
    1)category
    2)book
    3)exit
    >>> """
    key = int(input(text))
    match key:
        case 1:
            category_CRUD()
        case 2:
            book_CRUD()
        case 3:
            return


admin_menu()