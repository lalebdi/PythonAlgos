scores = {98, 99, 94, 88, 70, 79}

print(scores)

scores.add(93)
scores.add(82)
print(scores)

scores.discard(88)
scores.discard(98)
print(scores)

attendance = set([1, 2, 3, 4, 5, 99])

print(attendance)

print(scores | attendance) # Union

print(scores & attendance) # Intersection


print(scores <= attendance) # compare
