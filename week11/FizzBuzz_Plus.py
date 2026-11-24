def fizzbuzz_plus(n) -> str:
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        if i % 5 == 0 and i % 7 == 0:
            res.append("BuzzBazz")
        if i % 3 == 0 and i % 7 == 0:
            res.append("FizzBazz")
        if i % 3 == 0:
            res.append("Fizz")
        if i % 5 == 0:
            res.append("Buzz")
        if i % 7 == 0:
            res.append("Bazz")
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            res.append(str(i))
     
    return res


print(fizzbuzz_plus(35))





# if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz")
# elif i % 5 == 0 and i % 7 == 0:
#     print("BuzzBazz")
# elif i % 3 == 0 and i % 7 == 0:
#     print("FizzBazz")
# elif i % 3 == 0:
#     print("Fizz")
# elif i % 5 == 0:
#     print("Buzz")
# elif i % 7 == 0:
#     print("Bazz")
