''''
Task:

The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

Example:

n = 3

Prints:
0
1
4
'''

n = int(input())

def main():

    for i in range(0,n):

        sq = i**2

        print(sq)

if __name__ == '__main__':

    main()