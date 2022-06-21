import math

# ex 1
def highest(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(highest(1,2))

# ex 2
def average(list):
    total_average = 0
    for number in list:
        total_average += number
    return (total_average / len(list))

print(average([4, 2]))

# ex 3
def print_square(n):
        times_to_print = 0
        while times_to_print < n:
            times_to_print += 1
            print(n * '*')

print(print_square(4))

# ex 4
def longest_name(names):
    longest_name = ''
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name

print(longest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))

# ex 5
# 1l / 3m2
# 18l - r$ 80,00
# cada lata pinta 54m2
# cada m2 = 54 / 80 = 0,68 / m2
def needed_ink(area):
    return (math.ceil(area / (18 * 3)), math.ceil(area /(18 * 3)) * 80)

print(needed_ink(200))

# ex 6
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.
def type_of_triangle(side1, side2, side3):
    is_triangle = (
            side1 + side2 > side3 and
            side2 + side3 > side1 and
            side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"

# bonus 1
def lowest_value(list):
    return min(list)

print(lowest_value([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))

# bonus 2
def print_triangle(n):
    size_unit = 1
    while size_unit <= n:
        print(size_unit * '*')
        size_unit += 1

print_triangle(5)

# bonus 3
def total_sum(n):
    total = 0
    for number in range(n + 1):
        total += number
    return total

print(total_sum(5))
