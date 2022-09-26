# 🌟 Exercice 2 : Travailler Avec JSON
# Des Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Accédez à la clé "salaire" imbriquée à partir de la chaîne JSON ci-dessus.
# Ajoutez une clé appelée "birth_date" à la chaîne JSON au même niveau que la clé "name".
# Enregistrez le dictionnaire au format JSON dans un fichier.
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
js=json.loads(sampleJson)
print("Salaire: {}".format(js["company"]["employee"]["payable"]["salary"]))
js["company"]["employee"]["birth_date"]="2022/02/15"
print(js["company"]["employee"])
file_json="my_sample.json"
with open(file_json,"w") as file:
    json.dump(js,file,indent=2)