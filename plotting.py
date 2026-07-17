# Import our graphing toolbox and give it a short nickname 'plt'
import matplotlib.pyplot as plt

# Import the tools we built in Stage 2 and Stage 3
from data_generator import generate_core_data
from calculations import calculate_j_function

def plot_rock_curves(core_data):
    # 1. Pull the data lists out of our dictionary box
    sw = core_data["Sw"]
    pc = core_data["Pc"]
    j_values = core_data["J"]
    core_id = core_data["Core ID"]

    # 2. Create a blank canvas. (10, 5) means 10 inches wide, 5 inches tall.
    plt.figure(figsize=(10, 5))

    # --- First Graph: Capillary Pressure ---
    # plt.subplot(Rows, Columns, Position). We want 1 row, 2 columns, 1st position.
    plt.subplot(1, 2, 1)
    
    # Plot the line. marker='o' puts a little circle on every exact data point.
    plt.plot(sw, pc, marker='o', color='blue', linewidth=2)
    
    # Every engineering graph MUST have labels!
    plt.title(f"{core_id}: Capillary Pressure vs Saturation")
    plt.xlabel("Water Saturation (Sw) - Fraction")
    plt.ylabel("Capillary Pressure (Pc) - psi")
    plt.grid(True) # Adds a background grid to make reading easier

    # --- Second Graph: Leverett J-Function ---
    # Now we move to the 2nd position on our canvas
    plt.subplot(1, 2, 2)
    
    # marker='s' puts a little square (s for square) on the data points.
    plt.plot(sw, j_values, marker='s', color='green', linewidth=2)
    
    plt.title(f"{core_id}: J-Function vs Saturation")
    plt.xlabel("Water Saturation (Sw) - Fraction")
    plt.ylabel("Leverett J-Function - Unitless")
    plt.grid(True)

    # 3. This cleans up the spacing so the titles don't overlap
    plt.tight_layout()

    # 4. Command the computer to pop open a window and display the drawing
    plt.show()

# --- The Testing Area ---
if __name__ == "__main__":
    # Step A: Make a new rock in our digital lab (Porosity 0.15, Permeability 50)
    my_rock = generate_core_data("Rock_C", 0.15, 50)
    
    # Step B: Do the math (IFT = 30, Angle = 0 degrees)
    analyzed_rock = calculate_j_function(my_rock, 30, 0)
    
    # Step C: Give the finished data to our plotting function
    print("Drawing the graphs... a new window should pop up!")
    plot_rock_curves(analyzed_rock)

def plot_multiple_rocks(list_of_rocks):
    # Create a slightly wider canvas for multiple lines
    plt.figure(figsize=(12, 6))

    # --- First Graph: The Messy Capillary Pressures ---
    plt.subplot(1, 2, 1)
    
    # This is a 'for loop'. It goes through the list one by one.
    for rock in list_of_rocks:
        # label=rock["Core ID"] tells the artist to remember the rock's name
        plt.plot(rock["Sw"], rock["Pc"], marker='o', label=rock["Core ID"])
        
    plt.title("Capillary Pressure (Messy Reservoir)")
    plt.xlabel("Water Saturation (Sw)")
    plt.ylabel("Capillary Pressure (Pc) - psi")
    plt.grid(True)
    plt.legend() # This turns on the name tags (the legend) so we know which color is which rock

    # --- Second Graph: The Master J-Function Curve ---
    plt.subplot(1, 2, 2)
    
    for rock in list_of_rocks:
        plt.plot(rock["Sw"], rock["J"], marker='s', label=rock["Core ID"])
        
    plt.title("Leverett J-Function (Normalized Master Curve)")
    plt.xlabel("Water Saturation (Sw)")
    plt.ylabel("Leverett J-Function")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
    