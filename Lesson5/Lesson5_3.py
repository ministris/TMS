
list2 = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,9,9,9,8,8,8,7,7,4,4,41,5,1,12,2]
dict13 = {}
for x in list2:
    if dict13.get(x, None):
        dict13[x] += 1
    else:
        dict13[x] = 1
print(dict13)


