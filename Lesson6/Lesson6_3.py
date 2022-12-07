
tuple = ("саша", "маша", "даша", "наташа", "проорп", "статс",)
clon = filter(lambda x: x if x[::1] == x[::-1] else plug.append(x), tuple)
plug = []
print(list(clon))
