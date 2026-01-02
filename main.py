from scripts import charger_scripts, reconnaitre_scenario

def main():
    print("===== SYSTEME RCAA : RECONNAISSANCE DE SCRIPTS =====\n")

    scripts = charger_scripts("dataset.csv")

    print("Entrez les actions observées (séparées par des virgules)")
    print("Exemple : entrer,commander,manger,payer")
    print("Tapez 'exit' pour quitter\n")

    while True:
        saisie = input("Actions : ")
        
        if saisie.lower() == "exit":  # condition pour quitter
            print("\nMerci d'avoir utilisé le système !")
            break

        actions = [a.strip() for a in saisie.split(",")]

        script_id, scenario, score = reconnaitre_scenario(actions, scripts)

        print("\n--- RESULTAT ---")
        print("Actions observées :", actions)
        if script_id is None:
            print("Scénario reconnu :", scenario)
        else:
            print("ID du script reconnu :", script_id)
            print("Scénario reconnu :", scenario)
        print("Score de confiance :", round(score, 2))
        print("\n--- Nouvelle saisie possible ---\n")

if __name__ == "__main__":
    main()
