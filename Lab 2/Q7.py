def avg(temp):
    avrg = 0
    for i in range(len(temp)):
        avrg += temp[i]
    return avrg / len(temp)
    
def highLow(temp):
    low = temp[0]
    high = temp[0]
    for i in range(len(temp)):
        if high < temp[i]:
            high = temp[i]
        if low > temp[i]:
            low = temp[i]
    return low,high
    
def ascending(temp):
    for i in range(len(temp)-1):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                check = temp[i]
                temp[i] = temp[j]
                temp[j] = check
    
    return temp
    
def remove(temp,day):
    if 0 <= day < len(temp):
        temp.pop(day)
    else:
        print("Day index out of range.")
    return temp

temp = [4,2,3,1,5,6,7,8,9,10,11,12,14,15,18,17,18,95,98,45,78,54,58,5,25,21,48,95,85,87]
print(avg(temp))
print(highLow(temp))
print(ascending(temp))
print(remove(temp,4))
