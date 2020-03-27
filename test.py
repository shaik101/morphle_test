from itertools import combinations


s = "shaik"
length = len(s)
for j in  ( combinations(s, (length+1)-i) for i in range(1, length+1) ):
    print(set(j))