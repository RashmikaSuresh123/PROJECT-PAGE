import tkinter as tk
from tkinter import *
from tkinter import messagebox



def books():
    class ShoppingCartApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Shopping Cart")
            
            self.cart = []
            
            self.item_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
            self.item_listbox.pack(padx=10, pady=10)
            
            items = [["Devil and miss prym"],
                    ["Harry potter"],
                    ["Malgudi days"],
                    ["Tuesdays with morrie"],
                    ["Chicken soup for fathers soul"],
                    ["5 People you meet in heaven"],
                    ["Romio Juliet"],
                    ["I am another you"],
                    ["The art of racing in the rain"],
                    ["Little women"]]
            for item in items:
                self.item_listbox.insert(tk.END, item)

            self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
            self.add_button.pack(padx=10, pady=5)
            
            self.cart_label = tk.Label(root, text="Cart:")
            self.cart_label.pack(padx=10, pady=5)
            
            self.cart_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
            self.cart_listbox.pack(padx=10, pady=10)

            self.delete_button=tk.Button(root,text="Delete item",command=self.delete_item)
            self.delete_button.pack(padx=10, pady=5)

            self.delete1_button=tk.Button(root,text="Delete whole cart",command=self.delete1_item)
            self.delete1_button.pack(padx=10, pady=5)

            

            self.checkout_button = tk.Button(root, text="Proceed to Billing", command=self.checkout)
            self.checkout_button.pack(padx=10, pady=5)
        def delete_item(self):
            self.cart_listbox.delete(tk.ANCHOR)
            
        def delete1_item(self):
            self.cart_listbox.delete(0,END)
            
        def add_to_cart(self):
            selected_item = self.item_listbox.get(tk.ACTIVE)
            if selected_item:
                self.cart.append(selected_item)
                self.update_cart_listbox()
        
        def update_cart_listbox(self):
            self.cart_listbox.delete(0, tk.END)
            for item in self.cart:
                self.cart_listbox.insert(tk.END, item)
        
        def checkout(self):
            if not self.cart:
                messagebox.showinfo("Checkout", "Your cart is empty.")
            else:
                selected_item = self.cart_listbox.get(tk.ACTIVE)
                if selected_item:
                    messagebox.showinfo("Checkout", f"Proceeding to billing for {selected_item}")
                    messagebox.showinfo(title="END",message="Thank you for shopping")
                else:
                    messagebox.showinfo("Checkout", "Please select an item from the cart.")

    if __name__ == "__main__":
        root = tk.Tk()
        app = ShoppingCartApp(root)
        root.mainloop()


def login_user():
    username_info=username.get()
    password_info=password.get()
    username_info1=username1.get()
    password_info1=password1.get()

    file=open(username_info+".txt","w")
    file.write(username_info)
    file.write(password_info)
    file.close()
    if (username_info1==username_info and password_info1==password_info):
        messagebox.showinfo(title="Sucess",message="Login Sucess" )

    else:        
        messagebox.showinfo(title="Failure",message="Login Again" )
        login()
        
        
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    
    books()
def login():
    global root1
    global username
    global password
    global username_entry
    global password_entry
    root1=Toplevel(root)
    username=StringVar()
    password=StringVar()
    root1.configure(bg="turquoise")
    root1.geometry('340x250')
    Label(root1,text="**Enter the registered username and password**",bg='turquoise').pack()
    Label(root1,text='Username *',bg='turquoise').pack()
    username_entry=Entry(root1,textvariable=username)
    username_entry.pack()
    Label(root1,text='Password *',bg='turquoise').pack()
    password_entry=Entry(root1,textvariable=password,show="*")
    password_entry.pack()
    Button(root1,text='Login',width=10,height=1,command=login_user).pack()
    root.mainloop()

def register():
    global root1
    global username1
    global password1
    global username_entry1
    global password_entry1
    root1=Toplevel(root)
    username1=StringVar()
    password1=StringVar()
    root1.configure(bg="turquoise")
    root1.geometry('340x250')
    Label(root1,text='Username *',bg='turquoise').pack()
    username_entry1=Entry(root1,textvariable=username1)
    username_entry1.pack()
    Label(root1,text='Password *',bg='turquoise').pack()
    password_entry1=Entry(root1,textvariable=password1,show="*")
    password_entry1.pack()
    Button(root1,text='Register',width=10,height=1,command=login).pack()
    root.mainloop()
    
def main_screen():
    global root
    root=tk.Tk()
    root.configure(bg="turquoise")
    root.title("Main Page")
    root.geometry('340x250')
    Label(text="Main page",bg='turquoise',font=('TimeRoman',15)).pack()
    Button(text="Login",command=login,height="2",width="30").pack()
    Button(text="Register",command=register,height="2",width="30").pack()
    root.mainloop()
#login page
main_screen()
#authors page

        
        
    
