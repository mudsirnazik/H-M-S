import tkinter as tk
from tkinter import messagebox
from database import setup
import auth, hospital

setup()

root = tk.Tk()
root.title("Advanced Hospital Management System")

def do_login():
    if auth.login(user_entry.get(), pass_entry.get()):
        messagebox.showinfo("Success", "Login Successful")
        main_screen()
    else:
        messagebox.showerror("Error", "Invalid Login")

def register_user():
    auth.register(user_entry.get(), pass_entry.get())
    messagebox.showinfo("Success", "User Registered")

def main_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Patient ID").grid(row=0,column=0)
    pid = tk.Entry(root); pid.grid(row=0,column=1)

    tk.Label(root, text="Name").grid(row=1,column=0)
    pname = tk.Entry(root); pname.grid(row=1,column=1)

    tk.Label(root, text="Age").grid(row=2,column=0)
    page = tk.Entry(root); page.grid(row=2,column=1)

    tk.Label(root, text="Disease").grid(row=3,column=0)
    dis = tk.Entry(root); dis.grid(row=3,column=1)

    def add_p():
        hospital.add_patient(pid.get(), pname.get(), page.get(), dis.get())
        messagebox.showinfo("Added","Patient Added")

    tk.Button(root,text="Add Patient",command=add_p).grid(row=4,column=0)

    def show_p():
        data = hospital.get_patients()
        text.delete(1.0, tk.END)
        for d in data:
            text.insert(tk.END, str(d)+"\n")

    tk.Button(root,text="Show Patients",command=show_p).grid(row=4,column=1)

    # Doctor
    tk.Label(root, text="Doctor ID").grid(row=5,column=0)
    did = tk.Entry(root); did.grid(row=5,column=1)

    tk.Label(root, text="Name").grid(row=6,column=0)
    dname = tk.Entry(root); dname.grid(row=6,column=1)

    tk.Label(root, text="Specialization").grid(row=7,column=0)
    spec = tk.Entry(root); spec.grid(row=7,column=1)

    def add_d():
        hospital.add_doctor(did.get(), dname.get(), spec.get())
        messagebox.showinfo("Added","Doctor Added")

    tk.Button(root,text="Add Doctor",command=add_d).grid(row=8,column=0)

    def show_d():
        data = hospital.get_doctors()
        text.delete(1.0, tk.END)
        for d in data:
            text.insert(tk.END, str(d)+"\n")

    tk.Button(root,text="Show Doctors",command=show_d).grid(row=8,column=1)

    global text
    text = tk.Text(root,height=10,width=40)
    text.grid(row=9,column=0,columnspan=2)

# Login UI
tk.Label(root, text="Username").grid(row=0,column=0)
user_entry = tk.Entry(root)
user_entry.grid(row=0,column=1)

tk.Label(root, text="Password").grid(row=1,column=0)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=1,column=1)

tk.Button(root, text="Login", command=do_login).grid(row=2,column=0)
tk.Button(root, text="Register", command=register_user).grid(row=2,column=1)

root.mainloop()
