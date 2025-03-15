a=int(input("enter num1="))
b=int(input("enter num2="))
c=int(input("enter num3="))
if(a>b and a>c):
  print("largest=",a)
elif(b>a and b>c):
  print("largest=",b)
else:
  print("largest=",c)
if(a<b and a<c):
  print("smallest=",a)
elif(b<a and b<c):
  print("smallest=",b)
else:
  print("smallest=",c)
