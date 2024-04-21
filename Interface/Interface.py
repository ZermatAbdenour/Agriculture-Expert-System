import customtkinter
from InterfaceComponents import OutputFrame,InputFrame
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agriculture Expert System")
        
        # create scrollable checkbox frame
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  
        
        self.leftframe = InputFrame(self)
        self.leftframe.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        
        self.rightframe = OutputFrame(self)
        self.rightframe.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        

customtkinter.set_appearance_mode("dark")
app = App()
app.mainloop()