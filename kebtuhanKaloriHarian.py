print("Selamat datang di kalkulator kalori")
jenisKelamin =input("Masukkan jenis kelamin(Laki-laki atau Perempuan):")
BeratBadan = int(input("Masukkan berat badan(KG):"))    
TinggiBadan = int(input("Masukkan tinggi badan(CM):"))
Usia = int(input("Masukkan usia anda:"))
aktivitas = str(input("""Seberapa sering  anda berolahraga
                              -Kurang aktif
                              -Aktif ringan
                              -Cukup aktif
                              -Sangat aktif
                              -Ekstra aktif
                              Masukkan jawaban:"""))

if jenisKelamin == "Laki-laki":
    
    if aktivitas == "Kurang aktif":
        hasil = round((88.4 + 13.4 * BeratBadan) + (4.8 * TinggiBadan) - (5.68 * Usia) * 1.2,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Aktif ringan":
        hasil = round((88.4 + 13.4 * BeratBadan) + (4.8 * TinggiBadan) - (5.68 * Usia) * 1.375,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Cukup aktif":
        hasil = round((88.4 + 13.4 * BeratBadan) + (4.8 * TinggiBadan) - (5.68 * Usia) * 1.55,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Sangat aktif":
        hasil = round((88.4 + 13.4 * BeratBadan) + (4.8 * TinggiBadan) - (5.68 * Usia) * 1.725,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    else:
        hasil = round((88.4 + 13.4 * BeratBadan) + (4.8 * TinggiBadan) - (5.68 * Usia) * 1.9,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
elif jenisKelamin == "Perempuan": 
    if aktivitas == "Kurang aktif":
        hasil = round((447.6 + 9.25 * BeratBadan) + (3.10 * TinggiBadan) - (4.33 * Usia) * 1.2,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Aktif ringan":
        hasil = round((447.6 + 9.25 * BeratBadan) + (3.10 * TinggiBadan) - (4.33 * Usia) * 1.375,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Cukup aktif":
        hasil = round((447.6 + 9.25 * BeratBadan) + (3.10 * TinggiBadan) - (4.33 * Usia) * 1.55,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    elif aktivitas == "Sangat aktif":
        hasil = round((447.6 + 9.25 * BeratBadan) + (3.10 * TinggiBadan) - (4.33 * Usia) * 1.725,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")
    else:
        hasil = round((447.6 + 9.25 * BeratBadan) + (3.10 * TinggiBadan) - (4.33 * Usia) * 1.9,2)
        print(f"""
            Jenis kelamin                      : {jenisKelamin}
            Berat badan                        : {BeratBadan} KG
            Tinggi badan                       : {TinggiBadan} CM
            Usia                               : {Usia} Tahun
            Kebutuhan kalori harian anda adalah: {hasil} kcal""")   
else:
    print("Data yang anda masukkan tidak valid!")