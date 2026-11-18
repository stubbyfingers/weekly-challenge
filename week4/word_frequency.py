# def word_frequency(text):
def count_words(words: list[str]) -> dict[str, int]:
    words = words.lower().split()
    print(words)
    
    dictionary = {}
    
    for word in words:
        if not word.isalnum():
            continue
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print(dictionary)
        # key_value = f"{char} = {count}"
        # dictionary.update(key_value)

    

    
        





# def most_frequent(freq: dict[str, int]) -> str









print(count_words("This is a , sentence this python python"))
    # l = 0
    # r = 1
    # count = 0
    # while l != r:
    #     if not text[l].isalnum():
    #         continue
    #     if text[l] == text[r]:
    #         count += 1    
    #     r += 1
        
    # print(f"{text[a]} : {count}")

       
        

