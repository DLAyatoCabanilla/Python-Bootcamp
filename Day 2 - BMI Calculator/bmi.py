import tkinter as tk
from tkinter import messagebox

# --- BMI Categories and Colors ---
BMI_CATEGORIES = {
    (0, 18.5): ("Underweight", "lightblue"),
    (18.5, 25): ("Normal Weight", "lightgreen"),
    (25, 30): ("Overweight", "gold"),
    (30, 100): ("Obesity", "salmon")
}

def calculate_bmi():
    """Calculates BMI and updates the result label in the GUI."""
    try:
        # 1. Get and convert input from the entry fields
        # Use .get() to retrieve the string from the Entry widget
        weight_kg = float(weight_entry.get())
        height_m = float(height_entry.get())

        # 2. Validation
        if height_m <= 0 or weight_kg <= 0:
            messagebox.showerror("Input Error", "Height and weight must be positive numbers.")
            return

        # 3. Calculate BMI: weight / (height ** 2)
        bmi = weight_kg / (height_m ** 2)
        
        # Round the BMI to 1 decimal place for display
        bmi_rounded = round(bmi, 1)

        # 4. Determine category and color
        category_text = "N/A"
        category_color = "white"
        
        for (low, high), (category, color) in BMI_CATEGORIES.items():
            if low <= bmi_rounded < high:
                category_text = category
                category_color = color
                break
        
        # 5. Update the GUI result label
        result_label.config(
            text=f"Your BMI: {bmi_rounded}\nCategory: {category_text}",
            bg=category_color  # Change background color for visualization
        )

    except ValueError:
        # Handle cases where the user enters non-numeric text
        messagebox.showerror("Input Error", "Please enter valid numerical values for height and weight.")
        # Reset the result label on error
        result_label.config(text="Enter your details and click Calculate.", bg="white")


# --- GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
# Set window size
root.geometry("300x200") 

# 1. Height Input (Label and Entry)
height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(root, width=10)
height_entry.grid(row=0, column=1, padx=10, pady=5)
height_entry.focus() # Start cursor here

# 2. Weight Input (Label and Entry)
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(root, width=10)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

# 3. Calculate Button
calculate_button = tk.Button(
    root, 
    text="Calculate BMI", 
    command=calculate_bmi,  # This links the button press to the function
    bg="blue", 
    fg="white", 
    font=("Arial", 10, "bold")
)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# 4. Result Display Label (The Visualization)
result_label = tk.Label(
    root, 
    text="Enter your details and click Calculate.",
    bg="white",
    width=30,
    height=2,
    relief="sunken"  # Gives it a 3D, sunken appearance
)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()