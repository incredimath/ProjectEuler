fib = [1, 2]
while fib[-1] <= 4000000:
    fib.append(
        fib[-2] + fib[-1]
    )
sum = 0
for term in fib:
    if term % 2 == 0:
        sum += term
print(sum)
