def func(spisok, slovar):
    for i in spisok:
        if slovar.get(i):
            slovar[i] += 1
        else:
            slovar[i] = 1
spisok=[1, 1, 1, 1, 1, 2 ,2 ,2 ,2 ,2 ,3 ,3, 3, 4,4,4,5,5,5,9,9,9,9,9,9,9,8,8,7,7]
slovar={}
func(spisok,slovar)
print(slovar)