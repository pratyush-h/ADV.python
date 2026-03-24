lst = list(map(int, input().split()))

# Remove duplicates
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)

# Bubble sort
for i in range(len(unique)):
    for j in range(len(unique)-1):
        if unique[j] > unique[j+1]:
            unique[j], unique[j+1] = unique[j+1], unique[j]

print(unique)