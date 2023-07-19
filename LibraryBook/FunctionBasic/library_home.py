import random
import json
from string import ascii_lowercase
from datetime import  date

print(date.today())
category = {1 : "BADIY" , 2: "ILMIY" , 3:"DRAMATIK"}
session_user=None

def get_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=3)

def random_card_id():
    a = list(ascii_lowercase)
    random.shuffle(a)
    cart_id = str(hash(a.pop())).lstrip('-')[:8]
    return cart_id

def show_category():
    for k, v in category.items():
        print(f"{k}) {v}")
    print(f"{k + 1}) <- back")
    return k


def admin_menu():
    menu = """
    1) add book
    2) delete book
    3) update book
    4) log out
        >>>"""
    key = input(menu)
    match key:
        case "1":
            k = show_category()
            key = int(input('>>>'))
            if key == k+1:
                admin_menu()
            category_id = key
            books: list[dict] = get_data("books.json")

            if not books:
                new_id = 1
            else:

                new_id = books[-1]["id"] + 1
            d = {
                "id" : new_id,
                "category_id" : category_id,
                "name" : input("Book Name:"),
                "author" : input("Book Author:"),
                "count" : int(input("Book Count: "))
            }
            books.append(d)
            save_data("books.json", books)
            print("Successful append !")
            admin_menu()

        case "2":
            k = show_category()
            key = int(input('>>>'))
            if key == k + 1:
                admin_menu()
            category_id = key
            books: list[dict] = get_data("books.json")
            for i , v in enumerate(books , 1):
                if v["category_id"] == key:
                    print(f"{i}) {v.get('name')}")
            print("0) <- back")
            key = int(input('>>>'))
            if key == 0:
                admin_menu()
            else:
                delete_product: dict = books.pop(key-1)
                save_data("books.json", books)
                print(f"Success delete ! {delete_product.get('name')}")
                admin_menu()



        case "3":
                k = show_category()
                key = int(input('>>>'))
                if key == k + 1:
                    admin_menu()
                category_id = key
                books: list[dict] = get_data("books.json")
                for i, v in enumerate(books, 1):
                    if v["category_id"] == key:
                        print(f"{i}) {v.get('name')}")
                print("0) <- back")
                key = int(input('>>>'))
                if key == 0:
                    admin_menu()
                else:
                    field_key="""
                    1) name
                    2)author
                    3)count
                    4) back
                    """
                filed=int(input(field_key))
                new_val=input("new value  ")
                if filed ==4:
                    admin_menu()
                match  filed:
                    case 1:
                        filed="name"
                    case 2:
                        filed="author"
                    case 3:
                        filed="count"

                books[key-1][filed]=new_val
                save_data("books.json", books)
                print("Success upgrade ! ")
                admin_menu()



        case "4":
            return

def register():
    users:list[dict]=get_data("users.json")
    if users:
        new_id=users[-1]["id"]+1
    else:
        new_id=1
    d={
        "id":new_id,
        "Fullname": input("Fullname: "),
        "phone_number": input("phone_number: "),
        "card_id": random_card_id(),
        "books":[],
        "created_at ": str(date.today())
    }
    for i in users:
        if i ["phone_number"]== d["phone_number"]:
            print("Your phone number already exists !")
            return

    users.append(d)
    save_data("users.json", users)
    print(f"Success register! Your card_id : {d['card_id']}")


def Edit_account(column ,val, num):
    data:list[dict]=get_data("users.json")
    data[num][column]=val
    save_data("users.json", data)
    print("edited successful!")


def account_menu():
    menu = """
        1) books
        2) settings
        3) log out
    """
    key = int(input(menu))
    match key:
        case 1:
            k = show_category()
            key = int(input('>>>'))
            if key == k + 1:
                return
            category_id = key
            books: list[dict] = get_data("books.json")
            for i, v in enumerate(books, 1):
                if category_id == v.get("category_id"):
                    print(f"{i}) {v.get('name')}")
            print("0) <- back")
            book_position = int(input('>>>'))
            if book_position == 0:
                account_menu()
            book_name = books[book_position - 1]['name']
            users = get_data('users.json')
            for i in users:
                if session_user.get('id') == i.get("id"):
                    i["books"].append(book_name)
            save_data("users.json", users)

        case 2:
            menu = """
                1) Edit account
                2) Delete account
                3) <- back
                >>> 
                """
            key = int(input(menu))
            match key:
                case 1:
                    menu = """
                        1) fullname
                        2) phone_number
                        3) <- back
                        >>> 
                    """
                    key = int(input(menu))
                    if key != 3:
                        val = input()
                    else:
                        return
                    if key == 1:
                        new_name = input("New Fullname: ")
                        users: list[dict] = get_data("users.json")
                        for i in users:
                            if session_user.get('id') == i.get("id"):
                                i['Fullname'] = new_name
                        save_data("users.json", users)
                        print("Fullname successfully upgraded !")
                    elif key == 2:
                        new_number = input("New phone number: ")
                        users: list[dict] = get_data("users.json")
                        for i in users:
                            if session_user.get("id") == i.get("id"):
                                i['phone_number'] = new_number
                        save_data("users.json", users)
                case 2:
                    pass
                case 3:
                    return
        case 3:
            return


def login():
    global session_user
    phone_number:str=input("Enter your phone number:  ")
    card_id: str=input("enter your card id")
    users:list[dict]= get_data("users.json")
    for i in users:
        if i.get("phone_number")==phone_number and i.get("card_id")==card_id:
            print(f"Welcome {i.get('Fullname')}")
            sassion_user=i
            account_menu()
            break
        else:
            print(f"Wrong phone_number or card_id !")
def UI():
    while True:
        text = """
        1) ADMIN
        2) READER
        3) exit
        >>>"""
        key = int(input(text))
        match key:
            case 1:
                password = input("password : ")
                if password == "1234":
                    admin_menu()
                else:
                    print("Password xatto!")
                    continue
            case 2:
                text = """
                1)Register 
                2)Login
                3) <- back
                """
                key=int(input(text))
                match key:
                    case 1:
                        register()
                    case 2:
                        login()
                    case 3:
                        continue

            case 3:
                break


UI()

