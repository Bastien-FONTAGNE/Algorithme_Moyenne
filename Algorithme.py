Total = 0  #Initialisation de la variable "Total"

for i in range(31): #Répétez 31 fois
    
    temperature = float(input("Veuillez entrer une température: ")) #demande de rentrer la température à l'utilisateur
                        
    Total = Total + temperature #Ajoute la temperature à la variable totale

    Moyenne = Total/31 #Calcule la moyenne

print(f"La moyenne des températures est de {Moyenne}") #Affiche la moyenne 
