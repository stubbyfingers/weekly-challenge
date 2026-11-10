def palindrome(text):
    text = text.lower()
    clean_text = "".join(text.split())
    list = []
    for char in clean_text:
        list.append(char)

    a = 1
    for i in list:
        if list[a-1] == list[-a]:
            return True
            a += 1
        return False

print(palindrome("race    car"))