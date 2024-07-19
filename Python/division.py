'''
Task:

Provided code stub reads two integers, a and b from STDIN

Add logic to print two lines. The first line should contain the result of the integer division, a//b.
The second line should contain the result of float division, a/b.

No rounding or formatting is necessary.

------- Example --------

a = 3
b = 5

Print:
0
0.6
'''

a = int(input())
b = int(input())

def division():

    entera = a//b

    flotante = a/b

    return (print(f"{entera}\n{flotante}"))

if __name__ == '__main__':

    division()