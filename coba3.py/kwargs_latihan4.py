def konfigurasi_pengaturan(**pengaturan_baru):
    pengaturan = {
        'mode': 'default',
        'volume': 50,
        'kecerahan': 70
    }
    pengaturan.update(pengaturan_baru)
    return pengaturan

hasil = konfigurasi_pengaturan(mode='malam', volume=30)
print(f'Pengaturan terbaru: {hasil}')
