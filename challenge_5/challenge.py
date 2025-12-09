# Home Work from GPT
# challenge_5
# Contact Book Application

print("Welcome to the Contact Book Application!")
contacts = {}

print ("Contect Menu")
print("1. Add Contacts")
print("2. View Contacts")
print("3. Search Contacts")
print("4. Delete Contacts")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == '1':
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added successfully.")
elif choice == '2':
    if contacts:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")
elif choice == '3':
    search_name = input("Enter the name to search: ")
    if search_name in contacts:
        print(f"Found Contact - Name: {search_name}, Phone: {contacts[search_name]}")
    else:
        print("Contact not found.")
elif choice == '4':
    delete_name = input("Enter the name to delete: ")
    if delete_name in contacts:
        del contacts[delete_name]
        print(f"Contact {delete_name} deleted successfully.")
    else:
        print("Contact not found.")
elif choice == '5':
    print("Thank you! for using the application. Goodbye!")

