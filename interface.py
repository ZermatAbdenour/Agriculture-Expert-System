import customtkinter
from InterfaceComponents import ScrollableCheckBoxFrame, ScrollableRadiobuttonFrame,ValueInputsFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agriculture Expert System")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        
        # create scrollable checkbox frame
        
        #Nutrients
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,
                                                                 item_list=['Nitrogen','Phosphorus','Potassium','Calcium','Magnesium','Sulfur'],label_text="Nutrients")
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        
        #Drainage
        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500,
                                                                       item_list=['Poor','Moderate','Well'],
                                                                       label_text="Drainage")
        self.scrollable_radiobutton_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        self.scrollable_radiobutton_frame.configure(width=200)
        
        self.value_inputs_frame = ValueInputsFrame(master=self)
        self.value_inputs_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

customtkinter.set_appearance_mode("dark")
app = App()
app.mainloop()