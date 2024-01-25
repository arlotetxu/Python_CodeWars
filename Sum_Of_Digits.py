'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''
def sum_digits(n):
    total = 0
    while int(n) > 0:
        total += int(n) % 10
        n //= 10
    print(f"Valor total: {int(total)}")
    if total < 10:
        print(f"Desde dentro: {int(total)}")
        return total
    return sum_digits(int(total))

ret = sum_digits(493193)
print(f"Desde fuera: {ret}")
