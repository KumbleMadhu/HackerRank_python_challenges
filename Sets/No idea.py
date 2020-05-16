# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()  # integers n and m separated by a space.
arr = input()  # n integers, the elements of array
A = set(input().split())  # m integers in set A
B = set(input().split())  # m integers in set B
print(sum([(i in A) - (i in B) for i in arr]))
