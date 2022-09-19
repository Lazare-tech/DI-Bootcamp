# When will I retire ?
# Instructions

# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

#     Create a function get_age(year, month, day)
#     Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
#     After calculating the age of a person, the function should return the age (the age is an integer).
#     Create a function can_retire(gender, date_of_birth).
#     It should call the get_age function (with what arguments?) in order to receive an age.
#     Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
#     Calculate. You may need to do a little more hard-coding here.
#     Return True if the person can retire, and False if he/she can’t.

# Some Hints

#     Ask for the user’s gender as “m” or “f”.
#     Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
#     Call can_retire to get a definite value for whether the person can or can’t retire.
#     Display a message informing the user whether they can retire or not.
#     As always, test your code to ensure it works.
def get_age(year,month,day):
    age=2022-year
    day=day
    if(age>=67 and month>4):
        return 'true'
    else:
        return 'false'

def can_retire(gender, date_of_birth):
    date_birth=date_of_birth.split("/")
    d=int(date_birth[2])
    m=int(date_birth[1])
    y=int(date_birth[0])
    retraite=get_age(y,m,d)
    return retraite
    
    
date_birth=[]
gender=input("Entrer votre genre m->pour masculin f->pour feminin:")
date=input("Date de naissane sous forme yyyy/mm/dd:")
retraite=can_retire(gender,date)
print(retraite)

    
    