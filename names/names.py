import time
from binaryTree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

rootNode = BSTNode(names_1[0])
for name in names_1:
    rootNode.insert(name)
for name2 in names_2:
    if rootNode.contains(name2):
        duplicates.append(name2)

# old code runtime complexity O(n^2)
# solution code O(log n)

# time on my machine using binary tree: 0.15233612060546875 seconds (can be faster depending on machine)

# stretch using sets - crazy efficient: 0.005126953125 seconds
# duplicates = list((set(names_1) & set(names_2)))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
