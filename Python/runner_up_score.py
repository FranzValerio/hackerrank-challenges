'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given $n$ scores. Store them in a list and find the socre of the runner-up.

The input format is:

The first line contains $n$. The second line contains an array $A[]$ of $n$ integers, each separated by a space.

The constraints are:

- $2 \leq n\leq 10$
- $-100 \leq A[i] \leq 100$

Sample input:

5
2 3 6 6 5

Sample output:

5
'''

if __name__ == '__main__':
    # The runner-up is the second highest score.

    n = int(input())

    scores = list(map(int, input().split()))

    # convert the scores list to a set to remove duplicates, then convert it back to a list

    unique_scores = sorted(list(set(scores)), reverse=True)

    # the runner-up is then the second element of the sorted list

    runner_up_score = unique_scores[1]

    print(runner_up_score)

