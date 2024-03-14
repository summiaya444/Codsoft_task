from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime
from tkinter import messagebox,simpledialog
import mysql.connector

class Contact_bk:
    def __init__(self,root):
        self.root=root
        self.root.title("Contact Book")
        self.root.geometry("1040x650+0+0")
        my_title=Label(self.root,bd=20,relief=RIDGE,text="CONTACT BOOK",bg="light grey",fg="black",font=("courier new",45,"bold"))
        my_title.pack(side=TOP,fill=X)

        self.add_window=None
        self.update_window=None
        self.first_frame=Frame(self.root,bd=20,relief=RIDGE,bg="light grey")
        self.first_frame.place(x=0,y=100,width=1040,height=550)
        self.sec_frame=LabelFrame(self.first_frame,bd=10,padx=20,relief=RIDGE,font=("courier new",20,"bold"),text="CONTACT DETAILS",bg="light grey")
        self.sec_frame.place(x=0,y=5,width=1000,height=400)
        self.third_frame = LabelFrame(self.first_frame, bd=10, padx=20, relief=RIDGE, font=("courier new", 20, "bold"),
                                    text="EDIT DETAILS", bg="light grey")
        self.third_frame.place(x=0, y=405, width=1000, height=100)

        self.search_button = Button(self.third_frame, text="SEARCH", relief=RIDGE, font=("courier new", 18, "bold"),
                                 bg="white", command=self.search)
        self.search_button.place(x=60, y=4)

        self.add_button = Button(self.third_frame,text="ADD",relief=RIDGE, font=("courier new", 18,"bold"),bg="white", command=self.add_contact)
        self.add_button.place(x=220, y=4)

        self.update_button = Button(self.third_frame, text="UPDATE",relief=RIDGE, font=("courier new", 18,"bold"), bg="white", command=self.update_contact)
        self.update_button.place(x=340, y=4)

        self.delete_button = Button(self.third_frame, text="DELETE",relief=RIDGE, font=("courier new", 18,"bold"),bg="white", command=self.delete_contact)
        self.delete_button.place(x=500, y=4)

        self.reset_button = Button(self.third_frame, text="RESET", relief=RIDGE, font=("courier new", 18, "bold"),
                                    bg="white", command=self.reset_bk)
        self.reset_button.place(x=660, y=4)

        self.exit_button = Button(self.third_frame, text="EXIT", relief=RIDGE, font=("courier new", 18, "bold"),
                                    bg="white", command=self.exit)
        self.exit_button.place(x=800, y=4)

        self.contact_treeview = ttk.Treeview(self.sec_frame, columns=("S_No", "Name", "Contact_No", "Email_Id","Address"), show="headings",
                                             height=450)
        self.contact_treeview.heading("S_No", text="S_No")
        self.contact_treeview.heading("Name", text="Name")
        self.contact_treeview.heading("Contact_No", text="Contact #")
        self.contact_treeview.heading("Email_Id", text="Email Address")
        self.contact_treeview.heading("Address", text="Address")

        self.contact_treeview.pack(side=tk.LEFT, fill=tk.BOTH)
        self.contact_treeview.column("S_No",width=80)
        self.contact_treeview.column("Contact_No", width=180)
        self.contact_treeview.column("Address", width=240)

        scrollbar = tk.Scrollbar(self.sec_frame, orient=tk.VERTICAL, command=self.contact_treeview.yview,bg="white")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_treeview.config(yscrollcommand=scrollbar.set)

        self.update_contact_treeview()

    def get_contact_by_name(self,old_name):
                self.connection, self.cursor = self.make_connection()
                try:
                    comm="select * from contacts where name=%s"
                    self.cursor.execute(comm,(old_name,))
                    done_2=self.cursor.fetchone()
                    return done_2
                except:
                    messagebox.showerror("Error","Contact Not Found!")
                finally:
                    self.finish_connections()

    def search(self):
        self.search_2 = simpledialog.askstring("SEARCH CONTACT", "Enter Full Name: ")
        if self.search_2:
            true_2 = self.get_contact_by_name(self.search_2)
            if true_2:
                self.connection, self.cursor = self.make_connection()
                try:
                    comm = "select * from contacts where name=%s"
                    self.cursor.execute(comm, (self.search_2,))
                    self.contact_treeview.tag_configure("highlight", background="light grey")
                    rows = self.cursor.fetchall()
                    for item in self.contact_treeview.get_children():
                        values=self.contact_treeview.item(item,'values')
                        if values[1]==true_2[1]:
                            self.contact_treeview.item(item,tags=("highlight",))
                except Exception as a:
                    print(f"{a}")
                    messagebox.showerror("Incorrect","Enter Full Name Again:")
                finally:
                    self.finish_connections()
        #else:
            #messagebox.showerror("Incorrect", "Enter Full Name Again:

    def reset_bk(self):
        self.connection, self.cursor = self.make_connection()
        confirm=messagebox.askyesno("CONFIRM","Confirm Reset?")
        if confirm is True:
            comm = "delete from contacts "
            self.cursor.execute(comm)
            self.connection.commit()
            self.retrieve_contacts()
            messagebox.showinfo("INFO","Refresh Contact book!")
        self.finish_connections()

    def exit(self):
        messagebox.askyesno("Confirm","Are you sure you want to exit?")
        if True:
            root.destroy()

    def update_contact_treeview(self):
        existing_contacts = [self.contact_treeview.item(item, 'values')
                             for item in self.contact_treeview.get_children()]

        contacts_get = self.retrieve_contacts()
        new_contacts=existing_contacts+contacts_get
        self.contact_treeview.delete(*self.contact_treeview.get_children())
        for contact in new_contacts:
            self.contact_treeview.insert("", "end", values=(contact[0], contact[1], contact[2], contact[3]),tags=("courier new,"))

    def make_connection(self):
                try:
                    self.connection = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="physicsbook12",
                        database="contact_bk")
                    self.cursor = self.connection.cursor()
                    return self.connection, self.cursor
                    # yhn return karana tha connection aur cursor
                except Exception as e:
                    print(f"Error establishing connection: {e}")
                    messagebox.showerror("Error","Error establishing connection!")  # yhn warning ka syntax dekhna hai

    def finish_connections(self):
                try:
                    self.cursor.close()
                    self.connection.close()
                except Exception as e:
                    print(f"Error establishing connection: {e}")
                    messagebox.showerror("Error","Error closing connection!")

    def enter_details(self,S_No,Name,Contact_No,Email_Id,Add):
                self.connection, self.cursor=self.make_connection()
                try:
                    comm="insert into Contacts(S_No,Name,Contact_No,Email_Id,Address) values(%s,%s,%s,%s,%s)"
                    values=(S_No,Name,Contact_No,Email_Id,Add)
                    self.cursor.execute(comm,values)
                    self.connection.commit()
                except Exception as e:
                    print(f"{e}")
                    messagebox.showwarning("Error","Error entering details!")
                finally:
                    self.finish_connections()

    def update_details(self,S_No,Name,Contact_No,Email_Id,Address,check_1):
                self.connection, self.cursor = self.make_connection()
                try:
                    comm="update contacts set S_No=%s, Name=%s, Contact_No=%s, Email_Id=%s, Address=%s where Name=%s"
                    values = (S_No,Name,Contact_No, Email_Id,Address,check_1)
                    self.cursor.execute(comm, values)
                    self.connection.commit()
                except Exception as error:
                    print(f"{error}")
                    messagebox.showerror("Error","Error in Updating Details!!")
                finally:
                    self.finish_connections()

    def retrieve_contacts(self):
                self.connection, self.cursor = self.make_connection()
                contacts=[]
                try:
                    comm= "select * from contacts"
                    self.cursor.execute(comm)
                    contacts=self.cursor.fetchall()
                    for contact in contacts:
                        self.contact_treeview.insert("", "end",values=contact,tags=("CourierNew,"))
                    return contacts
                except Exception as e:
                    print(f"{e}")
                    messagebox.showerror("Error","Error in displaying contacts!")
                finally:
                    self.finish_connections()
                    return contacts

    def delete_single_contact(self,search_by_name):
        self.connection,self.cursor=self.make_connection()
        try:
            comm="delete from contacts where name=%s"
            self.cursor.execute(comm,(search_by_name,))
            self.connection.commit()
            display = self.retrieve_contacts()
            self.contact_treeview.delete(*self.contact_treeview.get_children())
            for contact in display:
                self.contact_treeview.insert("", "end", values=contact,tags=("CourierNew",))
            messagebox.showinfo("Deleted","Contact Deleted!")
        except Exception as error:
            print(f"{error}")
            messagebox.showerror("Error","Error in Deleting Contact!")
        finally:
            self.finish_connections()

    def save_contact(self):
        s_no=self.S_No_entry.get()
        name =self.name_entry.get()
        phone =self.phone_entry.get()
        email =self.email_entry.get()
        add=self.add_entry.get()

        if name and email and phone:
            self.enter_details(s_no,name, phone, email,add)
            display=self.retrieve_contacts()
            self.contact_treeview.delete(*self.contact_treeview.get_children())
            for contact in display:
                self.contact_treeview.insert("","end",values=contact)
            if self.add_window:
                self.add_window.destroy()
        else:
            messagebox.showerror("ERROR","Incomplete Information!")

    def add_contact(self):

            self.add_window=Tk()
            self.add_window.title("ADD CONTACT")
            self.add_window.geometry("500x300")

            Label(self.add_window, text="S#: ", font=("courier new", 12)).grid(row=0, column=0, padx=20, pady=10)
            self.S_No_entry = Entry(self.add_window, font=("courier new", 12))
            self.S_No_entry.grid(row=0, column=1, padx=10, pady=5)

            Label(self.add_window, text="NAME: ", font=("courier new", 12)).grid(row=1, column=0, padx=20, pady=10)
            self.name_entry = Entry(self.add_window, font=("courier new", 12))
            self.name_entry.grid(row=1, column=1, padx=10, pady=5)

            Label(self.add_window, text="PHONE: ", font=("courier new", 12)).grid(row=2, column=0, padx=20, pady=10)
            self.phone_entry = Entry(self.add_window, font=("courier new", 12))
            self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

            Label(self.add_window, text="EMAIL: ", font=("courier new", 12)).grid(row=3, column=0, padx=20, pady=10)
            self.email_entry = Entry(self.add_window, font=("courier new", 12))
            self.email_entry.grid(row=3, column=1, padx=10, pady=5)

            Label(self.add_window, text="ADDRESS ", font=("courier new", 12)).grid(row=4, column=0, padx=20, pady=10)
            self.add_entry = Entry(self.add_window, font=("courier new", 12))
            self.add_entry.grid(row=4, column=1, padx=10, pady=5)

            save_button = Button(self.add_window, text="SAVE", font=("courier new", 12), command=self.save_contact)
            save_button.grid(row=5, column=0, columnspan=2, pady=10)

    def save_contact_2(self,check_1):
        up_s_no=self.sno_entry.get()
        up_name = self.n_entry.get()
        up_phone = self.p_entry.get()
        up_email = self.e_entry.get()
        up_add = self.a_entry.get()

        if up_s_no and up_name and up_email and up_phone and up_add:
            self.update_details(up_s_no,up_name,up_phone,up_email,up_add,check_1)
            display = self.retrieve_contacts()
            self.contact_treeview.delete(*self.contact_treeview.get_children())
            for contact in display:
                self.contact_treeview.insert("", "end", values=contact)
            if self.update_window:
                self.update_window.destroy()
        else:
            messagebox.showerror("Error", "INCOMPLETE INFORMATION!\nPROVIDE ALL DETAILS!")

    def update_contact(self):
                self.check_1=simpledialog.askstring("UPDATE CONTACT","Enter Full Name: ")
                if self.check_1:
                    true_1=self.get_contact_by_name(self.check_1)
                    if true_1:
                        self.update_window=Tk()
                        self.update_window.title("UPDATE CONTACT")
                        self.update_window.geometry("500x300")

                        Label(self.update_window, text="S_No: ", font=("courier new", 12)).grid(row=0, column=0, padx=10, pady=5)
                        self.sno_entry = Entry(self.update_window, font=("courier new", 12))
                        self.sno_entry.grid(row=0, column=1, padx=10, pady=5)

                        Label(self.update_window, text="NAME: ", font=("courier new", 12)).grid(row=1, column=0, padx=10, pady=5)
                        self.n_entry = Entry(self.update_window, font=("courier new", 12))
                        self.n_entry.grid(row=1, column=1, padx=10, pady=5)

                        Label(self.update_window, text="PHONE: ", font=("courier new", 12)).grid(row=2, column=0, padx=10, pady=5)
                        self.p_entry = Entry(self.update_window, font=("courier new", 12))
                        self.p_entry.grid(row=2, column=1, padx=10, pady=5)

                        Label(self.update_window, text="EMAIL: ", font=("courier new", 12)).grid(row=3, column=0, padx=10, pady=5)
                        self.e_entry = Entry(self.update_window, font=("courier new", 12))
                        self.e_entry.grid(row=3, column=1, padx=10, pady=5)

                        Label(self.update_window, text="ADDRESS: ", font=("courier new", 12)).grid(row=4, column=0,padx=10, pady=5)
                        self.a_entry = Entry(self.update_window, font=("courier new", 12))
                        self.a_entry.grid(row=4, column=1, padx=10, pady=5)

                        self.sno_entry.insert(0, true_1[0])
                        self.n_entry.insert(0, true_1[1])
                        self.p_entry.insert(0, true_1[2])
                        self.e_entry.insert(0, true_1[3])
                        self.a_entry.insert(0, true_1[4])

                        save_button = Button(self.update_window, text="SAVE", font=("courier new", 12), command=lambda :self.save_contact_2(self.check_1))
                        save_button.grid(row=5, column=0, columnspan=2, pady=10)

                    else:
                        messagebox.showerror("Error",f"Contact Not Found No contact found with the name '{full_name}'.")
                else:
                    messagebox.showerror("Error","No Name Entered! \nPlease enter a full name for updating.")

    def delete_contact(self):
                self.check_2 = simpledialog.askstring("DELETE CONTACT", "Enter Full Name: ")
                if self.check_2:
                    true_2 = self.get_contact_by_name(self.check_2)
                    if true_2:
                        confirm = messagebox.askokcancel("Confirm","Do you want to delete the contact?")
                        if confirm:
                            self.delete_single_contact(self.check_2)
root=Tk()
start=Contact_bk(root)
root.mainloop()
