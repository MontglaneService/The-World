print("please enter a number between 1 and 20: ")
x = input()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = len(a)
low = 0
high = y - 1
found = False
while low <= high:
    mid = (low + high)/2
    if a[mid]is x:
        found = True
        break
    elif a[mid] < x:
         low = mid + 1
    else:
        high = mid - 1
if found is True:
    print("{0} was found in the array." .format(x))
else:
    print("You didn't follow directions.")