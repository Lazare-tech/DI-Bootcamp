#Set
my_fav_numbers={2,4,8,12}
print(my_fav_numbers)
my_fav_numbers.update([15,20])#ajout plus dun element
print(my_fav_numbers)
my_fav_numbers.remove(20)#last number removed
print(my_fav_numbers)
friend_fav_numbers={67487164}
our_fav_numbers={}
our_fav_numbers=my_fav_numbers|friend_fav_numbers
print(our_fav_numbers)