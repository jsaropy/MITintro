N = int(input("Enter your number: "))
epsilon = 0.01
numbers = 0
low = 0
high = 1000
guess = (high + low) / 2.0

while guess-N:
    if guess < N:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    numbers += 1

print("Count: ", numbers)
print("Answer: ", guess)