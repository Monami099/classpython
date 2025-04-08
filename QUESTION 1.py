def count_names():
    name='monami'
    with open("myname.txt","w") as file:
         file.write(monami,monami,monami)
    with open("myname.txt","r") as file:     
         data=file.read()
         
    count=data.count(name)
    print(f"{count}")
