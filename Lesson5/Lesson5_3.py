def my_f(spisok, slovarik):
    for i in spisok:
        if i in slovarik:
            slovarik[i] += 1
        else:
            slovarik[i] = 1

list = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,9,9,9,8,8,8,7,7,4,4,41,5,1,12,2]
dict1 = {}
my_f(list, dict1)
print(dict1)




