import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.title("Kalkulator Keuangan")

# Variabel dan fungsi
modal = tk.StringVar()
tingkat_bunga = tk.StringVar()
waktu = tk.StringVar()
n = tk.StringVar()

def bunga_sederhana(modal, tingkat_bunga, waktu):
    try:
        modal2 = float(modal)
        bunga = float(tingkat_bunga)
        waktu2 = float(waktu)
    except ValueError:
        showinfo(title="Error", message="Masukkan angka yang valid untuk Modal, Tingkat bunga, dan Waktu.")
        return None
    
    tb = bunga / 100
    return modal2 * (1 + tb * waktu2)
    
def bunga_majemuk(modal, tingkat_bunga, waktu, n):
    try:
        modal2 = float(modal)
        bunga = float(tingkat_bunga)
        waktu2 = float(waktu)
        n = int(n)
    except ValueError:
        showinfo(title="Error", message="Masukkan angka yang valid untuk Modal, Tingkat bunga, Waktu, dan frekuensi majemuk.")
        return None
    
    tb = bunga / 100
    return modal2 * (1 + tb / n) ** (n * waktu2)

def show_result(result):
    result_window = tk.Toplevel(window)
    result_window.title("Hasil Perhitungan")
    result_window.geometry("300x200")

    result_label = ttk.Label(result_window, text=f"""
        Modal\t\t: RP. {float(modal.get()):,.2f}
        Tingkat Bunga \t: {tingkat_bunga.get()} %
        Waktu \t \t: {waktu.get()} Tahun
        Hasil \t \t: RP. {result:,.2f}""")
    result_label.pack(pady=20)

def calculate_simple_interest():
    result = bunga_sederhana(modal.get(), tingkat_bunga.get(), waktu.get())
    if result is not None:
        show_result(result)

def calculate_compound_interest():
    result = bunga_majemuk(modal.get(), tingkat_bunga.get(), waktu.get(), n.get())
    if result is not None:
        show_result(result)

def tampilan_sederhana():
    form_window = tk.Toplevel(window)
    form_window.title("Form Bunga Sederhana")
    form_window.geometry("300x300")

    modal_label = ttk.Label(form_window, text="Masukkan Modal:")
    modal_label.pack(pady=10)
    modal_entry = ttk.Entry(form_window, textvariable=modal)
    modal_entry.pack(pady=10)

    tingkat_bunga_label = ttk.Label(form_window, text="Masukkan Tingkat Bunga (%):")
    tingkat_bunga_label.pack(pady=10)
    tingkat_bunga_entry = ttk.Entry(form_window, textvariable=tingkat_bunga)
    tingkat_bunga_entry.pack(pady=10)

    waktu_label = ttk.Label(form_window, text="Masukkan Waktu (tahun):")
    waktu_label.pack(pady=10)
    waktu_entry = ttk.Entry(form_window, textvariable=waktu)
    waktu_entry.pack(pady=10)

    calculate_button = ttk.Button(form_window, text="Hitung!", command=calculate_simple_interest)
    calculate_button.pack(pady=10)

def tampilan_majemuk():
    form_window = tk.Toplevel(window)
    form_window.title("Form Bunga Majemuk")
    form_window.geometry("300x400")

    modal_label = ttk.Label(form_window, text="Masukkan Modal:")
    modal_label.pack(pady=10)
    modal_entry = ttk.Entry(form_window, textvariable=modal)
    modal_entry.pack(pady=10)

    tingkat_bunga_label = ttk.Label(form_window, text="Masukkan Tingkat Bunga (%):")
    tingkat_bunga_label.pack(pady=10)
    tingkat_bunga_entry = ttk.Entry(form_window, textvariable=tingkat_bunga)
    tingkat_bunga_entry.pack(pady=10)

    waktu_label = ttk.Label(form_window, text="Masukkan Waktu (tahun):")
    waktu_label.pack(pady=10)
    waktu_entry = ttk.Entry(form_window, textvariable=waktu)
    waktu_entry.pack(pady=10)

    n_label = ttk.Label(form_window, text="Masukkan jumlah  bunga majemuk per tahun:")
    n_label.pack(pady=10)
    n_entry = ttk.Entry(form_window, textvariable=n)
    n_entry.pack(pady=10)

    calculate_button = ttk.Button(form_window, text="Hitung!", command=calculate_compound_interest)
    calculate_button.pack(pady=10)

# Tampilan utama
choice_label = ttk.Label(window, text="Pilih jenis perhitungan:")
choice_label.pack(pady=10)

simple_interest_button = ttk.Button(window, text="Bunga Sederhana", command=tampilan_sederhana)
simple_interest_button.pack(pady=10)

compound_interest_button = ttk.Button(window, text="Bunga Majemuk", command=tampilan_majemuk)
compound_interest_button.pack(pady=10)

window.mainloop()
