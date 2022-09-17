#Check the index
# Instructions
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

# Example: if input is 'Cortana' we should be printing the index 1
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input("Entrer votre nom:")
for i in range(len(names)):
    if(name==names[i]):
        print(name)
        break