# Problem: 5
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def lcm(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = abs(result * number) // math.gcd(result, number)
    
    return result

print(lcm(range(1, 21)))