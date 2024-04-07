def fizz_buzz (n):
    if n % 3 == 0:
        print('Fizz')
    if n % 5 == 0:
        print('Buzz')
    if n % 3 and 5 == 0:
        print('FizzBuzz')

    


n = 15
print(fizz_buzz(n))