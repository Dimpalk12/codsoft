contacts = []


# Add contact
def addContact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added!\n")

# View contacts
def viewContacts():
    if len(contacts) == 0:
        print("No contacts saved.\n")
        return
    for contact in contacts:
        print("------")
        print("Name:", contact["Name"])
        print("Phone:", contact["Phone"])
        print("Email:", contact["Email"])
        print("Address:", contact["Address"])
    print("------\n")

# Search contact
def searchContact():
    search = input("Enter name or phone to search: ")
    for contact in contacts:
        if search.lower() in contact["Name"].lower() or search in contact["Phone"]:
            print("Found:")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            return
    print("Contact not found.\n")

# Update contact
def updateContact():
    name = input("Enter name to update: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            phone = input("New phone (leave blank to keep old): ")
            email = input("New email (leave blank to keep old): ")
            address = input("New address (leave blank to keep old): ")

            if phone: contact["Phone"] = phone
            if email: contact["Email"] = email
            if address: contact["Address"] = address

            print(" Contact updated!\n")
            return
    print(" Contact not found.\n")

# Delete contact
def deleteContact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted!\n")
            return
    print(" Contact not found.\n")
# Menu
while True:
    print(" Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        addContact()
    elif choice == "2":
        viewContacts()
    elif choice == "3":
        searchContact()
    elif choice == "4":
        updateContact()
    elif choice == "5":
        deleteContact()
    elif choice == "6":
        print(" Thank you for using dimpal's Contact Book ")
        break
    else:
        print("Invalid choice. Try again.\n")