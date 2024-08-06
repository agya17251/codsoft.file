import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact book to store contact details
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Name", "Enter contact name:")
    if name:
        if name in contacts:
            messagebox.showwarning("Warning", "Contact already exists!")
        else:
            phone = simpledialog.askstring("Phone", "Enter contact phone number:")
            email = simpledialog.askstring("Email", "Enter contact email:")
            address = simpledialog.askstring("Address", "Enter contact address:")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact added successfully!")
            display_contacts()

# Function to display all contacts
def display_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Function to search for a contact
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter contact name or phone number:")
    if search_term:
        for name, details in contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                return
        messagebox.showwarning("Not Found", "Contact not found!")

# Function to update a contact
def update_contact():
    name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    if name and name in contacts:
        phone = simpledialog.askstring("Phone", "Enter new phone number:")
        email = simpledialog.askstring("Email", "Enter new email:")
        address = simpledialog.askstring("Address", "Enter new address:")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact updated successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Contact not found!")

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    if name and name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Contact not found!")

# Main window setup
root = tk.Tk()
root.title("Contact Book App")

# Buttons for actions
tk.Button(root, text="Add Contact", command=add_contact, width=20).pack(pady=5)
tk.Button(root, text="View Contacts", command=display_contacts, width=20).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact, width=20).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, width=20).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, width=20).pack(pady=5)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(pady=10)

# Start the main loop
root.mainloop()
