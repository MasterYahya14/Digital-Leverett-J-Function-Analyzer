# Digital Leverett J-Function Analyzer

## Project Overview
This is a Python-based reservoir engineering tool built from scratch to analyze and normalize core laboratory data. It generates synthetic capillary pressure data, calculates the Leverett J-Function, and visualizes the results to prove reservoir consistency.

## Objectives
* Generate realistic synthetic core data (Porosity, Permeability, Water Saturation, Capillary Pressure).
* Apply the Leverett J-Function to normalize capillary pressure curves.
* Visualize the raw data and the normalized master curve using Matplotlib.
* Automatically generate an engineering summary report for reservoir simulation input.

## Features
* **Physics-Based Data Generation:** Capillary pressure is calculated based on realistic permeability and water saturation relationships.
* **Automated Calculations:** Computes the J-Function using Interfacial Tension (IFT) and Contact Angle.
* **Side-by-Side Visualization:** Instantly compares messy raw curves with the normalized master curve.
* **Statistical Reporting:** Outputs a clear text summary with minimum, maximum, and average J-values.

## Installation
1. Install Python on your computer.
2. Open your terminal and install the required libraries:
   `pip install -r requirements.txt`

## Usage
Run the main script to generate the data, view the graphs, and print the report:
`python main.py`

## Engineering Results
The project successfully demonstrates that diverse capillary pressure curves from different rock types (tight, average, excellent) merge into a single master curve. This proves the rocks share a similar pore throat geometry and confirms the mathematical validity of the Leverett J-Function for reservoir simulation.

## Future Improvements
* Add functionality to read real laboratory data from CSV files.
* Calculate absolute permeability from the master curve.