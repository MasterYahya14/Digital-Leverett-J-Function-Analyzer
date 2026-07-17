# 1. Bring in all our tools from our other files
from data_generator import generate_core_data
from calculations import calculate_j_function
from plotting import plot_multiple_rocks
from report import generate_summary_report

print("Starting Reservoir Core Analysis Project...")

# 2. Create an empty list (a filing cabinet) to hold our finished rocks
all_analyzed_rocks = []

# 3. Create Rock 1: A very tight rock (low permeability)
rock1 = generate_core_data("Core_1_Tight", porosity=0.10, permeability=10)
rock1 = calculate_j_function(rock1, interfacial_tension=30, contact_angle_degrees=0)
all_analyzed_rocks.append(rock1) # Put it in the filing cabinet

# 4. Create Rock 2: An average rock
rock2 = generate_core_data("Core_2_Average", porosity=0.20, permeability=100)
rock2 = calculate_j_function(rock2, interfacial_tension=30, contact_angle_degrees=0)
all_analyzed_rocks.append(rock2) # Put it in the filing cabinet

# 5. Create Rock 3: A fantastic rock (high permeability)
rock3 = generate_core_data("Core_3_Excellent", porosity=0.30, permeability=500)
rock3 = calculate_j_function(rock3, interfacial_tension=30, contact_angle_degrees=0)
all_analyzed_rocks.append(rock3) # Put it in the filing cabinet

# 6. Send the whole cabinet to our new plotting function!
print("Data calculated! Now drawing the graphs...")
plot_multiple_rocks(all_analyzed_rocks)

# 7. Generate the final text report
print("Graphs closed. Generating final report...")
generate_summary_report(all_analyzed_rocks)