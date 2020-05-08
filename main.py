from equation import Equation

def main():
  #Initialisation des variables
  hypothese = ['A','B','D']
  systeme = [Equation(['A','B'], 'X'), Equation(['C','E','D'], 'F'),Equation(['X','D'], 'Z')]
  
  #Affichage de l'hypothèse initiale
  print('Hypothèse initiale: ' + str(hypothese))
    
  #Pour chaque H de Hypothèses faire
  for h in hypothese: 
    
    #Pour chaque equation E de S faire
    for e in systeme:
      #Si H appartient à premisse de E alors supprimer H de premisse de E fsi
      if h in e.premisse:
        e.premisse.remove(h)

      #Si vide(premisse de E) alors ajouter conclusion de E à Hypothese fsi
      if e.premisse == [] and e.conclusion not in hypothese:
        hypothese.append(e.conclusion)    
  
  #Affichage de l'hypothèse finale
  print('Hypothèse finale:   ' + str(hypothese))

main()