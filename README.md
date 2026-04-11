# 🚀 PyDirb Scanner

**PyDirb** est un outil pédagogique en Python conçu pour l'énumération de répertoires et fichiers cachés sur un serveur web (implémentation simplifiée de la commande `dirb`).

Ce projet a été développé dans le cadre de mon apprentissage en cybersécurité pour mieux comprendre le fonctionnement des requêtes HTTP et le principe du "fuzzing" d'URL.

> ⚠️ **Avertissement :** Cet outil est destiné **exclusivement** à des fins éducatives et de tests d'intrusion sur des systèmes dont vous avez l'autorisation explicite. L'utilisation de cet outil contre des serveurs sans autorisation est illégale.

## 📋 Fonctionnalités
* **Scan HTTP** : Envoie des requêtes `HEAD` pour vérifier l'existence de ressources.
* **Respect du serveur** : Utilisation d'un `timeout` pour éviter de surcharger les cibles.
* **Simulation d'utilisateur** : Ajout d'un `User-Agent` pour simuler une navigation réelle.
* **Affichage en temps réel** : Suivi du scan directement dans la console.

## 🛠️ Installation & Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/ton-utilisateur/pydirb-scanner.git](https://github.com/ton-utilisateur/pydirb-scanner.git)
   cd pydirb-scanner
