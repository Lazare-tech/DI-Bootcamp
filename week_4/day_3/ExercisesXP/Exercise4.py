# : Disney characters
# Instructions

# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


#     Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#     Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
#     Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#     Only recreate the 1st result for:
#         The characters, which names contain the letter “i”.
#         The characters, which names start with the letter “m” or “p”.


users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
num=[]
disney_users_A={}
disney_users_B={}
for i in range(5):
    num.append(i)
disney_users_A=dict(zip(users,num))
print(disney_users_A)
disney_users_B=dict(zip(num,users))
print(disney_users_B)
users.sort()
disney_users_C=dict(zip(users,num))
print(disney_users_C)
name=[]
print("List with the characters, which names contain the letter “i”.")
for i in range(4):
    if 'i' in users[i]:
        name.append(users[i])
disney_users_A=dict(zip(name,num))
print(disney_users_A)
print("Liste with the characters, which names start with the letter “m” or “p”.")
namE=[]
for i in range(4):
    noM=users[i]
    c=noM[0]
    if c=='m' or c=='p':
        namE.append(noM)
    else:
        print("No characters with names start with the letter m or p")
        break
disney_users_A=dict(zip(namE,num))
print(disney_users_A)
