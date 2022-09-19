# Count occurence

# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0

s=input("String:")
ch=input("Character:")
n=0
for i in range(len(s)):
    if s[i]==ch:
        n=n+1
print(n)