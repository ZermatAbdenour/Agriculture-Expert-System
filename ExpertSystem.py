from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask

#PH Levels
def PHLevel(kb,value): #Value is in Celsius
    Class = ''
    if(value<6.5):
        Class = 'Acidic'
    elif(value< 7.5):
        Class = 'Neutral'
    else:
        Class = 'Alkaline'
        
    return expr(f'PHLevel({Class})')

#Nutrients
def Nutrient(kb,values):
    Nutrients = list()
    for value in values:
        Nutrients.append(expr(f'Nutrient({value})'))
    return Nutrients

#Drainage properties
def Drainage(kb,value):
    return expr(f'Drainage({value})')

#Temperature
def Temperature(kb,value): #Value is in Celsius
    Class = ''
    if(value<15):
        Class = 'Low'
    elif(value< 25):
        Class = 'Moderate'
    else:
        Class = 'High'
        
    return expr(f'Temperature({Class})')

#Precipitation
def Precipitation(kb,value):#value is in cm
    Class = ''
    if(value<50):
        Class = 'Low'
    elif(value< 150):
        Class = 'Moderate'
    else:
        Class = 'High'
        
    return expr(f'Precipitation({Class})')

#Categories
categories = ['Citrus']

def GetRecommendations(PHLevelvalue,Temperaturevalue,Precipitationvalue,Drainagevalue,Nutrientsvalue):
    print(PHLevelvalue,Temperaturevalue,Precipitationvalue,Drainagevalue,Nutrientsvalue)
    kb = FolKB()
    # Define the rules
    DefineRules(kb)
    
    # Define the agenda
    agenda = []

    agenda.append(PHLevel(kb,PHLevelvalue))
    agenda.append(Temperature(kb,Temperaturevalue))
    agenda.append(Precipitation(kb,Precipitationvalue))
    agenda.append(Drainage(kb,Drainagevalue))
    agenda.extend(Nutrient(kb,Nutrientsvalue))

    # Temporary memory
    memory = []

    # Run the expert system
    seen = set()  # Keep track of the conditions already processed
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue  # Skip the condition if it has already been processed
        seen.add(p)
        kb.tell(p)
        results = list(fol_fc_ask(kb, expr('CanPlant(x)')))
        for result in results:
            if result.get('x') in categories:
                agenda.append(expr(f'CanPlantCategory({result})'))
            else:
                if(result not in memory):
                    memory.append(result)

    
    return memory
        
        
def DefineRules(kb):
    # Rice
    kb.tell(expr('PHLevel(Acidic) & (Drainage(Poor) or Drainage(Moderate)) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Rice)'))

    kb.tell(expr('PHLevel(Acidic) & Nutrient(Phosphorus) ==> CanPlantCategory(Citrus)'))
    kb.tell(expr('CanPlantCategory(Citrus) & Nutrient(Potassium) ==> CanPlant(Lemon)'))
    # Wheat
    kb.tell(expr('(PHLevel(Neutral) or PHLevel(Alkaline)) & Drainage(Well) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) & Nutrient(Sulfur) ==> CanPlant(Wheat)'))

    # Corn
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral)) & Drainage(Well) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Corn)'))

    # Soybeans
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral) or PHLevel(Alkaline)) & (Drainage(Moderate) or Drainage(Well)) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Soybeans)'))

    # Potatoes
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral)) & Drainage(Moderate) & Temperature(Low) & Precipitation(High) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) & Nutrient(Calcium) ==> CanPlant(Potatoes)'))

    # Tomato
    kb.tell(expr('PHLevel(Acidic) & Drainage(Well) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) & Nutrient(Calcium) ==> CanPlant(Tomato)'))

    # Carrot
    kb.tell(expr('(PHLevel(Neutral) or PHLevel(Acidic)) & Drainage(Moderate) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Carrot)'))

    # Lettuce
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral)) & Drainage(Moderate) & Temperature(Moderate) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Lettuce)'))

    # Cabbage
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral)) & Drainage(Moderate) & Temperature(Low) & Precipitation(High) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) & Nutrient(Calcium) ==> CanPlant(Cabbage)'))

    # Spinach
    kb.tell(expr('(PHLevel(Acidic) or PHLevel(Neutral)) & Drainage(Moderate) & Temperature(Low) & Precipitation(Moderate) & Nutrient(Nitrogen) & Nutrient(Phosphorus) & Nutrient(Potassium) ==> CanPlant(Spinach)'))
