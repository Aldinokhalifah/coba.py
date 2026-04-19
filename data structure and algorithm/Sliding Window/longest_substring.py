def findLongestSubstring(str, k) :
    window_start = 0
    max_length = 0
    char_frequency = {}
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        # 1. Masukkan karakter ke Map (hitung frekuensinya)
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # 2. CIUTKAN jendela jika karakter unik > k
        while len(char_frequency) > k:
            left_char = str[window_start]
            # Kurangi frekuensi karakter kiri di Map
            char_frequency[left_char] -= 1
            
            # Jika frekuensi jadi 0, hapus dari Map agar len(char_frequency) berkurang
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            # Geser window_start
            window_start += 1

        # 3. Catat panjang maksimal jendela yang valid
        current_window_size = window_end - window_start + 1
        max_length = max(max_length, current_window_size)

    return max_length

print(findLongestSubstring("araaci", 2))