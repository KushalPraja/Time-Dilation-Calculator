import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_time_dilation(speed_percentage, years_relative):
    try:
        # Speed of light in m/s
        c = 299792458
        # Convert speed percentage to a factor of the speed of light
        speed_factor = speed_percentage / 100
        # Velocity in m/s
        velocity = speed_factor * c
        # Lorentz factor formula for time dilation
        lorentz_factor = (1 - (velocity**2 / c**2))**0.5
        # Real world time calculation
        real_time = years_relative / lorentz_factor

        # Display the steps
        steps_text.set(
            f"Step 1: Speed Percentage to Velocity\n"
            f"  Velocity = {speed_percentage}% of light speed = {velocity:.2f} m/s\n\n"
            f"Step 2: Lorentz Factor Calculation\n"
            f"  Lorentz Factor = 1 / sqrt(1 - (v^2 / c^2)) = {lorentz_factor:.4f}\n\n"
            f"Step 3: Real World Time Calculation\n"
            f"  Real World Time = Relative Time / Lorentz Factor = {years_relative} years / {lorentz_factor:.4f} = {real_time:.2f} years"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Time Dilation Calculator")
root.geometry("800x600")

# Load background image
background_image = Image.open("background.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

frame = ttk.Frame(root, padding="10", style="TFrame")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the frame
x_coord = (screen_width - 800) // 2
y_coord = (screen_height - 600) // 2

# Set the geometry of the frame
frame.grid(row=0, column=0, padx=x_coord, pady=y_coord)

# Add a custom style to set the font size
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))

# Add title label
title_label = ttk.Label(frame, text="Time Dilation Calculator by Kushal", font=("Courier", 16, "bold"))
title_label.grid(column=0, row=0, columnspan=2, pady=10)

speed_label = ttk.Label(frame, text="Speed Percentage of Light:")
speed_label.grid(column=0, row=1, sticky=tk.W)

speed_entry = ttk.Entry(frame)
speed_entry.grid(column=1, row=1, sticky=tk.W)

years_label = ttk.Label(frame, text="Years Relative to Traveler:")
years_label.grid(column=0, row=2, sticky=tk.W)

years_entry = ttk.Entry(frame)
years_entry.grid(column=1, row=2, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Calculate", command=lambda: calculate_time_dilation(float(speed_entry.get()), float(years_entry.get())))
calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

# Display the steps
steps_text = tk.StringVar()
steps_label = ttk.Label(frame, textvariable=steps_text, wraplength=750, justify=tk.LEFT)
steps_label.grid(column=0, row=4, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
