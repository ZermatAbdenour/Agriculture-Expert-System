import customtkinter
from InterfaceAddons import ScrollableCheckBoxFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agriculture Expert System")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        
        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self,label="Nutrients", width=200, command=self.checkbox_frame_event,
                                                                 item_list=[f"item {i}" for i in range(5)])
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

        
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

customtkinter.set_appearance_mode("dark")
app = App()
app.mainloop()