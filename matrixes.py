size = int(input())

array_input = []

for x in range(size):
    array_input.append([int(y) for y in input().split()])

print(array_input)


for i in array_input:
    for j in i:
        print(j, end=" ")
    print()


