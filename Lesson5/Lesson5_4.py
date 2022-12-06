
a=float(input())
c=input()
b=float(input())

if c=='+': print (a + b)

if c=='-': print (a-b)

if c=='/' and b ==0.0: print("Деление на 0!")

if c=='/' and b!=0.0 : print(a/b)

if c=='*': print(a*b)

if c=='pow': print(a**b)

if c=='div' and b==0.0: print("Деление на 0!")

if c=='div' and b!=0.0: print(a//b)

if c=='mod' and b==0.0: print ("Деление на 0!")

if c=='mod' and b!=0.0: print (a%b)