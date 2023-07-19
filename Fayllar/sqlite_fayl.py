import  sqlite3

con=sqlite3.connect('test.sqlite') # connect open vazifasini bajaradi
cur=con.cursor()
# connect open vazifasini bajaradi
# cursor biz yozadigan QUERYarni yuboruvchi (iwlatubvchi)  metod
# cursorning ichidagi execute yaratib beradi
#faylga qandaydir ozgartiruvchi qowsak commitdan foydalananmiz
# primary key ---> unik qb beradi
# autoincrement bu avtomaticiskiy id yoq bosa yaratib beradi
#varchar bu text kirgizamiza unda biza uzunligini beriwimiza mumkin varchar(50)
#fullname varchar(255) not null bow boliwi mumkinmas
# fulname varchar(255) unique faqat 1ta boliw kere qaytib iwlatiw mumkinmas
query="""
    create table users(
            id integer  primary  key autoincrement,
            fullname varchar(255) ,
            phone_number varchar (20) 
    );
"""

fullname = input()
phone_number = input()

user1 = """
    insert into users(fullname, phone_number) values (? , ?)
"""


cur.execute(user1, (fullname , phone_number))
con.commit()

select_query="""
    select id,fullname,phone_number from users where  fullname='Mahliyo';
"""
delete_query="""
    delete from users where  id=3
"""
update_query="""
    update users set fullname = 'Komol' where phone_number='+998977093415'
"""


# cur.execute(user1) buni yaratkanda iwlatiladi
# con.commit()
#
# cur.execute(user1)
# con.commit()
