'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
specifications:

- Mat size must be N X M. (N is an odd natural number, and M is 3 times N).
- The design should have "WELCOME" written in the center.
- The design pattern should only use | . and _ characters.

Sample designs:

Size 9x27

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------


Input format:

A single line containing the space separated values of N and M.

Constraints:

- 5 < N < 101
- 15 < M < 303
'''

N, M = map(int, input().split())

for i in range(1, N, 2):

    print((i * ".|.").center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N-2, -1, -2):

    print((i * ".|.").center(M, "-"))