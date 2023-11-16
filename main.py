from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #




    
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open('password.txt', 'a') as filename:
        filename.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0,  END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width= 200)
image_png = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=image_png)
canvas.grid(column=1, row=0)


website_label = Label(text="Website: ")
website_label.grid(column= 0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)



website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan= 2)

email_entry = Entry(width= 38)
email_entry.grid(column =1,  row=2, columnspan= 2)
email_entry.insert(0, 'xyz@gmail.com')

password_entry = Entry(width= 21)
password_entry.grid(column=1, row=3)


generate_password = Button(text="Genrate Password")
generate_password.grid(column = 2, row=3)

add = Button(text="ADD", width=36, command= save_password)
add.grid(column =1, columnspan=2, row=4)


window.mainloop()

