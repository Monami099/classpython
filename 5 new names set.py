names_set=set()
names_set.add("Maya")
names_set.add("Bina")
names_set.add("Charls")
names_set.add("Dev")
names_set.add("Eric")
print("set after adding names:",names_set)
if "Charls" in names_set:
    names_set.remove("Charls")
    names_set.add("Charls")
print("set after modifying a name:",names_set)
names_set.discard("Maya")
names_set.discard("Eric")
print("set after dleleting names:",names_set)

output:
set after adding names: {'Dev', 'Maya', 'Charls', 'Eric', 'Bina'}
set after modifying a name: {'Dev', 'Maya', 'Charls', 'Eric', 'Bina'}
set after dleleting names: {'Dev', 'Charls', 'Bina'}
