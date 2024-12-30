# Write a program to create a dictionary where the keys are names and the values are phone numbers.
# Allow the user to add, delete, update, and search for contacts.

# contactdata={}

# def displaymenue():
#     print("welcome to contact Book Management")
    
    
# def addcont():
#     name= input("enter the contact u want to add:")
#     if name in contactdata:
#         print("name already present enter another name :")
#         return
    
#     phoneno = int(input("enter the phonenum"))
#     contactdata[name]=phoneno
    
    
    
# def deletecont():
#     name = input("enter the name to be deleted: ")
#     if name in contactdata:
#         del deletecont[name]
        
# # def updatecont():
# #     name =  input("enter the contact to be updated: ")    
# #     if name in contactdata:
        
 #******************************************************************************************************   
# def display_menu():
#     print("\nContact Manager")
#     print("1. Add Contact")
#     print("2. Delete Contact")
#     print("3. Update Contact")
#     print("4. Search Contact")
#     print("5. View All Contacts")
#     print("6. Exit")

# def add_contact(contacts):
#     name = input("Enter name: ").strip()
#     if name in contacts:
#         print("Contact already exists.")
#     else:
#         phone = input("Enter phone number: ").strip()
#         contacts[name] = phone
#         # print(f"Contact {name} added.")

# def delete_contact(contacts):
#     name = input("Enter name to delete: ").strip()
#     if name in contacts:
#         del contacts[name]
#         # print(f"Contact {name} deleted.")
#     else:
#         print("Contact not found.")

# def update_contact(contacts):
#     name = input("Enter name to update: ").strip()
#     if name in contacts:
#         phone = input("Enter new phone number: ").strip()
#         contacts[name] = phone
#         # print(f"Contact {name} updated.")
#     else:
#         print("Contact not found.")

# def search_contact(contacts):
#     name = input("Enter name to search: ").strip()
#     if name in contacts:
#         print(f"{name}: {contacts[name]}")
#     else:
#         print("Contact not found.")

# def view_all_contacts(contacts):
#     if contacts:
#         print("\nAll Contacts:")
#         for name, phone in contacts.items():
#             print(f"{name}: {phone}")
#     else:
#         print("No contacts available.")

# def main():
#     contacts = {}
#     while True:
#         display_menu()
#         choice = input("Choose an option: ").strip()
        
#         if choice == '1':
#             add_contact(contacts)
#         elif choice == '2':
#             delete_contact(contacts)
#         elif choice == '3':
#             update_contact(contacts)
#         elif choice == '4':
#             search_contact(contacts)
#         elif choice == '5':
#             view_all_contacts(contacts)
#         elif choice == '6':
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

    






























# #******************************************************************************************************

# #******************************************************************************************************


# # contactdata={}
# # noofcon= int(input("enter the number of contact to be added"))

# # i = 1
# # while i<=noofcon:
# #     name = input("enter the name")
# #     if name in contactdata:
# #         print("name already present ,enter another name ")
# #         continue
    
# #     pno = int(input("enter the pno"))
# #     contactdata ={
# #     "name":name,
# #     "phonenumber":pno
# #     }
# # i+=1
# # print(contact)




def display_menu():
    print("\nWelcome to contact book")
    print("display menue")
    print("1. Add contact ")
    print("2. delete contact ")
    print("3. update contact ")
    print("4. view contact ")
    print("5. search contact ")
    print("6. exit")
    

def add_contact(contacts):
    name = input("enter the name to add").strip()
    if name in contacts:
        print("name already present... enter aother name")
    else:
        phone = input("enter the phoneumber").strip()
        contacts[name] = phone
        print(f"{name} added to the list")

def delete_contact(contacts):
    name = input("enter name to be deleted: ").strip()
    if name in contacts:
        del contacts[name]
        print("deleted")
    else:
        print("contact not found")

def update_contact(contacts):
    name = input("enter the name to be updated").strip()
    if name in contacts:
        phone=input("enter the new phnonenumber").strip()
        contacts[name] = phone
    else:
        print("contact not found")


def search_contact(contacts):
    name = input("enter name to display the details ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("contact not found")
        
def view_all_contacts(contacts):
    if contacts:
        print("displaying all the contacts")
        for k,v in contacts.items():
            print(f"{k}:{v}")
    else:
        print("no contact present")
    


def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("enter your choice ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            view_all_contacts(contacts)
        elif choice == '5':
            search_contact(contacts)

        elif choice == '6':
            print("exitted")
            break 
        else:
            print("invalid choice ")
            
if __name__ == "__main__":
    main()
        









