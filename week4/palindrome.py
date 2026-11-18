def palindrome(text):
    text = text.lower()
    clean_text = "".join(text.split())
    text = []
    for char in clean_text:
        if not char.isalnum():
            continue
        text.append(char)

    print(text)

    l = 0
    r = len(text) - 1
    
    while l < r:
        if text[l] == text[r]:
            res = True   
        else:
            res = False
        l += 1
        r -= 1

    return res 
    
    # a = 1
    # for i in list:
    #     if list[a-1] == list[-a]:
    #         return True
    #         a += 1
    #     return False

print(palindrome("Was it a car or a cat I saw?"))