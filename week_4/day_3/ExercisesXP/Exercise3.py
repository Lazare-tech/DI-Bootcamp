# ara
# Instructions

#     Here is some information about a brand.

#     name: Zara 
#     creation_date: 1975 
#     creator_name: Amancio Ortega Gaona 
#     type_of_clothes: men, women, children, home 
#     international_competitors: Gap, H&M, Benetton 
#     number_stores: 7000 
#     major_color: 
#         France: blue, 
#         Spain: red, 
#         US: pink, green



#     2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#     3. Change the number of stores to 2.
#     4. Print a sentence that explains who Zaras clients are.
#     5. Add a key called country_creation with a value of Spain.
#     6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
#     7. Delete the information about the date of creation.
#     8. Print the last international competitor.
#     9. Print the major clothes colors in the US.
#     10. Print the amount of key value pairs (ie. length of the dictionary).
#     11. Print the keys of the dictionary.
#     12. Create another dictionary called more_on_zara with the following details:

#     creation_date: 1975 
#     number_stores: 10 000



#     13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
#     14. Print the value of the key number_stores. What just happened ?
import copy
brand =dict()
brand={'name':'zara',
      'creation_date':1975,
      'creator_name':'Amancino Ortega Gaona',
      'type_of_clothes':['men','women','children','home'],
      'international_competitors':['Gap','H&M','Benetton'],
      'numbers_stores':7000,
      'major_color':
          {
              'France':'blue',
              'Spain':'red',
              'Us':('pink','green')
          },
      }
print(brand)
print(".............................................................................")
print(".............................................................................")

brand['numbers_stores']=2
print(brand)
print(".............................................................................")
print(".............................................................................")

print("Les clients de zara sont les",brand['type_of_clothes'][0],"les ",brand['type_of_clothes'][1],"et les",brand['type_of_clothes'][2])
brand["country_creation"]="Spain"
print("..............Ajout dune nouvelle cle. country_creation.....................")
print(".............................................................................")
print(brand)
if('international_competitors' in brand.keys()):
    brand['international_competitors'][2]='Desigual'
print("")
print("..............Ajout dune nouvelle valeur dans international_compettors.....")
print(".............................................................................")
print(brand)
print("")
print("..............Supression de creation date...................................")
print("...........................................................................")
del brand['creation_date']    
print(brand)
print("")
print("The last international competitors",brand['international_competitors'][2])
print("Major colors in US:",brand['major_color']['Us'])
print("longeur du dictionnaire:",len(brand))
print("Cle du dictionnaire:")
for cle in brand.keys():
    print(cle)
    
more_on_zara={'creation_date': 1975,
                'number_stores': 10000,
            }
print("")
print("..............copie du dictionnaire more_on_zara dans brand.........")
print("....................................................................")
brand=dict(more_on_zara)
print(brand)
 