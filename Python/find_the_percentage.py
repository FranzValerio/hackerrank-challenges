'''
You have a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example:

marks key:value pairs are:

'alpha':[20,30,40]
'beta':[30,50,70]

query_name = 'beta'

The query_name is 'beta', so beta's average score is (30+50+70)/3 = 50.0

Input format:

The first line contains the integer n, the number of students' records. The next n lines contains the names
and marks obtained by a student, each value separated by a space. The final line contains query_name, the name
of a student to query.

Constraints:

- 2 <= n <= 10
- 0 <= marks[i] <= 100
- length of marks arrays = 3

Output format:

Print one line: the average of the marks obtained by the particular student correct to 2 decimal places.

Sample input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample output:

56.00
'''

if __name__ == '__main__':

    n = int(input())

    students_marks = {}

    for i in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        students_marks[name] = scores
    
    query_name = input()

    query_marks = students_marks.get(query_name)

    average_query = sum(query_marks) / len(query_marks)

    print(format(average_query, ".2f"))

