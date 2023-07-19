# matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# matrix = [[7,8],
#           [1,2]]
# minm=0
# l=[]
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j]==max(matrix[j])-1:
#             minm=min(matrix[j])
#
# l.append(minm)
# print(l)
# grid = [
#     [1,0] , [0,2]
# ]
# count=0

# for i in grid:
#     count +=  max(i)
#     for j in i:
#         if j != 0:
#             count += 1
#
# for i in zip(*grid):
#     count += max(i)
# print(count)

# mat = [
#     [0, 1],
#     [1, 1]
# ]
#
# index, count = 0, 0
# for i in range(len(mat)):
#     if (c := mat[i].count(1)) > count:
#         count = c
#         index = i
# print([index, count])
#
# grid = [
#     [1, 2, 4],
#     [3, 3, 1]
# ]
# c = 0
# for _ in range(len(grid[0])):
#     max_ = float("-inf")
#     for j in grid:
#         max_ = max(max_ , max(j))
#         del j[j.index(max(j))]
#     c += max_
# print(c)


# matrix = [
#     [3, 7, 8],
#     [9, 11, 13],
#     [15, 14, 17]
# ]
#
# for i in zip(*matrix):
#     m = max(i)
#     if m == min(matrix[i.index(m)]):
#         print([m])
#         break
# grid = [
#     [9, 9, 8, 1],
#     [5, 6, 2, 6],
#     [8, 2, 6, 4],
#     [6, 2, 2, 2]]
#
# r = []
# for i in range(len(grid) - 2):
#     l = []
#     m , n = 0 , 2
#     for j in range(len(grid[0]) - 2):
#         max_ = max([max(grid[k+i][m : n + 1]) for k in range(3)])
#         l.append(max_)
#         m += 1
#         n += 1
#     r.append(l)
# print(r)

# rows = 2
# cols = 2
# rCenter = 0
# cCenter = 1
# # r = []
# #
# # if rows >= cols:
# #     for i in range(rows):
# #         for j in range(cols):
# #             r.append([abs(i - rCenter) , abs(j - cCenter)])
# #
# #
# # else:
# #     for i in range(cols):
# #         for j in range(rows):
# #             r.append([abs(j - rCenter), abs(i - cCenter)])
# # print(r)
# res = []
# for r in range(rows):
#     for c in range(cols):
#         res.append([r, c])
#
# res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
# print(res)
from string import ascii_lowercase

board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
row=[]
col=[]
s=0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j]=='R':
            row,col=i,j
r=''.join(board[row]).replace(".",'')
c="".join(list(zip(*board))[col]).replace(".",'')
f=r.index('R') # R ning indeksini fga yukladim
f1=c.index('R')
s+= 0 if f==0 else r[f-1 ] in ascii_lowercase
s+=0 if f==len(r)-1 else r[f+1 ] in ascii_lowercase
s+= 0 if f1==0 else c[f1-1] in ascii_lowercase
s+= 0 if f1==len(c)-1 else c[f1+1] in ascii_lowercase
print(s)











