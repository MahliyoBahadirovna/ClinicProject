import json

# json.loads()
# json.dumps()

# json.load()
# json.dump()

# a = {1, 2, 3, 4, 5}
# print(type(a))
# a = json.dumps(a) # dumps -> str xolatga aylatiradi
# print(type(a) , a)
# a = json.loads(a) # loads -> str xolatdan chiqazadi
# print(type(a), a)
# temp= {
#     1:True,
# }
# with open("test.json" , "w") as file:
#     json.dump(temp , file , indent=3)
#

# with open("test.json" , "r") as file:
#     print(json.load(file))
#qayta qayta qowadi tempni
# with open("text.json" , "r") as file:
#     data=(json.load( file))
# data.append(temp)
# with open("text.json","w") as file:
#     json.dump(data,file,indent=3)


#HAR 1TA RUN QGANDA 1 QOWIB KETADI

# with open("text.json" , "r") as file:
#     data = json.load(file)
#
# if not data:
#     tmp = {1 : True}
#
# else:
#     id_=int(list(dict(data[-1]).keys())[0])+1
#     tmp = {id_:True}
# data.append(tmp)
# with open("text.json","w") as file:
#     json.dump(data,file,indent=3)


#import yaml
#YAML FAYL**************************************
# pip install pyyaml
# import yaml
#
# users = [{'name': ['John Doe','das'], 'occupation': 'gardener'},
#          {'name': ['Lucy Black','dfsd'], 'occupation': 'teacher'}]
#
# with open('my_yaml.yaml', 'w') as f:
#     print(yaml.dump(users,f))
#
# with open('my_yaml.yaml', 'r') as f:
#     print(yaml.load(f, Loader=yaml.FullLoader))



# home task

# n=input()
# maks=n.split()[0]
# for i in n.split():
#     if len(i)>len(maks):
#         maks=i
# print(maks)

# for i in dir(dict):
#     if i in "_":
#         print(i)
# s=input()
# r=[]
# for i in s.split():
#     r.append(i[::-1])
# print(*r)












