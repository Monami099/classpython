name = input("Enter the contact's name: ")
phone = input("Enter the phone number: ")
email = input("Enter the email address: ")
address = input("Enter the address: ")
vcard_content = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""
filename = "contact.vcf"
with open(filename, "w") as file:
    file.write(vcard_content)
print(f"vCard for {name} has been created successfully! You can save it as '{filename}'.")
