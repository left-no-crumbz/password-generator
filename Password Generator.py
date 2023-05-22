import string, secrets, customtkinter
import tkinter as tk


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

class Password_Generator:
    def __init__(self):
        super().__init__()
        
        # Enforces proper password length
        self.INITIAL_LENGTH = 12
        self.FINAL_LENGTH = 50
        
        # Initializing the font for the GUI.
        self.title_font = ("Arial", 18)
        self.main_font = ("Arial", 16)
        self.sub_font = ("Arial", 12)
        
        self.root = customtkinter.CTk()
        self.root.geometry(f"{1100}x{580}")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        
        self.empty = customtkinter.CTkLabel(self.frame, text="")
        self.empty.pack(padx=12, pady=50)

        
        self.title_label = customtkinter.CTkLabel(self.frame, text="Password Generator", font=self.title_font)
        self.title_label.pack(padx=12, pady=10)
        
        # Initializes the slider. The slider controls the password generation
        self.password_length = customtkinter.CTkSlider(master=self.frame, from_=self.INITIAL_LENGTH, to=self.FINAL_LENGTH, orientation='horizontal', hover=True, command=self.generate_password, number_of_steps=38)
        self.password_length.pack(padx=12, pady=5)
        
        # Initializes the counter below the slider
        self.length = customtkinter.CTkEntry(master=self.frame, show='', font=self.sub_font, width=30, justify='center')
        self.length.pack(padx=2, pady=2)
        
        # Initializes the checkboxes
        self.checkboxes = {
            "Letters": customtkinter.BooleanVar(value=True),
            "Numbers": customtkinter.BooleanVar(value=True),
            "Special": customtkinter.BooleanVar(value=True)
        }
        self.check_lettercase = customtkinter.CTkCheckBox(self.frame, text="Letters", font=self.main_font, variable=self.checkboxes.get("Letters"))
        self.check_lettercase.pack(padx=2, pady=2)
        self.check_numbercase = customtkinter.CTkCheckBox(self.frame, text="Numbers", font=self.main_font, variable=self.checkboxes.get("Numbers"))
        self.check_numbercase.pack(padx=2, pady=2)
        self.check_specialcase = customtkinter.CTkCheckBox(self.frame, text="Special", font=self.main_font, variable=self.checkboxes.get("Special"))
        self.check_specialcase.pack(padx=2, pady=2)
    
    
        self.show_password = customtkinter.CTkEntry(master=self.frame, show='', font=self.sub_font, width=365)
        self.show_password.pack(padx=10, pady=10)
        
        self.copy = customtkinter.CTkButton(master=self.frame, text='Copy to Clipboard', font=self.title_font, command=self.copy_to_clipboard, hover=True)
        self.copy.pack(padx=10, pady=10)
        
        self.root.mainloop()
    def generate_password(self, password_length):
        self.length.delete(0, 'end')
        self.length.insert(0, int(password_length))
        alphabet_list = list(string.ascii_letters)
        number_list = list(string.digits)
        special_list = list(string.punctuation)
        password_list = []
        password = ""

        if self.checkboxes["Letters"].get() is True:
            password_list.extend(alphabet_list)
        if self.checkboxes["Numbers"].get() is True:
            password_list.extend(number_list)
        if self.checkboxes["Special"].get() is True:
            password_list.extend(special_list)

        
        if all(value.get() for value in self.checkboxes.values()):
            while True:
                password = ''.join(secrets.choice(password_list) for i in range(int(password_length)))
                if (any(char.islower() for char in password)
                        and any(char.isupper() for char in password)
                        and any(char.isdigit() for char in password)
                        and any(not char.isalnum() for char in password)): 
                    break

        elif any(value.get() for value in self.checkboxes.values()):
            if self.checkboxes["Letters"].get() is True:
                while True:
                    password = ''.join(secrets.choice(password_list) for i in range(int(password_length)))
                    if (any(char.islower() for char in password) or any(char.isupper() for char in password)):
                        break
            if self.checkboxes["Numbers"].get() is True:
                while True:
                    password = ''.join(secrets.choice(password_list) for i in range(int(password_length)))
                    if (any(char.isdigit() for char in password)):
                        break
            if self.checkboxes["Special"].get() is True:
                while True:
                    password = ''.join(secrets.choice(password_list) for i in range(int(password_length)))
                    if (any(not char.isalnum() for char in password)):
                        break

        self.show_password.delete(0, 'end')
        self.show_password.insert(0, password)
        
    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.show_password.get())
        
        self.popup = customtkinter.CTkLabel(master=self.frame, text='Copied to Clipboard!', font=self.sub_font, fg_color='transparent')
        self.popup.pack(padx=5, pady=5)
        self.popup.after(2000, self.popup.destroy)


if __name__ == "__main__":
    app = Password_Generator()




