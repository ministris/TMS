def rec(some_list):
    assert (some_list)!=0
    next = some_list[0]
    for i in some_list:
        if next < i:
            next = i
    return next
list5 = [2, 1, 0, 5, 7, 6, 4, 3]
otvet = rec(list5)
print(otvet)


