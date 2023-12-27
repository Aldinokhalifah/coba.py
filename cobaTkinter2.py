import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x300")
window.resizable(False, False)
window.title("kalkulator kalori")

# variabel dan fungsi
jenisKelamin = tk.StringVar()
BeratBadan = tk.StringVar()
TinggiBadan = tk.StringVar()
Usia = tk.StringVar()
aktivitas = tk.StringVar()


def tombol_click():
    try:
        Berat = float(BeratBadan.get())
        Tinggi = float(TinggiBadan.get())
        Age = float(Usia.get())
    except ValueError:
        showinfo(title="Error", message="Masukkan angka yang valid untuk Berat Badan, Tinggi Badan, dan Usia.")
        return

    if jenisKelamin.get() == "Laki-laki":
        if aktivitas.get() == "Kurang aktif":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.2, 2)
        elif aktivitas.get() == "Aktif ringan":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.375, 2)
        elif aktivitas.get() == "Cukup aktif":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.55, 2)
        elif aktivitas.get() == "Sangat aktif":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.725, 2)
        elif aktivitas.get() == "Ekstra aktif":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.9, 2)
        else:
              showinfo(title="Error", message="Jenis kelamin tidak valid.")
    elif jenisKelamin.get() == "Perempuan":
        if aktivitas.get() == "Kurang aktif":
            hasil = round((447.6 + 9.25 * Berat) + (3.10 * Tinggi) - (4.33 * Age) * 1.2, 2)
        elif aktivitas.get() == "Aktif ringan":
            hasil = round((447.6 + 9.25 * Berat) + (3.10 * Tinggi) - (4.33 * Age) * 1.375, 2)
        elif aktivitas.get() == "Cukup aktif":
            hasil = round((447.6 + 9.25 * Berat) + (3.10 * Tinggi) - (4.33 * Age) * 1.55, 2)
        elif aktivitas.get() == "Sangat aktif":
            hasil = round((447.6 + 9.25 * Berat) + (3.10 * Tinggi) - (4.33 * Age) * 1.725, 2)
        elif aktivitas.get() == "Ekstra aktif":
            hasil = round((88.4 + 13.4 * Berat) + (4.8 * Tinggi) - (5.68 * Age) * 1.9, 2)
        else:
            hasil = round((447.6 + 9.25 * Berat) + (3.10 * Tinggi) - (4.33 * Age) * 1.9, 2)
    else:
        showinfo(title="Error", message="Jenis kelamin tidak valid.")
        return

    pesan = f"""
    =======================================
    Jenis kelamin \t \t \t \t: {jenisKelamin.get()}
    Berat badan \t \t \t \t: {Berat} KG
    Tinggi badan \t \t \t \t: {Tinggi} CM
    Usia  \t \t \t \t \t: {Age} Tahun
    Kebutuhan kalori harian anda adalah \t: {hasil} kcal
    ======================================="""
    showinfo(title="Hasil", message=pesan)


# frame input
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen
# 1. jenis kelamin label
jenis_kelamin_label = ttk.Label(input_frame, text="Jenis Kelamin:")
jenis_kelamin_label.pack(padx=10, fill="x", expand=True)
# 2. entry jenis kelamin
jenis_kelamin_entry = ttk.Entry(input_frame, textvariable=jenisKelamin)
jenis_kelamin_entry.pack(padx=10, fill="x", expand=True)

# 3. berat badan label
berat_badan_label = ttk.Label(input_frame, text="Berat Badan (KG):")
berat_badan_label.pack(padx=10, fill="x", expand=True)
# 4. entry berat badan
berat_badan_entry = ttk.Entry(input_frame, textvariable=BeratBadan)
berat_badan_entry.pack(padx=10, fill="x", expand=True)

# 5. tinggi badan label
tinggi_badan_label = ttk.Label(input_frame, text="Tinggi Badan (CM):")
tinggi_badan_label.pack(padx=10, fill="x", expand=True)
# 6. entry tinggi badan
tinggi_badan_entry = ttk.Entry(input_frame, textvariable=TinggiBadan)
tinggi_badan_entry.pack(padx=10, fill="x", expand=True)

# 7. usia label
usia_label = ttk.Label(input_frame, text="Usia (Tahun):")
usia_label.pack(padx=10, fill="x", expand=True)
# 8. entry usia
usia_entry = ttk.Entry(input_frame, textvariable=Usia)
usia_entry.pack(padx=10, fill="x", expand=True)

# 9. aktivitas label
aktivitas_label = ttk.Label(input_frame, text="Aktivitas:")
aktivitas_label.pack(padx=10, fill="x", expand=True)
# 10. entry aktivitas
aktivitas_entry = ttk.Entry(input_frame, textvariable=aktivitas)
aktivitas_entry.pack(padx=10, fill="x", expand=True)

# Button 
calculate_button = ttk.Button(input_frame, text="Hitung", command=tombol_click)
calculate_button.pack(fill="x",expand=True,padx=10,pady=10)

window.mainloop()
