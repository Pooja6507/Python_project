from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('database')
root.geometry("400x400")

# Databases
conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("""CREATE TABLE names (
          name text,
          email text,
          contact text,

           """)

# Create function to modify
def modify():
    modify = Tk()
    modify.title('Modify A Record')
    modify.geometry("400x600")
    
    # Create a database or connect to one
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FR0M customers WHERE oid =" + record_id)
    records = c.fetchall()


    # Create text boxes
    name_modify = Entry(modify, width=40)
    name_modify.grid(row=0, column=0, padx=20)
    email_modify = Entry(modify, width=40)
    email_modify.grid(row=1, column=1, padx=20)
    contact_modify= Entry(modify, width=40)
    contact_modify.grid(row=2, column=1, padx=20)
    
    # Create text box labels
    name_label = Label(modify, text="Name")
    name_label.grid(row=0, column=0)
    email_label = Label(modify, text="Email")
    email_label.grid(row=1, column=0)
    contact_label = Label(modify, text="Contact")
    contact_label.grid(row=2, column=0)

    # loop
    for record in records:
        name_modify.insert(0, record[0])
        email_modify.insert(0, record[1])
        contact_modify.insert(0, record[2])


    # Create a Save button
    save_btn = Button(modify, text="Save Record", command=save)
    save_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=140)
    
    
    #Create function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from customers WHERE oid= " + delete_box.get())

    delete_box.delete(0,END)

    conn.commit()

    conn.close()
    
    
    # Create Submit Function
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO customer VALUES (:name, :email, :contact")
             {
               'name' : name.get(),
               'email' : email.get(),
               'contact' : contact.get()
             })

    conn.commit()

    conn.close()
    
    
    
    # Clear The Text Boxes
    name.delete(0, END)
    email.delete(0, END)
    contact.delete(0, END)


#Create Query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FR0M customers")
    records = c.fetchall()
    print(records)
    
       print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=5, column=0, columnspan=2)

    conn.commit()

    conn.close()


#Create text boxes
name = Entry(root, width=40)
name.grid(row=0, column=0, padx=20)
email = Entry(root, width=40)
email.grid(row=1, column=1, padx=20)
contact = Entry(root, width=40)
contact.grid(row=2, column=1, padx=20)
delete_box = Entry(root, width=40)
delete_box.grid(row=7, column=1)

#Create text box labels
name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=1, column=0)
contact_label = Label(root, text="Contact")
contact_label.grid(row=2, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=7, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create A Query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

#Create an Modify  button
modify_btn = Button(root, text="Modify Record", command=modify)
modify_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=140)


conn.commit()

conn.close()

root.mainloop()


    
    
    
    
    
    
    
    
    
