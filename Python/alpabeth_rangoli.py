'''
You are given an integer N. Your task is to print an alphabet rangoli of size N. 
A rangoli is a form of Indian folk art based on creation of patterns.

For example, different sizes of alphabet rangoli are shown below:

Size = 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

Size = 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Note that the center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter
(in alphabetical order).

You should create a function named print_rangoli() with the following parameters:

- size (int): the size of the rangoli

Returns:

-string: a single string made up of each of the lines of the rangoli separated by a newline character
'''

def print_rangoli(size):

    '''
    Since we need to have the nth letter in the alphabet, we can use the chr() method to obtain them.

    chr(number) gets the character that represents the specified unicode value.

    Since a its unicode = 97, we can use it to generate the needed alphabet letters.


    '''

    unicode = 96 # One before

    characters = []

    for i in range(1, size + 1):

        get_character = chr(unicode + i)

        characters.append(get_character)

    '''
    Now, we can note that the rangoli has a symmetric pattern with the middle line containing all the
    characters from 'a' to the 'N'th alphabet.
    The lines above and below are symmetric around this middle line.
    And each line is centered with '-' characters.

    Notice that for the 1st line in a ragnoli size 3, the character 'c' is the 3rd character from 'a'

    Also, the pattern in the 2nd line in the rangoli size 3 is 'c-b-a-b-c', which is constructed using 
    characters from 'a' to the 3rd character, separated by '-' and then back to 'a'.

    Now, we need to now the width of the rangoli. Let's break down how we could calculate it:

    1. Each character in the rangoli is separated by a '-'.
    2. For N characters, there are N-1 dashes between them. For example: N = 3, the middle line is
    'c-b-a-b-c', there is 5 characters and 4 dashes.
    3. The total number of characters in the middle line is 5, that's 2*N - 1 (includes characters from
    'a' to 'N' and back to 'a'). 
    4. The total number of dashes between the characters is 2*(N-1) 
    5. The width of the middle line is then: 
        number of characters + number of dashes = 2*N - 1 + 2*(N-1) = 4*N - 3
    6. So the width is: 4*N - 3

    We can start drawing the easiest one, the middle line. Once we have the needed characters, we can
    combine them in reverse order. Also, remember we need to separate them with '-'
    '''

    width = 4 * size - 3

    # Create a list that will store the lines

    lines = []

    '''
    Now, we can loop to create each line.

    Remember that we're gonna start the rangoli with the Nth alphabet letter. 
    So we need to slice the characters list in reverse order, starting from the n-1 index, down to i+1.

    Inside the loop, the slice would look like: characters[size-1:i:-1]

    If  size = 5, and i = 0, then: ['e','d','c','b']
    If i = 1, then: ['e', 'd', 'c']

    Also, we need to get the characters in order, we can achieve it with: characters[i:size]

    We also will join them with the dashes in between.

    Finally, we can use the center() string method, that will center the string within a width padding
    with '-'.
    '''

    for i in range(size):

        s = '-'.join(characters[size-1:i:-1] + characters[i:size])

        lines.append(s.center(width,'-'))

    print('\n'.join(lines[::-1] + lines[1::]))

n = int(input())

print_rangoli(n)
