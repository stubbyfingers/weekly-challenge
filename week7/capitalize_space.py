sentence = input("Give me a sentence: ")
def capitalize(sentence) -> str:
    to_list = sentence.split()
    #print(to_list)

    new_list = []
    for char in to_list:
        if not char[0] >= "A" or not char[0] <= "Z":
            convert = ord(char[0]) - 32
            result = chr(convert)
        
        new_word = char.replace(char[0], result)
        new_list.append(new_word)
    #print(new_list)

    capitalize = " ".join(new_list)
    print(f"Capitalized: {capitalize}")

    no_spaces = "".join(new_list)
    print(f"No Spaces: {no_spaces}")



capitalize(sentence)