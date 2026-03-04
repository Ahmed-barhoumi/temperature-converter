import tkinter as tk

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = round((fahrenheit - 32) * 5 / 9, 2)
        lbl_result.config(text=f"\N{DEGREE CELSIUS}  {celsius}")
    except ValueError:
        lbl_result.config(text="Enter a valid number!")

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)
window.configure(bg="#F0F4F8")
window.geometry("400x200")

lbl_title = tk.Label(
    master=window,
    text="🌡 Temperature Converter",
    bg="#F0F4F8",
    fg="#2C3E50",
    font=("Helvetica", 16, "bold")
)
lbl_title.grid(row=0, column=0, columnspan=3, pady=(18, 10))

frm_entry = tk.Frame(master=window, bg="#F0F4F8")

ent_temperature = tk.Entry(
    master=frm_entry,
    width=10,
    bg="#FFFFFF",
    fg="#2C3E50",
    font=("Helvetica", 12)
)

lbl_temp = tk.Label(
    master=frm_entry,
    text="\N{DEGREE FAHRENHEIT}",
    bg="#F0F4F8",
    fg="#2C3E50",
    font=("Helvetica", 12)
)

ent_temperature.grid(row=0, column=0, sticky="e", ipady=4)
lbl_temp.grid(row=0, column=1, sticky="w", padx=(4, 0))

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius,
    bg="#3498DB",
    fg="#FFFFFF",
    font=("Helvetica", 13, "bold"),
    relief="raised",
    padx=8
)

lbl_result = tk.Label(
    master=window,
    text="\N{DEGREE CELSIUS}",
    bg="#F0F4F8",
    fg="#27AE60",
    font=("Helvetica", 13, "bold")
)

frm_entry.grid(row=1, column=0, padx=14)
btn_convert.grid(row=1, column=1, padx=10)
lbl_result.grid(row=1, column=2, padx=14)
window.mainloop()
