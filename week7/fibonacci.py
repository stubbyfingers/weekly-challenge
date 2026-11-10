def fibonacci(N): 
    sequence = [0, 1]
    a = 0
    for i in range(N - 2):
        result = sequence[a] + sequence[a + 1]
        sequence.append(result)
        a = a + 1

    print(f"Sequence: {sequence}")

    even = []
    sum = 0
    for i in sequence:
        if i%2 == 0:
            even.append(i)
            sum = sum + i
    # print(even)
    print(f"Even Sum: {sum}")

    reverse = []
    for i in sequence:
        reverse.insert(0, i)
    print(f"Reversed: {reverse}")
    


fibonacci(8)