# 1
a=("a","b","c")
b=("a","b","c")
c=("a","b","c")
print(id(a),id(b),id(c))

#2
d=["a","b","c"]
e=("a","b","c")
print (id(d),id(e))

# 3
a=["a","b","c"]
b=["a","b","c"]
c=["a","b","c"]
d=("a","b","c")
e=("a","b","c")
print(id(a),id(b),id(c),id(d),id(e)),'/n'
#или так
text1= "a,b,c"
text2= "a,b,c"
text3= "a,b,c"
text4= "a,b,c"
text5= "a,b,c"
txt1=list(text1)
txt2=list(text2)
txt3=list(text3)
txt4=tuple(text4)
txt5=tuple(text5)
print(id(txt1),id(txt2),id(txt3),id(txt4),id(txt5),txt5,txt4)