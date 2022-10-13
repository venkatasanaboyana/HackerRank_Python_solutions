# List Comprehensions

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print ans

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores.
#Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
sorted_list = sorted(list(arr), reverse = True)
for order in range(len(sorted_list)):
    rank1 = sorted_list[0]
    if sorted_list[order] != rank1:
        print(sorted_list[order])
        break
