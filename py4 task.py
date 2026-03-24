lst = list(map(int, input().split()))

result = list(map(lambda x: x*x, filter(lambda x: x%2==0, lst)))

print(result)