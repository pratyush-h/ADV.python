
final_tuple = tuple(x for x in mt if not (isinstance(x, int) and x < 10))
print(final_tuple)