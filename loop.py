i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end='')
        j = j + 1
    print()  
    i = i + 1
    # table
    x=int(input("enter no :"))
    for y in range(1,11):
        print(x*y)