import json  
import os  

class Contact:  
    def __init__(self, name, phone):  
        self.name = name  
        self.phone = phone  

    def __str__(self):  
        return f"{self.name}: {self.phone}"  

class ContactBook:  
    def __init__(self):  
        self.contacts = []  
        self.load_contacts()  # Load existing contacts when initialized  

    def load_contacts(self):  
        # Load contacts from a JSON file if it exists  
        if os.path.exists("contacts.json"):  
            with open("contacts.json", "r") as file:  
                self.contacts = [Contact(**contact) for contact in json.load(file)]  

    def save_contacts(self):  
        # Save contacts to a JSON file  
        with open("contacts.json", "w") as file:  
            json.dump([contact.__dict__ for contact in self.contacts], file)  

    def add_contact(self, name, phone):  
        # Add a new contact and save  
        contact = Contact(name, phone)  
        self.contacts.append(contact)  
        self.save_contacts()  
        print(f"Contact '{name}' added successfully.")  

    def view_contacts(self):  
        # Show existing contacts  
        if not self.contacts:  
            print("No contacts available.")  
            return  
        print("\nContact List:")  
        for contact in self.contacts:  
            print(contact)  

    def delete_contact(self, name):  
        # Delete a contact by name  
        for contact in self.contacts:  
            if contact.name == name:  
                self.contacts.remove(contact)  
                self.save_contacts()  # Save after deleting  
                print(f"Contact '{name}' deleted successfully.")  
                return  
        print(f"Contact '{name}' not found.")  

    def edit_contact(self, name, new_name, new_phone):  
        # Edit an existing contact  
        for contact in self.contacts:  
            if contact.name == name:  
                contact.name = new_name  
                contact.phone = new_phone  
                self.save_contacts()  # Save after editing  
                print(f"Contact '{name}' updated successfully.")  
                return  
        print(f"Contact '{name}' not found.")  

    def search_contact(self, query):  
        # Search for a contact by name or phone  
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]  
        if found_contacts:  
            print("\nSearch Results:")  
            for contact in found_contacts:  
                print(contact)  
        else:  
            print(f"No contacts found matching '{query}'.")  

def main():  
    contact_book = ContactBook()  

    while True:  
        print("\nContact Book Menu:")  
        print("1. Add Contact")  
        print("2. View Contacts")  
        print("3. Delete Contact")  
        print("4. Edit Contact")  
        print("5. Search Contact")  
        print("6. Exit")  
        choice = input("Choose an option: ")  

        if choice == '1':  
            name = input("Enter contact name: ").strip()  
            phone = input("Enter contact phone: ").strip()  
            contact_book.add_contact(name, phone)  
        elif choice == '2':  
            contact_book.view_contacts()  
        elif choice == '3':  
            name = input("Enter the name of the contact to delete: ").strip()  
            contact_book.delete_contact(name)  
        elif choice == '4':  
            name = input("Enter the name of the contact to edit: ").strip()  
            new_name = input("Enter new contact name: ").strip()  
            new_phone = input("Enter new contact phone: ").strip()  
            contact_book.edit_contact(name, new_name, new_phone)  
        elif choice == '5':  
            query = input("Enter name or phone to search for: ").strip()  
            contact_book.search_contact(query)  
        elif choice == '6':  
            print("Exiting the contact book. Goodbye!")  
            break  
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()