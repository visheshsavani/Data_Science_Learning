# a = input("Enter your favourite movie 1")
# b = input("Enter your favourite movie 2")
# c = input("Enter your favourite movie 3")
# list = [a,b,c]
# print(list)
##
# list = [1,"abc","abc",2]
# list1 = list.copy()
# list1.reverse()
# if(list1 == list):

#     print("the list is a palindrome")
# else:
#     print("the list is not a palindrome")
##
tup  = ("B","D","A","C","E","A","C","D")
list = [tup]
print(type(list))
list.sort()
print(list)
print(list[0])
print(tup.count("A"))