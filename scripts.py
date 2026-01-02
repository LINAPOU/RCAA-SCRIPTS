import csv

class Script:
    def __init__(self, id, scenario, acteurs, contexte, actions):
        self.id = id
        self.scenario = scenario
        self.acteurs = acteurs
        self.contexte = contexte
        self.actions = actions

    def score(self, actions_obs):
        # Similarité simple
        score_actions = len(set(actions_obs) & set(self.actions))
        # Bonus ordre
        score_ordre = 0
        index = 0
        for action in actions_obs:
            if action in self.actions[index:]:
                index = self.actions.index(action) + 1
                score_ordre += 1
        return score_actions + 0.5 * score_ordre

def charger_scripts(fichier):
    scripts = []
    with open(fichier, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            actions = row["actions"].split(";")
            script = Script(
                id=row["id"],
                scenario=row["scenario"],
                acteurs=row["acteurs"],
                contexte=row["contexte"],
                actions=actions
            )
            scripts.append(script)
    return scripts

def reconnaitre_scenario(actions_obs, scripts, seuil=3):
    meilleur_score = 0
    meilleur_script = None

    for script in scripts:
        score_total = script.score(actions_obs)
        if score_total > meilleur_score:
            meilleur_score = score_total
            meilleur_script = script

    if meilleur_score < seuil:
        return None, "Scénario non reconnu", meilleur_score

    return meilleur_script.id, meilleur_script.scenario, meilleur_score
