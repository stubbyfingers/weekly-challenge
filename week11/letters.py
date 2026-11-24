def count_letters(text):
    vowel_count = 0
    consonant_count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in text:
        char = char.lower()
        if char in vowels:
            vowel_count += 1
    
        
        if (char >= 'a' and  char <= 'z') and not char in vowels:
            consonant_count += 1
        

        
    return vowel_count,consonant_count

print(count_letters("Hello, World 123"))
