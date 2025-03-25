def fun():
    print("This is the fun() function.")
def msg():
    print("This is the msg() function.")
def disp():
    print("This is the disp() function.")
functions_list=[fun,msg,disp]
for func in functions_list:
    func()

output:
This is the fun() function.
This is the msg() function.
This is the disp() function.
