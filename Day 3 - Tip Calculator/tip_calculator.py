import tkinter as tk
from tkinter import messagebox

def calculate_split():
    """Retrieves inputs from the GUI, calculates the split, and displays the result."""
    try:
        # 1. Get and convert values from Tkinter Entry widgets
        bill = float(bill_entry.get())
        tip_percent = int(tip_entry.get())
        people = int(people_entry.get())
        
        # 2. Validation
        if bill < 0 or tip_percent < 0 or people <= 0:
            messagebox.showerror("Input Error", "Please enter positive numbers for all fields.")
            return

        # 3. Calculation Logic (Same as command-line version)
        tip_as_decimal = tip_percent / 100
        total_bill_with_tip = bill * (1 + tip_as_decimal)
        per_person_pay = total_bill_with_tip / people

        # 4. Format and Update Result Label
        final_amount_formatted = "{:.2f}".format(per_person_pay)
        
        result_label.config(
            text=f"Each person pays: ${final_amount_formatted}",
            bg="lightgreen", # Visual feedback for a successful calculation
            fg="darkgreen",
            font=("Arial", 14, "bold")
        )

    except ValueError:
        # Handle non-numeric input error
        messagebox.showerror("Input Error", "Please ensure all fields contain valid numbers.")
        result_label.config(text="Calculation failed. Check your inputs.", bg="yellow")


# --- GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("500x450") # Set a fixed size

# Use the grid layout manager for a clean form-like structure

# Row 0: Total Bill
tk.Label(root, text="Total Bill ($):", anchor="e", width=20).grid(row=0, column=0, padx=10, pady=5, sticky="w")
bill_entry = tk.Entry(root, width=15)
bill_entry.grid(row=0, column=1, padx=10, pady=5)

# Row 1: Tip Percentage
tk.Label(root, text="Tip Percentage (e.g., 15):", anchor="e", width=20).grid(row=1, column=0, padx=10, pady=5, sticky="w")
tip_entry = tk.Entry(root, width=15)
tip_entry.grid(row=1, column=1, padx=10, pady=5)
tip_entry.insert(0, "15") # Pre-fill with a common tip

# Row 2: Number of People
tk.Label(root, text="People to Split:", anchor="e", width=20).grid(row=2, column=0, padx=10, pady=5, sticky="w")
people_entry = tk.Entry(root, width=15)
people_entry.grid(row=2, column=1, padx=10, pady=5)
people_entry.insert(0, "2") # Pre-fill with a common split

# Row 3: Calculate Button
calculate_button = tk.Button(
    root, 
    text="Calculate Split", 
    command=calculate_split,  # Links to the function
    bg="#4CAF50", # Green background
    fg="white", 
    font=("Arial", 12, "bold")
)
calculate_button.grid(row=3, column=0, columnspan=2, pady=15, padx=10, ipadx=50) # ipadx expands the button

# Row 4: Result Display Label
result_label = tk.Label(
    root, 
    text="Enter details and click Calculate.",
    bg="lightgray",
    width=40,
    height=4,
    relief="sunken" # Gives a distinct look
)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()