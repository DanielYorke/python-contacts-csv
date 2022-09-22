#from nis import match
#from unittest import case
from models.contact import Contact
import csv


def addNewContact() -> Contact:
    name = input("Enter new contact's name: ")
    phone = input("Enter new contact's phone number: ")
    email = input("Enter new contact's email address: ")
    return Contact(name, phone, email)

contacts = []



while True:
    menu = int(input("Menu \n 1. Add new contact\n 2.Display Contacts\n 3.Search for Contact\n 0.Exit\n"))
    match menu:
        case 0:
            break
        case 1:
            print("Adding new contact")
            #put code to add new contact
            #newContact = addNewContact()
            contacts.append(addNewContact())
        case 2:
            print("\n\n -----Contacts-----")
            for c in contacts:
                #print(str(c))
                print(c)
            #print(contacts)
        case 3:
            key = input("Enter the name of the contact you are searching for: ")
            for c in contacts:
                if c.name == key:
                    print(c.__str__())
        case _:
            print("Invalid option. Please select another option from the Menu")


print("End of application")