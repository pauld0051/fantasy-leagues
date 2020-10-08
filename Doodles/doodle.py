for number in range(0,101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 4 == 0 and number % 6 == 0:
        print("buckfuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 4 == 0:
        print("buck")
    elif number % 5 == 0:
        print("buzz")
    elif number % 6 == 0:
        print("fuzz")
    else:
        print(number)