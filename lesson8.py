def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0

    return ans

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n
    """
    count = 0

    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(n-sqrt) < epsilon:
            print(i, sqrt)
            count += 1
        else: 
            continue
    
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))