'''
Task:

The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
    1. The first line contains the sum of the two numbers
    2. The second line contains the difference of the two numbers (first - second)
    3. The third line contains the product of the two numbers.

------------Example-------------

a = 3
b = 5

Prints:

8
-12
15

Constraints:

1 <= a <= 10^10
1 <= b <= 10^10
'''

a = int(input())
b = int(input())

def arithmetic_ops():

    suma = a + b

    resta = a - b

    producto = a * b

    return(print(f"{suma}\n{resta}\n{producto}"))

if __name__ == '__main__':

    arithmetic_ops()
