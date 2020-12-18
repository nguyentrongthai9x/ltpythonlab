def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True
import timeit
list_number = [1, 3, 4, 8, 11, 33, 77, 84, 100, 120]
total_time = 0
for number in list_number:
    start = timeit.default_timer()
    result = is_prime_basic(number)
    stop = timeit.default_timer()
    result = is_prime_basic(number)
    print("{} is a prime number: {}.".format(number, result))
    total_time += stop - start

print("Elapsed time: {}(second)".format(total_time))
