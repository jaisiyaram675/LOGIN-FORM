import  tkinter
from tkinter import messagebox
window =tkinter.Tk()
window.title("LOGIN FORM")
window.geometry("300x500")
window.configure(bg="#333333")
def login():
    username="GAURAV DHULL"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="LOGIN",message="LOGIN SUCCESSFULLY")
    else:
       messagebox.showerror(title="error",message="INCORRECT USERNAME OR PASSWORD")
frame=tkinter.Frame(bg="#333333") 
login_label = tkinter.Label( frame,text="LOGIN" ,font=("Arial" , 16), bg="#333333" , fg="#FFFFFF")
username_label=tkinter.Label(frame, text="USERNAME" ,font=("Arial" , 16), bg="#333333" , fg="#FFFFFF")

username_entry= tkinter.Entry(frame,font=("Arial" , 16))

password_label=tkinter.Label( frame,text="PASSWORD" , font=("Arial" , 16), bg="#333333" , fg="#FFFFFF")

password_entry= tkinter.Entry( frame,show="*" ,font=("Arial" , 16))
login_button=tkinter.Button( frame,text="Login" , bg="#FF3399" , fg="#FFFFFF" , font=("Arial" , 16) ,command=login  )




login_label.grid(row=0, column=0 , columnspan=2  ,sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1 , pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1    ,pady=20)
login_button.grid(row=3, column=1 ,columnspan=2 , pady=20)




frame.pack()



window.mainloop()
