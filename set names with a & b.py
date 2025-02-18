names_set={"Aryan","Bina","Ayushi","Bobby","Arnab","Bita"}
a_names={name for name in names_set if name.startswith("A")}
b_names={name for name in names_set if name.startswith("B")}
print("names starting with A:",a_names)
print("names starting with B:",b_names)
