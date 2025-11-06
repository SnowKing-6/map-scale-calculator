import customtkinter as ctk

#-------------------------------------------
# Function to calculate the map scale
def calculate_scale():
    try:
        # Read values from input fields
        map_length = float(length_map_entry.get())
        real_length = float(length_real_entry.get())
        unit = length_unit_option.get()

        # Validate input values
        if map_length <= 0 or real_length <= 0:
            result_label.configure(text="❌ Values must be positive.")
            return

        # Convert the real length to centimeters based on the selected unit
        if unit == "cm":
            real_length_cm = real_length
        elif unit == "m":
            real_length_cm = real_length * 100
        elif unit == "km":
            real_length_cm = real_length * 100000
        elif unit == "hectare":
            # Hectare is not a linear unit, so scale calculation doesn’t make sense
            result_label.configure(text="⚠️ Scale cannot be calculated using hectares (not a length unit).")
            return
        else:
            result_label.configure(text="❌ Unknown unit.")
            return

        # Calculate the scale ratio
        scale = real_length_cm / map_length

        # Display the formatted result
        result_label.configure(text=f"📏 Scale = 1 : {format_scale(scale)}")

    except ValueError:
        result_label.configure(text="⚠️ Please enter valid numeric values.")


def format_scale(value):
    """Format the number with commas for easier reading"""
    return f"{value:,.0f}"

#-------------------------------------------
# Create and configure the main window
app = ctk.CTk()
app.geometry("400x400")
app.title("Map Scale Calculator")
app.resizable(False, False)
#-------------------------------------------

# Main title
title_label = ctk.CTkLabel(app, text="Map Scale Calculator", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

# Map length input
length_map_label = ctk.CTkLabel(app, text="Length on the map (cm):")
length_map_label.pack(pady=5)
length_map_entry = ctk.CTkEntry(app)
length_map_entry.pack(pady=5)

# Real length input
length_real_label = ctk.CTkLabel(app, text="Actual real-world length:")
length_real_label.pack(pady=5)
length_real_entry = ctk.CTkEntry(app)
length_real_entry.pack(pady=5)

# Unit selection
length_unit_label = ctk.CTkLabel(app, text="Select the unit of real length:")
length_unit_label.pack(pady=5)
length_unit_option = ctk.CTkOptionMenu(app, values=["cm", "m", "km", "hectare"])
length_unit_option.pack(pady=5)

# Calculate button
calc_button = ctk.CTkButton(app, text="Calculate Scale", command=calculate_scale)
calc_button.pack(pady=20)

# Result label
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
result_label.pack(pady=10)

#-------------------------------------------
# Run the main event loop
app.mainloop()
