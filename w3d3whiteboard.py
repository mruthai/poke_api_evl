# The Hamming Distance is a measure of similarity between two strings of equal length. 
# Complete the function so that it returns the number of positions where the input strings do not match.
# Examples:

# a = "I like turtles"
# b = "I like turkeys"
# Result: 3

# a = "Hello World"
# b = "Hello World"
# Result: 0

# a = "espresso"
# b = "Expresso"
# Result: 2

def num_of_not_same(string1, string2):
    not_same = 0
    for i in range(len(string1)):
        if string2[i] != string1[i]:
            not_same += 1
        else:
            continue
    return not_same