list1=list(range(1,101))
list2=[x*10 for x in list1 if x%10==0 if x%4!=0]
print(list2)
list3=[x*2 for x in list1 if x%10!=0 if x%4==0]
print(list3)