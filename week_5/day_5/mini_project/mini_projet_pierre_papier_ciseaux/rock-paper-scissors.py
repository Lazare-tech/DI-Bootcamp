from ast import While
from telnetlib import GA
from game import Game
class pierre_pa_cis(Game):
    cpt_user=0

    def __init__(self):
        self.cpt_ordi=0
        self.cpt_nul=0
        self.cpt_user=0
        super().__init__()
    #method
    def get_user_menu_choice(self):
        
            # print("\tMenu:")
            # print(" (g) Jouer une nouvelle jeu")
            # print(" (x) Score du jeu")
            # c=input("Choisir:")
            # if c=='g':
            super(pierre_pa_cis,self).get_user_item()
            # elif c=='x':
                # self.print_results(self)
            
                
                
    #method
    def play(self):
        super(pierre_pa_cis,self).get_computer_item()
        # super(pierre_pa_cis,self).get_game_result()
        if self.choix=="r" and self.choix_ordi=="s":
            # self.cpt_user=self.cpt_user+1
            super(pierre_pa_cis,self).get_game_result()
            # print("ssss: ",self.cpt_user)
            print("vous avez choix:",self.choix,"L'ordinateur a choisi:",self.choix_ordi,"_ Resultat:vouz avez gagne!!")
        elif self.choix=="s" and self.choix_ordi=="p":
            super(pierre_pa_cis,self).get_game_result()
            print("vous avez choix:",self.choix,"L'ordinateur a choisi:",self.choix_ordi,"_ Resultat:vouz avez gagne!!!")
        elif self.choix=="r" and self.choix_ordi=="p":
            super(pierre_pa_cis,self).get_game_result()
            print("vous avez choix:",self.choix,"L'ordinateur a choisi:",self.choix_ordi,"_ Resultat:vouz avez perdu!!!")

        elif self.choix=="p" and self.choix_ordi=="s":
            super(pierre_pa_cis,self).get_game_result()
            print("vous avez choix:",self.choix,"L'ordinateur a choisi:",self.choix_ordi,"_ Resultat:vouz avez perdu!!!")
        elif self.choix==self.choix_ordi:
            super(pierre_pa_cis,self).get_game_result()

            print("vous avez choix:",self.choix,"L'ordinateur a choisi:",self.choix_ordi,"_ Resultat:match nul!!!")
     

        # self.print_results(self)
      
        
    #method
    def print_results(self,results={}):
        # super(pierre_pa_cis,self).get_game_result()
        # results={}
        results["gagne"]=self.cpt_user
        results["perdu"]=self.cpt_ordi
        results["nul"]=self.cpt_nul
        print(results)
        print("\tResultat du jeu")
        print("\tVous avez gagner",results["gagne"],"fois")
        print("\tVous avez perdu",results["perdu"],"fois")
        print("\tMatch null ",results["nul"],"fois")
    #method

                
        
#instanc
def main():
    p=pierre_pa_cis()
    while True:
        print("\tMenu:")
        print(" (g) Jouer une nouvelle jeu")
        print(" (x) Score du jeu")
        c=input("Choisir:")
        if c=='g':
            p.get_user_menu_choice()
            p.play()    
        else:
            p.print_results()
            break            

                        
# for i in range(4):                
main() 