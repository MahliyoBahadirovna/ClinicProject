#READ QILIB PRINTTA TEXT FAYLDEGI JYFT SONLANI CHIQARADI
# a=open("text.txt","r")
# c=a.read()
# for i in c.split(","):
#     if not  int(i)%2:
#         print(i)
#a.close()
#
#
# <*>
#
# file = open('motion.txt', 'r')
# arr = list(map (str, file.read().split()))
#
# for i in range(len(arr)):
#     if i % 2 == 0:
#         arr[i] = "00"
#
# f = open('imtihon.txt', 'w')
#
# for i in range(len(arr)):
#     f.write(f'{arr[i]} ')
#
#
# <**>
#
# file = open('imtihon2.txt', 'r')
# arr = list(map (str, file.read().split()))
#
# for i in range(len(arr)):
#     if not i % 2 == 0:
#         arr[i] = arr[i] + ' ' + arr[i]
#
# f = open('imtihon2.txt', 'w')
#
# for i in range(len(arr)):
#     f.write(f'{arr[i]} ')
#
#
#
# <***>
#
#
# file = open('imtihon3.txt', 'r')
# arr = list(map (str, file.read().split()))
#
# for i in range(len(arr)):
#     arr[i] = arr[i].replace('  ', ' ')
#
# str = open('imtihon3.txt', 'w')
#
# for i in range(len(arr)):
#     str.write(f'{arr[i]} ')
#
#
#
#
# <****>
#
# s = input('s satr kiriting: ')
# s1 = input('s1 satr kiriting: ')
# s2 = input('s2 satr kiriting: ')
#
# s = s.replace(s1, s2, 1)
# print(f's sartdagi s1 satrlar s2 satri bilan almashtrildi:  {s}')
#
#
#
#
#  <*****>
#
# class Raqam:
#     def __init__(self, son: int):
#         self.son = son
#
#     def birlar(self):
#         satr = ''
#         self.xona = self.son % 10
#         if self.xona == 1:
#             satr = "bir"
#         elif self.xona == 2:
#             satr = "ikki"
#         elif self.xona == 3:
#             satr = "uch"
#         elif self.xona == 4:
#             satr = "tort"
#         elif self.xona == 5:
#             satr = "besh"
#         elif self.xona == 6:
#             satr = "olti"
#         elif self.xona == 7:
#             satr = "yetti"
#         elif self.xona == 8:
#             satr = "sakkiz"
#         elif self.xona == 9:
#             satr = "toqqiz"
#         else:
#             satr = "nol"
#         return satr
#
#     def onlar(self):
#         satr = ''
#         self.xona = self.son // 10 % 10
#         if self.xona == 1:
#             satr = "o'n"
#         elif self.xona == 2:
#             satr = "yigirma"
#         elif self.xona == 3:
#             satr = "o'ttiz"
#         elif self.xona == 4:
#             satr = "qirq"
#         elif self.xona == 5:
#             satr = "ellik"
#         elif self.xona == 6:
#             satr = "oltmish"
#         elif self.xona == 7:
#             satr = "yetmush"
#         elif self.xona == 8:
#             satr = "sakson"
#         elif self.xona == 9:
#             satr = "toqson"
#         return satr
#
#     def yuzlar(self):
#         satr = ''
#         self.xona = self.son // 100
#         if self.xona == 1:
#             satr = "bir yuz"
#         elif self.xona == 2:
#             satr = "ikki yuz"
#         elif self.xona == 3:
#             satr = "uch yuz"
#         elif self.xona == 4:
#             satr = "tort yuz"
#         elif self.xona == 5:
#             satr = "besh yuz"
#         elif self.xona == 6:
#             satr = "olti yuz"
#         elif self.xona == 7:
#             satr = "yetti yuz"
#         elif self.xona == 8:
#             satr = "sakkiz yuz"
#         elif self.xona == 9:
#             satr = "toqqiz yuz"
#         return satr
#
#
#
# b_son = int(input("son kiriting: (0<= son >= 999): "))
# son = Raqam(b_son)
# print(f'{son.yuzlar()} {son.onlar()} {son.birlar()}')
#
#
#
#
#
#
# <******>
#
# class COUNT_SYSTEM:
#     def __init__(self, number):
#         self.number = number
#
#     def sanoq_2(self):
#         sum2 = ""
#         while self.number > 0:
#             sum2 = str(self.number % 2) + sum2
#             self.number //= 2
#         return sum2
#
#     def sanoq_8(self):
#         sum8 = ""
#         while self.number > 0:
#             sum8 = str(self.number % 8) + sum8
#             self.number //= 8
#         return sum8
#
#     def sanoq_16(self):
#         sum16 = ""
#         while self.number > 0:
#             if (self.number % 16) == 10:
#                 sum16 = 'A' + sum16
#             elif (self.number % 16) == 11:
#                 sum16 = 'B' + sum16
#             elif (self.number % 16) == 12:
#                 sum16 = 'C' + sum16
#             elif (self.number % 16) == 13:
#                 sum16 = 'D' + sum16
#             elif (self.number % 16) == 14:
#                 sum16 = 'E' + sum16
#             elif (self.number % 16) == 15:
#                 sum16 = 'F' + sum16
#             else:
#                 sum16 = str(self.number % 16) + sum16
#             self.number //= 16
#         return sum16
#
# n = int(input("son kiriting: "))
# obj2 = COUNT_SYSTEM(n)
# obj8 = COUNT_SYSTEM(n)
# obj16 = COUNT_SYSTEM(n)
# print(obj2.sanoq_2())
# print(obj8.sanoq_8())
# print(obj16.sanoq_16())
#
#
#
#
#
#
#
#
# kerak bo'ladi
#
#
# def num2word(m):
#     s1 = m // 100
#     s2 = (m // 10) % 10
#     s3 = m % 10
#
#     birlik = {
#         0: '',
#         1: 'bir',
#         2: 'ikki',
#         3: 'uch',
#         4: "to'rt",
#         5: 'besh',
#         6: 'olti',
#         7: 'yetti',
#         8: 'sakkiz',
#         9: "to'qqiz",
#     }
#     onlik = {
#         0: '',
#         1: "o'n",
#         2: "yigirma",
#         3: "o'ttiz",
#         4: "qirq",
#         5: "ellik",
#         6: "oltmish",
#         7: "yetmish",
#         8: "sakson",
#         9: "to'qson",
#     }
#     if s1 != 0:
#         son1 = birlik[s1] + 'yuz'
#     else:
#         son1 = ''
#     son2 = onlik[s2]
#     son3 = birlik[s3]
#     son = son1 + ' ' + son2 + ' ' + son3
#
#     return son.strip()
#
#
#
# nollar = {
#     1: 'ming',
#     2: 'million',
#     3: 'milliard',
#     4: 'trillion'
# }
# n = int(input("n= "))
# num = num2word(n % 1000)
# n //= 1000
# i = 1
# while n > 0:
#     num = num2word(n % 1000) + ' ' + nollar[i] + ' ' + num
#     n //= 1000
#     i += 1
#
# print(num.strip())
# #
#
# fayldan hamma qiymatni ochirib  faqat juft sonlanigina yozadi
# a=open("text.txt","r")
# c=a.read()
# a.close()
# a=open("text.txt","w")
# f=''
# for i in c.split(","):
#     if not int(i)%2:
#         f+=i
# a.write(",".join(f))
# a.close()
# qiymatni ochirmastan juftlani yengi linega qowiw
# a=open("text.txt","r")
# c=a.read()
# a.close()
# a=open("text.txt","a")
# f=''
# for i in c.split(","):
#     if not int(i)%2:
#         f+=i
# a.write("\n"+",".join(f))
# a.close()
#
#
#

# yulduzcha 1 *********************
# a=open("text.txt","r")
# c=a.read()
# a.close()
# a=open("text.txt","w")
# star_num=int(input())
# for i in range(star_num):
#     for j in range(star_num):
#         if i==j:
#             a.write("*   ")
#         else:
#             a.write("   ")
#     a.write("\n")
# yulduzcha 2***********************
# n = int(input())

# file = open("text.txt" , 'w')
#re = ""
# for i in range(n, 0,-1):
#     if i == 1:
#         re += "\t" * (n - i) + "*"
#    else:
        # re += "\t"*(n-i)+"*" + "\t"*(i*2-2) + "*" + "\n"

# file.write(re)
# file.close()

# yulduzchamas uchburce 3*****************
#n = int(input/










