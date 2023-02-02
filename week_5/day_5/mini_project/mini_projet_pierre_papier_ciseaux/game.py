import random
import string
class Game:
    def __init__(self):
        self.choix=''
        self.choix_ordi=''
        self.cpt_user=0
        self.cpt_ordi=0
        self.cpt_nul=0
        pass
    #method
    def get_user_item(self):
        self.choix=input("Choisir (r)rock (p)aper ou (s)cissors:")
    #method
    def get_computer_item(self):
        liste=["r","p","s"]
        str=liste 
        self.choix_ordi=''.join(random.choice(str))
    #method
    def get_game_result(self, user_item='', computer_item=''):
    
        user_item=self.choix
        computer_item=self.choix_ordi
        # print(computer_item)
        if user_item=="r" and computer_item=="s":
            self.cpt_user=self.cpt_user+1
            # print("ssss: ",self.cpt_user)

        elif user_item=="s" and computer_item=="p":
            self.cpt_user=self.cpt_user+1
        elif user_item=="r" and computer_item=="p":
            self.cpt_ordi =self.cpt_ordi+1
        elif user_item=="p" and computer_item=="s":
            self.cpt_ordi =self.cpt_ordi+1
        elif user_item==computer_item:
            self.cpt_nul =self.cpt_nul+1
        # print("total: ",self.cpt_user)    
        
#instance
game=Game()
game.get_computer_item()   
game.get_game_result()             
        