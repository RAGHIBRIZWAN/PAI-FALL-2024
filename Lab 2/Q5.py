def listmul(mult):
    mul = 1
    for i in range(len(mult)):
        mul *= mult[i]

    return mul

mult = [2, 3, 4, 5]
print(listmul(mult))
