# Projet RCAA – Reconnaissance de Scripts

## Objectif
Implémenter un système de reconnaissance de scénarios basé sur la théorie des scripts
en Représentation des Connaissances et Apprentissage Automatique (RCAA).

Le système permet d’identifier un scénario (restaurant, supermarché, hôpital, université, etc.)
à partir d’une séquence d’actions observées.

## Principe
- Chaque scénario est représenté sous forme de script : acteurs, contexte, séquence d’actions.  
- Les actions observées sont comparées aux scripts connus.  
- Le scénario dont les actions correspondent le mieux est reconnu, avec un score de confiance.

## Fonctionnalités
- Gestion de l’ordre des actions  
- Tolérance aux actions manquantes  
- Seuil de reconnaissance configurable  
- Détection de scénarios inconnus  
- Interaction utilisateur en boucle : tester plusieurs séquences sans relancer le programme  
- Affichage de l’ID et du scénario reconnu

## Technologies
- Python 3.x  
- CSV pour le dataset  
- Standard library (csv, input/output)

## Fichiers du projet
- `dataset.csv` : contient les scripts avec ID, scénario, acteurs, contexte et actions  
- `scripts.py` : contient la classe Script et les fonctions de chargement et reconnaissance  
- `main.py` : programme principal pour tester le système de reconnaissance

## Utilisation
1. Lancer le programme :  
python main.py
