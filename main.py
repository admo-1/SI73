def main():
  #Initialisation des variables
  hypothese = ['A','B','D']
  premisse = [['A','B'], ['C','E','D'], ['X','D']]
  conclusion = [['X'],['F'],['Z']]
  print('hypothese initiale: ' + str(hypothese))
  print('premisse initiale: ' + str(premisse) + '\n')
  #Pour chaque H de Hypothèses faire
  for h in hypothese:
    
    #Pour chaque equation E de S faire
    for index, e in enumerate(premisse):
      #print("Premisse : " + str(e))
      #print("Caractère à chercher : " + str(h))
      #Si H appartient à premisse de E alors supprimer H de premisse de E fsi
      if h in e:
        e.remove(h)
        #print('Supprimé :' + str(h))

      #Si vide(premisse de E) alors ajouter conclusion de E à Hypothese fsi
      if e == [] and conclusion[index][0] not in hypothese:
        
        hypothese.append(conclusion[index][0])
        #print('Valeur ajoutée dans hypothèse : ' + str(conclusion[index]))
      
      #print('\n')
  
  print('hypothese finale: ' + str(hypothese))
  print('premisse finale: ' + str(premisse))

main()