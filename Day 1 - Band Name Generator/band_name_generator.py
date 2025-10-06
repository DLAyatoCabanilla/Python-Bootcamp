import tkinter as tk
from tkinter import messagebox

# The main function that contains the logic from your original script.
def generate_band_name():
    # Retrieve values from the input fields
    # city = (input("What is the name of your city?\n")) -> implemented by city_entry.get()
    city = city_entry.get().strip()
    # pet = (input("What is the name of your pet?\n")) -> implemented by pet_entry.get()
    pet = pet_entry.get().strip()

    if not city or not pet:
        # Instead of the forbidden alert(), we use tkinter's messagebox for user feedback.
        messagebox.showerror("Missing Information", "Please enter both a city and a pet name to generate a band name.")
        return

    # print("Your Band Name is " + city + " " + pet) -> implemented by updating the result label
    band_name = city + " " + pet
    
    # Update the visual label with the result
    result_label.config(
        text=f"Your Band Name is: {band_name}", 
        fg="#e94560"  # Use a vibrant color for the result
    )
    
    # Clear inputs after generation for a clean slate
    city_entry.delete(0, tk.END)
    pet_entry.delete(0, tk.END)


# --- GUI Setup ---

# 1. Initialize the main window
root = tk.Tk()
root.title("Band Name Generator 🥁")
root.geometry("450x450")
root.config(bg="#1a1a2e") # Dark background

# Center the content using a frame
main_frame = tk.Frame(root, bg="#1a1a2e", padx=20, pady=20)
main_frame.pack(expand=True)

# 2. Welcome Message
welcome_label = tk.Label(
    main_frame,
    text="Welcome to the Band Name Generator! 🥁",
    font=("Inter", 16, "bold"),
    fg="white",
    bg="#1a1a2e",
    pady=10
)
welcome_label.pack()

# 3. City Input
city_label = tk.Label(
    main_frame,
    text="What is the name of your city?",
    font=("Inter", 10),
    fg="#e94560",
    bg="#1a1a2e",
    anchor="w"
)
city_label.pack(fill='x', pady=(10, 2))

city_entry = tk.Entry(
    main_frame,
    font=("Inter", 12),
    bg="#0f3460",
    fg="white",
    insertbackground="white",
    bd=0,
    highlightthickness=1,
    highlightbackground="#e94560",
    highlightcolor="#e94560"
)
city_entry.pack(fill='x', ipady=5)

# 4. Pet Input
pet_label = tk.Label(
    main_frame,
    text="What is the name of your pet?",
    font=("Inter", 10),
    fg="#e94560",
    bg="#1a1a2e",
    anchor="w"
)
pet_label.pack(fill='x', pady=(10, 2))

pet_entry = tk.Entry(
    main_frame,
    font=("Inter", 12),
    bg="#0f3460",
    fg="white",
    insertbackground="white",
    bd=0,
    highlightthickness=1,
    highlightbackground="#e94560",
    highlightcolor="#e94560"
)
pet_entry.pack(fill='x', ipady=5)

# 5. Generate Button
generate_button = tk.Button(
    main_frame,
    text="Generate Band Name",
    command=generate_band_name,
    font=("Inter", 12, "bold"),
    bg="#e94560",
    fg="white",
    activebackground="#d13a52",
    activeforeground="white",
    bd=0,
    relief=tk.FLAT,
    cursor="hand2"
)
generate_button.pack(fill='x', pady=20, ipady=5)

# 6. Result Label
result_label = tk.Label(
    main_frame,
    text="Your Band Name is: ",
    font=("Inter", 14),
    fg="white",
    bg="#1a1a2e"
)
result_label.pack(pady=5)

# Start the application main loop
if __name__ == "__main__":
    root.mainloop()
