list1=[2,3,6,6,7]
max=0
max1=0
i=0
while i<len(list1):
    if list1[i]>max:
        max=list1[i]
    i+=1

i=0
while i<len(list1):
    if list1[i]>max1 and list1[i]!=max:
        max1=list1[i]
    i+=1
print(max1)

