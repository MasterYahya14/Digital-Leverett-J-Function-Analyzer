import numpy as np

# We import the factory we built in Stage 2 so we can use it here
from data_generator import generate_core_data

def calculate_j_function(core_data, interfacial_tension, contact_angle_degrees):
    # 1. Pull out the numbers we need from our labeled box (the dictionary)
    pc = core_data["Pc"]
    k = core_data["Permeability"]
    phi = core_data["Porosity"]
    
    # 2. Python's math brain needs angles in radians, not degrees. We convert it.
    theta_radians = np.radians(contact_angle_degrees)
    
    # 3. We break the Leverett formula into smaller pieces so it is easy to read
    rock_part = np.sqrt(k / phi)
    fluid_part = interfacial_tension * np.cos(theta_radians)
    
    # 4. Calculate the final J values using the industry constant 0.21645
    j_values = 0.21645 * (pc / fluid_part) * rock_part
    
    # 5. Add our new J values into the same labeled box so we don't lose them
    core_data["J"] = j_values
    
    return core_data

# --- The Testing Area ---
if __name__ == "__main__":
    # First, make a fake rock from our Stage 2 factory
    my_rock = generate_core_data("Rock_B", 0.25, 200)
    
    # Next, calculate the J-function. 
    # Standard oil and water IFT is about 30 dynes/cm. 
    # A strongly water-wet rock has an angle of 0 degrees.
    analyzed_rock = calculate_j_function(my_rock, 30, 0)
    
    print("Calculations complete for:", analyzed_rock["Core ID"])
    print("\nHere are the first 5 J-Function numbers:")
    print(analyzed_rock["J"][:5])