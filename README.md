# Cycle Ingénieur ESATIC — site de présentation

Site web pédagogique réalisé avec Flask pour présenter le Cycle Ingénieur généraliste en sciences du numérique de l’ESATIC. Le contenu de la page Formation reprend les unités et crédits des six semestres du syllabus fourni.

> Projet étudiant indépendant, non affilié officiellement à l’ESATIC. Le syllabus fourni comporte quelques libellés ambigus ou incohérents ; le site les présente de façon lisible sans prétendre remplacer la maquette officielle. Vérifier toute information d’admission ou d’organisation auprès de l’ESATIC.

## Fonctionnalités

- Accueil présentant les objectifs et caractéristiques du cycle.
- Programme structuré par année, semestre, unité d’enseignement et crédits.
- Page Vie étudiante limitée aux activités mentionnées dans le syllabus (projets, stages, sport, coaching et conférences).
- Navigation responsive, modèle commun, page 404 personnalisée.

## Prérequis

- Python 3.10 ou supérieur
- `pip`

## Installation et démarrage

```bash
git clone https://github.com/<votre-compte>/<nom-du-repo>.git
cd <nom-du-repo>
python -m venv .venv
```

Active l’environnement virtuel :

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Git Bash
source .venv/Scripts/activate

# macOS / Linux
source .venv/bin/activate
```

Puis installe les dépendances et lance le serveur :

```bash
python -m pip install -r requirements.txt
python app.py
```

Ouvre ensuite <http://127.0.0.1:5000/>. Le mode debug convient au développement local uniquement.

## Routes

| URL | Page |
| --- | --- |
| `/` | Accueil |
| `/formation` | Programme des six semestres |
| `/vie-etudiante` | Projets, stages et développement personnel |

## Structure

```text
.
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── formation.html
│   ├── vie_etudiante.html
│   └── 404.html
└── static/
    ├── esatic-logo.png
    └── style.css
```

## Source du programme

Document de référence transmis pour le projet : `CYCLE-INGENIEUR (1).pdf` (syllabus Cycle Ingénieur ESATIC). Le PDF n’est pas inclus dans ce dépôt ; ajoute-le uniquement si tu as l’autorisation de le redistribuer. Les crédits affichés proviennent de cette source.
