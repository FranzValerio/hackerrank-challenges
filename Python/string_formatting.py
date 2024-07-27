'''
Given an integer n, print the following values for each integer i from 1 to n:

- Decimal
- Octal
- Hexadecimal (capitalized)
- Binary

The function should be called print_formatted() with the following parameters:

    -number (int): the maximum value to print

The four values must be printed on a single line in the order specified above for each i from 1 to number.
Each value should be space-padded to match the width of the binary value of number and the values should be
separated by a single space.


'''

def print_formatted(number):

    # First, need to get the width for formatting

    width = len(bin(number)) - 2 # Using 'bin(number)' gives a '0b...' prefix, so substract 2 to get the actual length

    for i in range(1, number + 1):

        # Decimal

        dec = str(i).rjust(width)

        # Octal

        octal = oct(i)[2:].rjust(width) # 'oct(i)' gives a '0o...' prefix, so we need to remove it with [2:]

        # Hexadecimal

        hexa = hex(i)[2:].upper().rjust(width) # Same thing, removing prefix and capitalize

        # Binary

        binary = bin(i)[2:].rjust(width) # Remove prefix and adjust it

        print(f"{dec} {octal} {hexa} {binary}")


if __name__ == '__main__':

    n = int(input())

    print_formatted(n)