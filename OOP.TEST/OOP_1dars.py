# 4ta object addda qowiw
# class Kalkulyator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#
#
#     def add(self):
#         return  self.a+self.b
#
# obj=Kalkulyator(5,10)
# obj1=Kalkulyator(15,85)
# obj2=Kalkulyator(5,15)
# obj3=Kalkulyator(5,1)
#
# print(obj.add())
# print(obj1.add())
# print(obj2.add())
# print(obj3.add())

#multilevel
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass


#multiple
# class  A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass

#single
# class A:
#     pass
#
# class B(A):
#     pass


#
# class C:
#     pass
# class B(C):
#     pass
# class A(C):
#     pass



#gibrid
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C:
#     pass
#
# class D(B,C):
#     pass
#classda countini topw
# class MyStr():
#     def __init__(self,val):
#         self.val=val
#     def count(self,x):
#         c=0
#         for i in range(len(self.val)):
#             if self.val[i:i+len(x)]==x:
#                 c+=1
#         return c
#
#
#
# a=MyStr('878')
# print(a.count("8"))

# STRING METHOD:
# replace >>>>>>
# split >>>>>>
# join >>>>>>
# capitalize >>>>>>>
# casefold
# title >>>>>>
# count >>>>>>>
# find >>>>>>
# index
# ljust
# lower
# lstrip
# strip
# upper
# startswith
# endswith

class MyStr():
    def __init__(self,val)-> None:
        self.val=val
    def index(self,sub:str,start:int=None , end:int=None):
        if not sub in self.val:
            raise ValueError("substring not found ")
        val = self.val[start:end]
        for i, v in enumerate(self.val):
            if val[i:i + len(sub)] == sub:
                return i + start
    def replace(self ,old:str,new:str,count:int=None)->str:
        if count==None:
            count=len(self.val)
        re=''
        c=0
        while len(self.val)-1>=c:
            if self.val[c:c+len(old)]==old and count:
                re+=new
                c+=len(old)
                count-=1
                continue
            re+=self.val[c]
            c+=1
        return re
    def count(self ,x:str, start:int=None , end:int=None)-> int :
        c=0
        val=self.val[start:end]
        for i in range(len(val)):
            if val[i:i+len(x)]==x:
                c+=1
        return c
    def split(self,sep:str =' ',maxsep:int=None) -> list:
        if maxsep==None:
            maxsep=len(self.val)
        tmp=self.val
        re=[]
        c=0
        for i in range(len(self.val)):
            if self.val[i:i+len(sep)]==sep and maxsep:
                re.append(tmp[:c])
                tmp=self.val[i+len(sep):]
                c=0
                maxsep-=1
            c+=1
        if sep in self.val:
            return [re[0]] + [i[:-len(sep)]for i in re[1:]]+[tmp]
        return [self.val]
    def capitalize(self)->str:
        ascci = ord(self.val[0])
        if 97 <= ascci <= 122:
            return chr(ascci - 32) + self.val[1:]
    def title(self)->str:
        s=""
        for i in MyStr(self.val).split():
            if 97<=(c:=ord(i[0]))<=122:# c ozgaruvchiga tengladik
                s+=chr(c-32)+i[1:]+' '
        return s
    def find(self,x,start:int=None , end:int=None)->int:
        val = self.val[start:end]
        for i, v in enumerate(self.val):
             if val[i:i+len(x)]==x:
                return i+start
        return -1
    def join(self,iterable: list|set|str|tuple)->str:
        if True in [isinstance(i,int)for i in iterable]:
            raise TypeError("sequence item:expected str instance,int found")
        re=''
        for i in iterable:
            re+=i+self.val
        if self.val:
            return re[:-len(self.val)]
        else:
            return re
    def upper(self) -> str:
            s=''
            for i in self.val:
                if 97 <= ord(i) <= 122:
                    s+=chr(ord(i) - 32)
            return s
    def startswith(self,x:str,start:int=None,end:int=None )->bool:
        val=self.val
        for i in range(len(val[start:end])):
            if val[0:len(x)]==x:
                return True
            return False
    def endswith(self,x:str,start:int=None,end:int=None )->bool:
        val=self.val
        for i in range(len(val[start:end])):
            if val[0:-len(x)]==x:
                return True
            return False
    def lower(self)-> str:
            s=""
            for i in self.val:
                 if 65<= ord(i) <=90:
                     s+=chr(ord(i)+32)
            return s
    def casefold(self)-> str:
            s=""
            for i in self.val:
                 if 65<= ord(i) <=90:
                     s+=chr(ord(i)+32)
            return s
    def strip(self,x: str=" ") -> str:
        s=""
        for i in range(len(self.val)):
            if not self.val[i] in x:
                s+=self.val[i:]
                break
        for i ,v in enumerate(s[::-1]):
            if not v in x:
                s=s[:-i]
                break
        return s
    def lstrip(self,x:str=" ")->str:
        s = ""
        for i in range(len(self.val)):
            if not self.val[i] in x:
                s += self.val[i:]
                break
        return s
    def rstrip(self,x:str=" ")->str:
        s=""
        for i ,v in enumerate(self.val[::-1]):
            if not v in x:
                s+=self.val[:-i]
                break
        return s
    def ljust(self,n:int,x:str=" ")-> str:
        d=self.val
        while len(d)<n:
            d+=x
        return d
    def rjust(self,n:int,x:str=" ")-> str:
        d=''
        while len(d)<n-len(self.val):
            d+=x
        return d+self.val

#ENDSWITH
# h=MyStr("salom hammmaga>")
# print(h.endswith(">"))


#REPLACE
# h=MyStr("salom hammmaga111111")
# print(h.replace('1',"K",1))
#INDEX
#a=MyStr("salom")
#print(a.index("s"))

# REPLACE
# print(a.replace("s","m"))

#JOIN
#print(MyStr(" ").join(["1","2"]))

# COUNT
# c=MyStr("samlomm")
# print(c.count("m",1,-1))

#SPLIT
# d=MyStr("sal|sal")
# print(d.split("|")) #1 indexdan

#CAPITALIZE
# e=MyStr("salom")
# print(e.capitalize())

#TITLE
#f=MyStr("salom salom")
#print(f.title())
#print(f.find("al",4))


#CASEFOLD
# F=MyStr("SALOM")
# print(F.casefold())


#UPPER
# g=MyStr("salom")
# print(g.upper())

#LOWER
# h=MyStr("SALOM")
# print(h.lower())

#STARTSWITH
# h=MyStr("salom hammmaga")
# print(h.startswith("salom"))

# #ENDSWITH
# h=MyStr("salom hammmaga non>")
# print(h.startswith(">"))


#STRIP
# j=MyStr("aaaaaaasalomaaaaa")
# print(j.strip("a"))

#LSTRIP
# j=MyStr("aaaaaaasalomaaaaa")
# print(j.lstrip("a"))

#RSTRIP
# j=MyStr("aaaaaaasalomaaaaa")
# print(j.rstrip("a"))

#LJUST
# a=MyStr("SAlom")
# print(a.ljust(10))

#RJUST
# a=MyStr("SAlom")
# print(a.rjust(10,"-"))

# STRING METHOD:
# replace +
# split +
# join +
# capitalize +
# casefold +
# title +
# count +
# find +
# index +
# ljust +
# rjust +
# lower +
# lstrip
# strip +
# upper +
# startswith +
# endswith +

