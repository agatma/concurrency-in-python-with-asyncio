def positive_integers(until: int):
    yield from range(until)


positive_iterator = positive_integers(2)

print(next(positive_iterator))
print(next(positive_iterator))
