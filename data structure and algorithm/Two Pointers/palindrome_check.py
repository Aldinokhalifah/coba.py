def check_palindrome(kalimat) :
    clean = kalimat.lower()

    left = 0
    right = len(clean) - 1

    while left < right:
        if clean[left] != clean[right] :
            return False

        left += 1
        right -= 1
    return True

print(check_palindrome("kasur ini rusak"))