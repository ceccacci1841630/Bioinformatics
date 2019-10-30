def fib(n):
    """Returns the n-th Fibonacci number."""
    prev = 1
    curr = 0
    for i in range(n):
        p = curr
        curr = curr + prev
        prev = p
    return curr
print(fib(20))

