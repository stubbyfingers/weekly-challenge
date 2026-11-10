def word_frequency(text):
    text = text.lower().split()
    a = 0
    count = 0
    for i in text:
        if not i.isalnum():
            continue
        if text[a] == i:
            count += 1
        
    print(f"{text[a]} : {count}")

       
        

word_frequency("This is a , sentence this python python")