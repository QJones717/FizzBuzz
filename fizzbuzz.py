def fizzbuzz (s, f):

    for i in range(s, f):
 
        if i % 15 == 0:
            print("FizzBuzz")
            continue

        elif i % 3 == 0:
            print("Fizz")
            continue

        elif i % 5 == 0:
            print("Buzz")
            continue

        print(i)

fizzbuzz(1, 101)
