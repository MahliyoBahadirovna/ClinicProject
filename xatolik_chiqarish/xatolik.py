# def register(fullname,phone_number,password):
#     if len(fullname.split())<2:
#         raise Exception("Fullname must be at least 2 characters")
#     if len(phone_number)!=13:
#         raise Exception("Phone number must be 13 characters")
#     if len(password)<4:
#         raise Exception("Password must be at least 4 characters")



# try:
#     fullname=input("Fullname:")
#     phone_number=int(input("Phone number:"))
#     password=int(input("Password:"))
#     register(fullname,phone_number,password)
# except Exception as e:
#     print(e)

import  json
with open("post.json" , "r") as file:
      data = json.load(file)
count=0
for i in data:
    if len(i.get("title").split())==1:
        count+=1
print(count)
