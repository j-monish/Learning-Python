# expenses=[1200,1300,1500,1700,1500,1700,1500,1700]

# For loop working
# for i in range(0, len(expenses)):
#     print(f"Month:{i+1}")
#     print("expense:", expenses[i])


# # Created for efficiency 
# for i in expenses:
#     print("month","i:")
# j=0
#     j=j + (i)
# print(j)
# for j in range(0,len(expenses)):
#     print("month:", j)
# for i in expenses:
#     print(i)
# for i in range(0,len(expenses)):
#     print("month:", i+1)
#     print("expense:", expenses[i])


# Pattern printing problems

# a=" *"
n=int(input("n:"))

# *
# **
# ***
# ****
# *****

# for i in range(1,n):
#     print(a*i)

#     *
#    **
#   ***
#  ****
# *****

# b=" "
# for i in range(1,n+1):
#     print(b*(n-i), a*i,a*i)



#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# for i in range(0,n+1):
#      print(b*(n-i), a*i) 
# for j in range(1,n):
#     print(b*j, a*(n-j))




#     *
#    ***
#   *****
#  *******
# *********
# b=" "
# for i in range(1,n):
#     print(b* (1-i))

# 1
# 12
# 123
# 1234
# 12345

# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j, end=' ')
#     print('\n')


#    2
#   4 6
#  8 10 12
# 14 16 18 20

# for i in range (1,n+1):  
#         for j in range ((i**2)-i+2,(i**2)+i+1,2):
#         #       if j%2==0:
#                 print(j, end=' ')
#         print('\n')

# *****
# *   *
# *   *
# *   *
# *****
# a="*"

# for i in range(1,n+1):
#         if i==1 or i==n:
#                 print(a*n)
#         else:
#                 print("*"," "*(n-2),"*", sep="")

# print("mohit", "monish", "aman")

# 1
# 22
# 333
# 4444
# 55555
# for i in range(0,n+1):
#         print(f"{i}"*i)

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# j=1
# for i in range(1,n+1):
#         for j in range(j,j+i):
#                 print(j, end=' ')
#         j=j+1
#         print('\n')


# 0 1 1 2 3 5 8
a=0
b=1
i=a+b
for i in range(0,n):
    i=i+a+b
    print(i)








