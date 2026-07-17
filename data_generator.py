import numpy as np

def generate_core_data(core_id, porosity, permeability):
    # 1. Create a list of Water Saturation (Sw) numbers from 0.2 to 1.0
    # np.linspace makes exactly 20 evenly spaced numbers between our start and end
    sw_values = np.linspace(0.2, 1.0, 50)
    
    # 2. Calculate Capillary Pressure (Pc) based on physics
    # We use a math formula so that higher permeability creates lower pressure
    # The '1.0 / sw_values' part creates a curve that looks like a slide
    pc_values = (1.0 / sw_values) * 50.0 * np.sqrt(porosity/permeability)
    
    # 3. Pack everything neatly into a dictionary (a labeled box)
    core_data = {
        "Core ID": core_id,
        "Porosity": porosity,
        "Permeability": permeability,
        "Sw": sw_values,
        "Pc": pc_values
    }
    
    return core_data

# --- The Testing Area ---
# This code at the bottom only runs if we run this specific file directly
if __name__ == "__main__":
    # Let's test our factory by making a fake rock sample
    my_rock = generate_core_data("Rock_A", 0.20, 100) 
    
    print("Successfully created data for:", my_rock["Core ID"])
    print("\nHere are the first 5 Water Saturation numbers:")
    print(my_rock["Sw"][:5])
    print("\nHere are the first 5 Capillary Pressure numbers:")
    print(my_rock["Pc"][:5])