# it=iter([1,5,3,6,2,8,7,9,4])
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__iter__())
# while True:
#     try:
#         print(it.__next__(),end=' ')
#     except StopIteration:
#         break
# print()


# for k in result:
#    print(k)


# def is_prime(n):
#     k=0
#     for i in  range(1,n+1):
#         if n % i ==0:
#             k+=1
#     return k==2
#
#
# f=open('test.txt','r')
#
# it =iter([i for i in f.read().split()])
#
# while True:
#     try:
#         element=it.__next__()
#         if is_prime(int(element)):
#             print(element,end=' ')
#     except StopIteration:
#         break
# print()

#""" iter - adres qaytaradi
#     next= har 1 nextda index oqidi
#     massivdan farqi  bu tez iwlidi indexsi yoq unga murojat qib bomidi
#     iteratorni lictta yoki dictka orab iwlatamiza (),[]
#     xotiradan kam joy egallidi
#
#     """