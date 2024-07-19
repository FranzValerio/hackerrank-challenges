'''
Given the names and grades for each student in a class of N students, store them in a nested list and print
the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print
each name on a new line.

Example:

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that
score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:

alpha
beta

Input format:

The first line contains an integer N, the number of students.
The 2N subsequent lines describe each student over 2 lines:
    - The first line contains a student's name
    - The second line contains their grade

Constraints:

- 2 <= N <= 5
- There will always be one or more students having the second lowest grade.

Sample Input:

5
Harry
37.12
Berry
37.12
Tina
37.2
Amir
41
Harsh
39

Sample output:

Berry
Harry
'''

if __name__ == '__main__':

    records = []

    for n in range(int(input())):

        name = str(input())

        score = float(input())

        records.append([name, score])

    # Extract all the scores using list comprehension

    scores = [record[1] for record in records]

    # Find the unique scores

    unique_scores = sorted(set(scores))

    # Find the second lowest score

    second_lowest_score = unique_scores[1]

    # Now find all the students with the second lowest score

    second_lowest_students = [record[0] for record in records if record[1] == second_lowest_score]

    # Sort the students' names alphabetically

    second_lowest_students.sort()

    for students in second_lowest_students:

        print(students)


    



