import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)

angka_pertama_var = tk.StringVar()
angka_kedua_var = tk.StringVar()
penghitung_var = tk.StringVar()

def calculate():
    try:
        angka_pertama = int(angka_pertama_var.get())
        angka_kedua = int(angka_kedua_var.get())
        penghitung = penghitung_var.get()
    except ValueError:
        showinfo(title="Error", message="Masukkan angka dan penghitung yang valid.")
        return

    if penghitung == "+":
        hasil = angka_pertama + angka_kedua
    elif penghitung == "-":
        hasil = angka_pertama - angka_kedua
    elif penghitung == "*":
        hasil = angka_pertama * angka_kedua
    elif penghitung == "/":
        try:
            hasil = angka_pertama / angka_kedua
        except ZeroDivisionError:
            showinfo(title="Error", message="Pembagian dengan nol tidak diperbolehkan.")
            return
    else:
        showinfo(title="Error", message="Masukkan penghitung yang valid (+, -, *, /).")
        return

    label_result.config(text=f"Result: {hasil}")

# label angka pertama
angka_pertama_label = tk.Label(root, text="Masukkan angka pertama:")
angka_pertama_label.pack(pady=10, padx=100)

# entry angka pertama
angka_pertama_entry = tk.Entry(root, textvariable=angka_pertama_var)
angka_pertama_entry.pack(pady=10, padx=10)

# label angka kedua
angka_kedua_label = tk.Label(root, text="Masukkan angka kedua:")
angka_kedua_label.pack(pady=10, padx=100)

# entry angka kedua
angka_kedua_entry = tk.Entry(root, textvariable=angka_kedua_var)
angka_kedua_entry.pack(pady=10, padx=10)

# label penghitung
penghitung_label = tk.Label(root, text="Masukkan penghitung (+, -, *, /):")
penghitung_label.pack(pady=10, padx=100)

# entry penghitung
penghitung_entry = tk.Entry(root, textvariable=penghitung_var)
penghitung_entry.pack(pady=10, padx=10)

# tombol calculate
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10, padx=10)

# label hasil
label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10, padx=10)

root.mainloop()
