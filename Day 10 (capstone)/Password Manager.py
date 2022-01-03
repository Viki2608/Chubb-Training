from tkinter import *
from tkinter import messagebox
import re
import psycopg2
from random import choice, randint, shuffle
import pyperclip


def email_check(mail):
    if(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mail)):
        return True
 
    else:
       return False

def password_check(ps):
    if (re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', ps)):
        return True
    else:
        return False

con=psycopg2.connect(
            host = "localhost",
            database = "guvi",
            user = "postgres",
            password="admin"
        )

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(email) == 0 :
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty or check the password strength.")
    elif password_check(password)==False:
        messagebox.showinfo(title="Oops", message="Check the password strength Minimum length should be 8 charachters including special characters.")
    elif email_check(email)== False:
        messagebox.showinfo(title="Oops", message="Please Provide a valid Email id.")

    else:
        is_ok = messagebox.askokcancel(
        title=website, 
        message=f"These are the details entered: \nEmail: {email} "
        f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            cur=con.cursor()
            sql_1=f"INSERT INTO password_manager (website_name,email,password)VALUES(%s,%s,%s)"
            
            cur.execute(sql_1,(website,email,password)) 
            print(f"data inserted successfully! into password_manager")
            con.commit()
            
        
            

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    
def display():
    newwin=Toplevel()
    newwin.geometry('600x600')
    newwin.title("Passwords")
    
    L2 = Label(newwin, text="WEBSITE NAME")
    L2.grid(row=0, column=2)
    L3=Label(newwin,text="EMAIL")
    L3.grid(row=0,column=4)
    L4=Label(newwin,text="PASSWORD")
    L4.grid(row=0,column=6)
    i=1
    cur=con.cursor() 
    website_query="select website_name from password_manager;"
    email_query="select email from password_manager;"
    password_query="select password from password_manager;"
    cur.execute(email_query)
    email=cur.fetchall()
    cur.execute(password_query)
    passw=cur.fetchall()
    cur.execute(website_query)
    wb=cur.fetchall()
    
    i=0
    y=1
    for x in wb:
        L2 = Label(newwin, text=wb[i])
        L2.grid(row=y, column=2)
        L3 = Label(newwin, text=email[i])
        L3.grid(row=y, column=4)
        L4 = Label(newwin, text=passw[i])
        L4.grid(row=y, column=6)
        i+=1
        y+=1


#-------------------------------UI------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=100, width=100)
logo_img = PhotoImage(file="Pass.png")
canvas.create_image(50, 50, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Vignesh26.manoharan@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

show= Button(text='Show Passwords',width=36,command=display)
show.grid(row=5,column=1,columnspan=2)

window.mainloop()