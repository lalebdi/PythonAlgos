scores = [98, 99, 94, 88, 70, 79]

print(scores)

scores.append(86)
print(scores)
scores.insert(1, 82)
print(scores)

scores.extend([77, 66])
print(scores)

scores.pop()
print(scores)

scores.remove(99)
print(scores)

# scores.clear()
# print(scores)

scores.sort()
print(scores)

print(scores.count(86))

print(scores.index(88))