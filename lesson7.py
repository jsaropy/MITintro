# def is_even(i):
#     """
#     Input: i, a positive int
#     Return True if i is even, otherwise False
#     """
#     if i % 2 == 0:
#         return True
#     else:
#         return False
    
# def is_even_optimized(i):
#     """
#     Input: i, a positive int
#     Return True if i is even, otherwise False.
#     i % 2 == 0 is already a Boolean
#     """
#     return i % 2 == 0

# print(is_even(int(input("Number: "))))
# print(is_even_optimized(int(input("Number: "))))

# def div_by(n, d):
#     """
#     n and d are ints > 0
#     Returns True if d divides n evenly and False otherwise
#     """
#     return n % d == 0

# print(div_by(10, 3))

# for i in range(1,10):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")

def sum_odds(a, b):
    """
    a and b a range
    Returns the sum of odd integers in range a,b
    """
    sum_of_odds = 0

    for i in range(a, b+1):
        if i % 2 == 1:
            sum_of_odds += i

    return sum_of_odds

print(sum_odds(2, 7))