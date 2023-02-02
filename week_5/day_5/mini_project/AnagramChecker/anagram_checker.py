from dataclasses import dataclass


class AnagramChecker:
    def __init__(self,fileName):
        self.fileName=fileName
        self.wordText=''
        with open(fileName,"r") as file:
            self.wordText=file.readlines()
        # print(self.wordText)
    
    #method
    def is_valid_word(self,word):
        # print(word)
        with open("text.txt","r") as file:
            

        # for line in self.wordText:
            if word in file.read():
                self.get_anagrams(word)  
            
                return True
            else:
                print("Ce mot n'est pas present")
            
                return False
    #method
    def get_anagrams(self,word):
        list=[]
        self.code_asc=0
        code_ascuii=0
        for i in word:
            self.code_asc=self.code_asc+(ord(i))
        with open("text.txt","r") as file:
            data=file.readline()
            print("Les anagrammes du mot :",word,"sont:")        

            while data!="":

                for c in data:
                    taille=len(data)
                    t=taille-1 
                    # for i in range(0,t-1):
                        # print("code:",c)
                    tab=[]
                    tab.append(c)
                    t=''.join(c)
                    mot=t.lstrip()
                    # print(mot)
                    # c=ord(tab)
                        # while i!=t:
                    for y in mot:
                        code_ascuii=code_ascuii+(ord(y))
                        # break
                if self.code_asc==code_ascuii:
                        # liste=[]
                        # liste.append(mot)
                        print(data,end=" ")    
                # print("taille: ",t)
                # print(code_ascuii,end= " ")
                # print(data,"code:",code_ascuii,end=" ")

                data=file.readline()
                code_ascuii=0

                # break
                

#instanc
anagramme_checker=AnagramChecker("text.txt")
# anagramme_checker.get_anagrams()                
        
        
#instance
