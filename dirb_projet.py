#Bibliothèque : 
import requests 

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
    Cette fonction Vérifie le statut HTTP d'une URL donnée. .
    
    url (chaine de caractère) : l'url donner par l'utilisateur + la partie a tester .

    # Variable requête
            # Les Timeout : enleve le risque de bloqué si le serveur ne répond pas s. 
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
    Cette fonction se comporte comme la commande dirb. Permet la découvrir des répertoires  

    url (chaine de caractère) : l'url donner par l'utilisateur .

    Valeur retournée : le tableau contenant les url positive a notre analyse et leur statut  .
    
    """

    # Initialisation des variable 

    path_wordlist=r".\wordlist_dirb.txt"
    resultats = [] # Création du tableau qui va contenir les resultat sous forme de dictionnaire
    url_test=""

    #Ouverture de la wordlist de dirb

    f = open(path_wordlist,"r",encoding="utf-8")
    ligne=f.readline()
    
    while( ligne!="" ) : 
        
        url_test=url+ligne
        url_test=url_test.strip() # assemblage de l'url avec la partie contenue dans la wordlist
        request = verifier_url(url_test) # appelle de la fonction vérifier_url pour faire notre teste
        print(f"Test en cours : {url_test} ...", end="\r") 
        
        if (request != None ) : 
            if (request==202 or request==403 or request==200) : 
                resultats.append( { "URL" : url_test , "status" : request } )
        ligne=f.readline()
    
    f.close()

    return resultats

# Fonction Principale : 
if __name__ == "__main__":
     

    url=input("Veuillez entrer l'URL pour la commande dirb : ")

    # teste l'intégrité de l'url :
    if ( url[-1] !="/" ) : 
        url=url+"/"
    if ( len(url)==0) :
        print("Erreur vous avez entrer une Url mauvaise ")


    commande = dirb(url)
    i=0
    print("pour L'URL : ",url," \n nous avons : \n")

    while ( i<len(commande) ):
        print(" * : ",commande[i]['URL']," status : ",commande[i]['status'],"\n")
        i=i+1

