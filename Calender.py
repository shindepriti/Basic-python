def maxno(num):
 max=num[0]
 min=num[0]
 for data in num:
    if data > max:
        max=num
    elif data < min:
        min=data

 return max,min
print(maxno([9,6,7,4]))
