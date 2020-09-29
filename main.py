def add(x,y):
return x+y
def sub(x,y):
return x-y
def mul(x,y):
return x*y
def div(x,y):
return x/y

print("select")
print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for division")

i=input("press ")
a=int(input("enter any no"))
b=int(input("enter any no"))

switch(i)
case'+': sum=add(a,b)
         print("sum is",sum)
         break
case '-': ans=sub(a,b)         
           print("ans is",ans)
         break
 case '*': ans=mul(a,b)         
           print("ans is",ans)
         break
case '/': ans=div(a,b)         
           print("ans is",ans)
         break
 default: print("no operation")
 
         
