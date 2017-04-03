# original: my_run.py
# improved using
# https://www.hackerrank.com/rest/contests/master/challenges/array-left-rotation/hackers/thunderb_/download_solution
# https://www.hackerrank.com/rest/contests/master/challenges/array-left-rotation/hackers/Norman99/download_solution

def left_rotation(arr_in, d):
    n = len(arr_in)
    return arr_in[d%n:] + arr_in[:d%n]

d = int(input().split()[1])
arr_in = list(map(int, input().split()))

arr_rot = left_rotation(arr_in, d)

print(*arr_rot)

