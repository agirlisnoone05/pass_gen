from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json


def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_text.insert(0,password)

    pyperclip.copy(password)


def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {website:{
        "email": email,
        "password": password,
    }
    }

    if len(website) ==0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error",message = "Enter all details")
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                website_text.delete(0, END)
                password_text.delete(0, END)


def find_password():
    website = website_text.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="File does not exist.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"Data does not exist for {website}.")


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")


canvas = Canvas(width=200,height=200,bg="white",highlightthickness =0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)

website_text = Entry(width=21,highlightthickness =0)
website_text.grid(column=1,row=1)

email_text = Entry(width=35,highlightthickness =0)
email_text.grid(column=1,row=2,columnspan=2)
email_text.insert(0,"abc@email.com")

password_text = Entry(width=21,highlightthickness =0)
password_text.grid(column=1,row=3)

search_btn = Button(text="Search",highlightthickness =0,width=13,command= find_password )
search_btn.grid(column=2,row=1)

gen_pass_btn = Button(text="Generate Password",highlightthickness =0,command = generate_password)
gen_pass_btn.grid(column=2,row=3)

add_btn = Button(text="Add",highlightthickness =0 ,width=36,command=save)
add_btn.grid(column=1,row=4,columnspan=2)

window.mainloop()
