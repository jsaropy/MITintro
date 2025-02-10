def char_counts(s):
    """
    s is a string of lowercase chars
    Returns a tuple where the first value is the
    number of vowels in s and the second value is
    the numnber of consonants in s 
    """
    vowels = 'aeoui'
    (v,c) = (0,0)
    for i in s:
        if i in vowels:
            v += 1
        else:
            c += 1
    return (v,c)   

print(char_counts("abcd"))
print(char_counts("zcght"))

# variable number of arguments
def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3,4,5,6)) # parentheses around values because its a tuple
print(mean(6,0,9))  

# Finger Excercise L9
def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    pairwise_product = 0
    for i in range(len(tA)):
        pairwise_product += tA[i] * tB[i]
            
    return (len(tA), pairwise_product)

tA = (1, 2, 3)
tB = (4, 5, 6) 
print(dot_product(tA, tB))