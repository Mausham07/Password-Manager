from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|']

def generate_password():
    rn_letters = random.randint(6,8)
    rn_numbers = random.randint(2,4)
    rn_symbols = random.randint(2,4)

    pasword_letters=[random.choice(all_letters) for char in range(rn_letters)]
    pasword_numbers=([random.choice(numbers) for char in range(rn_numbers)])
    pasword_symbols=[random.choice(special_characters) for char in range(rn_symbols)]

    password_list = pasword_letters + pasword_numbers + pasword_symbols
    random.shuffle(password_list)

    new_password = "".join(password_list)
    password_entry.insert(0, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

   
    if len(website) == 0 or len(password) == 0:
        is_full = messagebox.showinfo(title="Opps", message="Please do not leave any fields empty.")

    else:
        is_ok= messagebox.askokcancel(title="Sure?", message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            
            try:
                with open('data_json', 'r') as filename:
                    data = json.load(filename)

            except:
                with open('data_json', 'w') as filename:
                    json.dump(new_data, filename, indent=4)

            else:
                data.update(new_data)

                with open('data_json', "w") as data_file:

                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0,  END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open('data_json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

            else:
                messagebox.showerror(title="Error", message=f"No details currently exists for {website}.")

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



website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)

email_entry = Entry(width= 38)
email_entry.grid(column =1,  row=2, columnspan= 2)
email_entry.insert(0, 'xyz@gmail.com')

password_entry = Entry(width= 21)
password_entry.grid(column=1, row=3)



generate_password = Button(text="Genrate Password", command=generate_password)
generate_password.grid(column = 2, row=3)

add = Button(text="ADD", width=36, command= save_password)
add.grid(column =1, columnspan=2, row=4)

search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=1)


window.mainloop()

