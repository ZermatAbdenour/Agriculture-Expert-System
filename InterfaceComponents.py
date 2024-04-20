import customtkinter
from PIL import Image, ImageTk
from ExpertSystem import GetRecommendations

class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list)+1, column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return
    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]   
    
class ScrollableResultFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.command = command
        self.results_list = []
        if(len(item_list)==0):
            noResult = customtkinter.CTkLabel(self, text="No Results", font=('Arial', 20, 'bold'))
            noResult.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        else:
            for i, item in enumerate(item_list):
                self.add_item(item)
    def add_item(self, item):
        result = ResultFrame(
            self,
            plant_name="Sunflower",
            plant_description="Sunflowers are tall plants with large yellow flowers. They are known for turning their heads to follow the sun.",
            image_path="sunflower.jpg"
        )
        if self.command is not None:
            result.configure(command=self.command)
        result.grid(row=len(self.results_list)+1, column=0, pady=(0, 10),sticky="nwe")
        self.results_list.append(result)

    
class ScrollableRadiobuttonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        radiobutton = customtkinter.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()
    
class ValueInputsFrame(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Register the validation function
        validate_command = master.register(self.validate_numeric_input)

        # Create labels and entry widgets for numeric values
        # Label and entry for the first input
        PHLevellabel = customtkinter.CTkLabel(self, text="PHLevel:")
        PHLevellabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.PHLevelEntry = customtkinter.CTkEntry(self, validate="key", validatecommand=(validate_command, '%P'))
        self.PHLevelEntry.grid(row=0, column=1, padx=5, pady=5)
        self.PHLevelEntry.insert(0, "5")

        # Label and entry for the second input
        Temperaturelabel = customtkinter.CTkLabel(self, text="Temperature:")
        Temperaturelabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.TemperatureEntry = customtkinter.CTkEntry(self, validate="key", validatecommand=(validate_command, '%P'))
        self.TemperatureEntry.grid(row=1, column=1, padx=5, pady=5)
        self.TemperatureEntry.insert(0, "20")

        # Label and entry for the third input
        Precipitationlabel = customtkinter.CTkLabel(self, text="Precipitation:")
        Precipitationlabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.PrecipitationEntry = customtkinter.CTkEntry(self, validate="key", validatecommand=(validate_command, '%P'))
        self.PrecipitationEntry.grid(row=2, column=1, padx=5, pady=5)
        self.PrecipitationEntry.insert(0, "100")

    def validate_numeric_input(self, input_value):
        """Function to validate numeric input in the entry widgets."""
        # Check if the input_value can be converted to a float
        try:
            float(input_value)
            return True
        except ValueError:
            return input_value == ""
        
class OutputFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        
        result_frame = ResultFrame(
            self,
            plant_name="Sunflower",
            plant_description="Sunflowers are tall plants with large yellow flowers. They are known for turning their heads to follow the sun.",
            image_path="sunflower.jpg"
        )
        result_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
        
        button = customtkinter.CTkButton(self, text="Get Recommendations", font=('Arial', 20, 'bold'), command=self.get_recommendations)
        button.grid(row=1, column=0, padx=10, pady=10, sticky="nwe")
    def get_recommendations(self): 
        #Clear frame
        for widget in self.winfo_children():
            widget.destroy()
        self.pack_forget()  
        self.grid_columnconfigure(0, weight=1)  
        self.grid_rowconfigure(0, weight=1) 
        #get the recomandations
        agenda = self.master.leftframe.getAgenda()
        print(agenda)
        recomandations = GetRecommendations(agenda["PHLevel"],agenda["Temperature"],agenda["Precipitation"],agenda["Drainage"],agenda["Nutrients"])
        print(recomandations)
        #diplay the recomandations
        i = 0
        
        scrolableframe = ScrollableResultFrame(self, item_list=recomandations)
        scrolableframe.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        
        button = customtkinter.CTkButton(self, text="Get Recommendations", font=('Arial', 20, 'bold'), command=self.get_recommendations)
        button.grid(row=1, column=0, padx=10, pady=10, sticky="nwe")
        self.update_idletasks()
        

        
class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, parent, plant_name, plant_description, image_path, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        
        # Create a label for the plant's name
        self.name_label = customtkinter.CTkLabel(self, text=plant_name, font=('Arial', 20, 'bold'))
        self.name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        # Load the image from the given path and create a label for it
        self.image = Image.open(image_path)
        self.image = self.image.resize((100, 100))  # Resize the image to 100x100 pixels
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = customtkinter.CTkLabel(self, image=self.photo, text="")
        self.image_label.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky='e')

        # Create a label for the plant's description
        self.description_label = customtkinter.CTkLabel(self, text=plant_description)
        self.description_label.grid(row=1, column=0, sticky='wn', padx=10, pady=5)

        
    

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_rowconfigure(0, weight=1)  
        self.grid_rowconfigure(1, weight=1)  
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)       
        self.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        
        self.text = customtkinter.CTkLabel(self, text="Characteristics", font=('Arial', 20, 'bold'))
        self.text.grid(row=0, column=0, padx=15, pady=20, sticky="nsew")
        
        #Inputs
        self.value_inputs_frame = ValueInputsFrame(master=self)
        self.value_inputs_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")
        
        #Drainage
        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self,
                                                                       item_list=['Poor','Moderate','Well'],
                                                                       label_text="Drainage")
        self.scrollable_radiobutton_frame.grid(row=2, column=0, padx=15, pady=15, sticky="nsew")
               
        #Nutrients
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, command=self.checkbox_frame_event,
                                                                 item_list=['Nitrogen','Phosphorus','Potassium','Calcium','Magnesium','Sulfur'],label_text="Nutrients")
        self.scrollable_checkbox_frame.grid(row=3, column=0, padx=15, pady=15, sticky="nsew")

    def getAgenda(self):
        agenda = {}
        agenda["PHLevel"] = float(self.value_inputs_frame.PHLevelEntry.get())
        agenda["Temperature"] = float(self.value_inputs_frame.TemperatureEntry.get())
        agenda["Precipitation"] = float(self.value_inputs_frame.PrecipitationEntry.get())
        agenda["Drainage"] = self.scrollable_radiobutton_frame.get_checked_item()
        agenda["Nutrients"] = self.scrollable_checkbox_frame.get_checked_items()
        return agenda
        
        
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}") 