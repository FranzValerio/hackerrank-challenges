'''
We know that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand it with an example. You are given an inmutable string, and you want to make changes to it.

Example:

>>> string = "abracadabra"

You can access and index by:

>>> print string[5]
a

What if you would like to assign a value?

>>> string[5] = 'k'
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

How would you approach this?

One solutions is to convert the string to a list and then change the value. Another approach is to slice
the string the string and join it back.

So, the task is that given a string, change the character at a given index and then print the modified string.

You should create a function called mutate_string() that have the following parameters:

- string (str): the string to change
- position (int): the index to insert the character at
- character (str): the character to insert

Returns: the altered string

Input format:

The first line contains a string, the next line contains an integer position, the index location and a string
character, separated by a space.
'''

def mutate_string(string, position, character):

    string_list = list(string)

    string_list[position] = character

    list_to_string = ''.join(map(str, string_list))

    return list_to_string

if __name__ == '__main__':

    s = str(input())

    i, c = input().split()

    s_new = mutate_string(s, int(i), c)

    print(s_new)