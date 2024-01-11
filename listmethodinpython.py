a=["ram",10,"shyam",12.5]
b=len(a)
print("length of list=",b)
a=[10,20,30,40,50]
b=max(a)
print("max value in the list=",b)
print("min value in the list=",min(a))
list1 = [2, 4, 5, 6, 7]
list2 = [2, 4, 5, 6, 7]

result = cmp(list1, list2)

if result == 0:
    print("Lists are equal")
elif result < 0:
    print("List1 is less than List2")
else:
    print("List1 is greater than List2")