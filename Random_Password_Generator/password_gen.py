import tkinter as tk
import math
import time
root=tk.Tk()
root.title("Random Password Generator")

class Random:
    random=3251
    def RandomGenerate(self,limit):
        self.random = ((self.random*self.random)/100)%10000
        if (self.random % 100) == 0 :
            self.random = self.random + (self.random/100)
        return math.ceil(self.random%limit)
    def change(self,time):
        self.random=int((self.random+(time%10000))%10000)
    

root.resizable(False,False)
enter_length=tk.Label(root, text="Enter length(12-32): ")
enter_length.grid(row=0,column=0)

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=1, padx=5, pady=5)

p = Random()
t=int(time.time())
p.change(t)
passw = ""
def generate():
    button_generate_pass.configure(state=tk.DISABLED)
    length=int(e.get())
    e.configure(state=tk.DISABLED)
    
    if length >= 12 and length <= 32:
        temp=choice=0
        temp=p.RandomGenerate(25)
        alphabet="mnbvcxzlkjhgfdsapoiuytrewq"
        Alpha = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        special_char = "!@#$%&*"
        numbers = "1234567890"
        password=""
        password=alphabet[temp] #Starting with Lower Case
        size=1

        while size < (length-5) :
            choice=p.RandomGenerate(4)

            if choice == 0 : #For lower case
                temp=p.RandomGenerate(25)
                if temp == 12:
                    t1=int(time.time())
                    p.change(t1)
                password=password+alphabet[temp]
                size=size+1
            elif choice == 1 : #For upper case
                temp=p.RandomGenerate(25)
                if temp == 11:
                    t1=int(time.time())
                    p.change(t1)
                password=password+Alpha[temp]
                size=size+1
            elif choice == 2 : #For Numbers
                temp=p.RandomGenerate(9)
                password=password+numbers[temp]
                size=size+1
            else : #For Special Chars
                temp=p.RandomGenerate(6)
                password=password+special_char[temp]
                size=size+1
        
        #For fulfilling criteria
        temp=p.RandomGenerate(25)
        password=password+alphabet[temp]

        temp=p.RandomGenerate(25)
        password=password+Alpha[temp]

        temp=p.RandomGenerate(9)
        password=password+numbers[temp]

        temp=p.RandomGenerate(6)
        password=password+special_char[temp]

        temp=p.RandomGenerate(25)
        password=password+Alpha[temp] #Ending with upper case

        ans.configure(text=password)
        global passw
        passw=password
        e.configure(state=tk.NORMAL)
        button_generate_pass.configure(state=tk.NORMAL)
    else :
        e.configure(state=tk.NORMAL)
        enter_length.configure(text="Re-enter correct length")
        button_generate_pass.configure(state=tk.NORMAL)
        return
    

button_generate_pass = tk.Button(root, text="Generate password", command=generate)
button_generate_pass.grid(row=1,column=0, padx=5, pady=5)

def copy():
    button_copy_pass.configure(state=tk.DISABLED)
    root.clipboard_clear()
    root.clipboard_append(passw)
    ans.configure(text="Copied to Clipboard")
    button_copy_pass.configure(state=tk.NORMAL)

button_copy_pass = tk.Button(root, text="Copy password", command=copy)
button_copy_pass.grid(row=1,column=1, padx=5, pady=5)

pass_generated=tk.Label(root, text="Generated Password")
pass_generated.grid(row=2,column=0)

ans = tk.Label(root, width=35, borderwidth=5, state=tk.DISABLED)
ans.grid(row=2, column=1, padx=5, pady=5)



root.mainloop()
