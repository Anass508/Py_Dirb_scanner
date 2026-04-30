#Bibliothèque : 
import requests 
from concurrent.futures import ThreadPoolExecutor

# Affichage graphique : 
#  
print("\n\n")
print(r"""          $$$$$$$\  $$\           $$\              $$$$$$\                                                                  $$\ 
          $$  __$$\ \__|          $$ |            $$  __$$\                                                                 $$ |
          $$ |  $$ |$$\  $$$$$$\  $$$$$$$\        $$ /  \__| $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$ |
          $$ |  $$ |$$ |$$  __$$\ $$  __$$\       $$ |      $$  __$$\ $$  _$$  _$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ $$  __$$ |
          $$ |  $$ |$$ |$$ |  \__|$$ |  $$ |      $$ |      $$ /  $$ |$$ / $$ / $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |
          $$ |  $$ |$$ |$$ |      $$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |
          $$$$$$$  |$$ |$$ |      $$$$$$$  |      \$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |
          \_______/ \__|\__|      \_______/        \______/  \______/ \__| \__| \__|\__| \__| \__| \_______|\__|  \__| \_______| 
                                                                                                                                dev : FATHI Anass """)
print("\n\n\n")

# Fonction : 

def verifier_url(url):
    """
    Cette fonction Vérifie le statut HTTP d'une URL donnée . 
    
    url (chaine de caractère) : l'url donner par l'utilisateur + la partie a tester .

    # Variable requête
            # Les Timeout : enleve le risque de bloqué si le serveur ne répond pas après n second . 
            # User-Agent : Simule un vrai utilisateur, évite le blocage de certaine site .
    
    Valeur retournée : None si erreur sur la requete 
                       ou (int) le status donner en réponse a notre requete
    """

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        reponse = requests.head(url,headers=headers,timeout=3)  
        return reponse.status_code
    
    except requests.exceptions.RequestException: 
        return None


def dirb(url) : 
    """
    Cette fonction se comporte comme la commande dirb. Permet la découvrir des répertoires .  

    url (chaine de caractère) : l'url donner par l'utilisateur .

    Valeur retournée : le tableau contenant les url positive a notre analyse et leur statut  .
    
    """

    # Initialisation des variables 

    path_wordlist=r".\wordlist_dirb.txt"
    resultats = [] # Création du tableau qui va contenir les resultat sous forme de dictionnaire
    url_test=""

    # Ouverture de la wordlist de dirb

    f = open(path_wordlist,"r",encoding="utf-8")
    ligne=f.readline()
    wordlist=[]

    while( ligne!="" ) : # remplissage de la liste 
        
        url_test=url+ligne
        url_test=url_test.strip() # assemblage de l'url avec la partie contenue dans la wordlist
        wordlist.append(url_test)

        ligne=f.readline()
    
    f.close()

    nb_requet = 10 # Tu peux tester 5, 10 ou 20
    with ThreadPoolExecutor(max_workers=nb_requet) as executor: #utiliser pour le multi-threading
        reponses = list(executor.map(verifier_url, wordlist))

        for i in range(len(wordlist)):
            code = reponses[i]
            if code in [200, 202, 403]:
                resultats.append( { "URL" : wordlist[i], "status" : code } )

        return resultats

# Fonction Principale : 
if __name__ == "__main__":
     

    url=input("Veuillez entrer l'URL pour la commande dirb : ")

    # teste l'intégrité de l'url :
    if ( url[-1] !="/" ) : 
        url=url+"/"
    if ( len(url)==0) :
        print("Erreur vous avez entrer une Url mauvaise : (vide) ")


    commande = dirb(url)
    i=0
    print("pour L'URL : ",url," \n nous avons : \n")

    while ( i<len(commande) ):
        print(" * : ",commande[i]['URL']," status : ",commande[i]['status'],"\n")
        i=i+1

