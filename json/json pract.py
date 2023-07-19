import json

def get_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data
def save_data(filename,data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=3)

def add_product(**kwargs):
    data=get_data('test.json')
    if data:
        id_=data[-1].get("id")+1
    else:
        id_=1

    kwargs.update({"id": id_})
    data.append(kwargs)

    save_data("test.json",data)
    print("Product add successful!")
def all_product():
    data=get_data('test.json')

    text=''
    for tar_r,val in enumerate(data,1):
        text+=f"{tar_r}){val.get('name')} {val.get('price')} {val.get('count')}\n"
    print(text)

def delete_product(num):
    data = get_data('test.json')
    del data[num]
    with open("test.json", "w") as f:
        json.dump(data, f, indent=3)

def update_product(column ,val, num):
    data:list[dict]=get_data("test.json")
    data[num][column]=val
    save_data("test.json", data)
    print("Product update successful!")




def UI():
    while True:
        text = """
            1) add product
            2) all product
            3) delete product
            4) update product
            5) exit
            >>>"""
        key = input(text)
        if key == '1':
            name = input("name: ")
            price = int(input("price: "))
            count = int(input("count: "))
            add_product(name = name , price = price ,count = count )
        elif key == '2':
            all_product()
        elif key == '3':
            all_product()
            key = int(input('>>>')) - 1 # 1
            delete_product(key)
        elif key=="4":
            text="""
            1) name
            2) price
            3) count
            0) back
            """
            key=int(input(text))
            if  key!=0:
                val=input("new value: ")
            else:
                continue
            if key==1:
                all_product()
                num=int(input(">>>"))-1
                update_product("name",val,num)
            elif key==2:
                all_product()
                num = int(input(">>>")) - 1
                update_product("price", val, num)
            elif key==3:
                all_product()
                num = int(input(">>>")) - 1
                update_product("count", val, num)
        elif key == '5':
            break

UI()