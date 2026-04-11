#  Py_Dirb_scanner

**Py_Dirb_scanner** est un outil pédagogique en Python conçu pour l'énumération de répertoires et fichiers cachés sur un serveur web (implémentation simplifiée de la commande `dirb`).

Ce projet a été développé dans le cadre de mon apprentissage en cybersécurité pour mieux comprendre le fonctionnement des requêtes HTTP et le principe du "fuzzing" d'URL.

> ⚠️ **Avertissement :** Cet outil est destiné **exclusivement** à des fins éducatives et de tests d'intrusion sur des systèmes dont vous avez l'autorisation explicite. L'utilisation de cet outil contre des serveurs sans autorisation est illégale.

## Fonctionnalités
* **Scan HTTP** : Envoie des requêtes `HEAD` pour vérifier l'existence de ressources.
* **Respect du serveur** : Utilisation d'un `timeout` pour éviter de surcharger les cibles.
* **Simulation d'utilisateur** : Ajout d'un `User-Agent` pour simuler une navigation réelle.
* **Affichage en temps réel** : Suivi du scan directement dans la console.

## Installation & Utilisation : 

1. **Prérequis :**
   Assurez-vous d'avoir Python installé. Ce script utilise la bibliothèque `requests` :
   ```bash
   pip install requests

Pour que le script puisse fonctionner correctement, il a besoin d'une liste de mots (wordlist) pour effectuer ses tests :

1. Assurez-vous d'avoir un fichier nommé `wordlist_dirb.txt` situé à la racine du dossier de votre projet.
2. Ce fichier doit contenir une liste de répertoires ou de fichiers, un par ligne.

##  Lancement
Une fois les prérequis installés et le fichier `wordlist_dirb.txt` en place, lancez le script via votre terminal 

