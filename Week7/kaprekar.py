
def isKap(n):
    if n<10:
        return False

    squared_str = str(n*n)

    for i in range(1, len(squared_str)):
        part_1 = squared_str[:i]
        part_2 = squared_str[i:]

        partition_sum = int(part_1) + int(part_2)
        if partition_sum == n:
            return True

    return False




x = int(input("Enter a top limit (inclusive): "))
print("\nThe list of all Kaprikar numbers from 10 to",x,"is:")
for i in range(10, x+1):

    if isKap(i):
        print(i, end=" ")

