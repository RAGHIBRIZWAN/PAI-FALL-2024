list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []

for i in range(2):
    for j in range(2):
        list3.append(list1[i] + list2[j])
        
print(list3)
