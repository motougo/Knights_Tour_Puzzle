def multiply(a, b):
    # base case
    if b == 1:
        return a
    else:
    # recursive case
        return a + multiply(a, b-1)

