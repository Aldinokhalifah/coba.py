def characterReplacement(s, k):
    window = {}
    left = 0
    max_length = 0
    max_freq = 0

    for right in range(len(s)):
        char = s[right]
        
        # update window
        window[char] = window.get(char, 0) + 1
        
        # update max_freq
        max_freq = max(max_freq, window[char])
        
        # cek invalid
        if (right - left + 1) - max_freq > k:
            # shrink
            window[s[left]] -= 1
            left += 1
        
        # update max_length
        max_length = max(max_length, right - left + 1)
    return max_length

print(characterReplacement("ABCABDE", 1))