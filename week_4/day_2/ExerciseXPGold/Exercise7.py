# Instructions

#     Create a list of numbers from one to one million and then use min() and max() 
#     to make sure your list actually starts at one and ends at one million.
#     Use the sum() function to see how quickly Python can add a million numbers.
liste=[]
i=0
sum=0
while i<=1000000:
    liste.append(i)
    i=i+1
for i in range(len(liste)):
    sum=sum+i
print("minimum est {} et maximun {}".format(min(liste),max(liste)))
print("Somme:",sum)