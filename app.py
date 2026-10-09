from flask import Flask, render_template

app = Flask(__name__)

SEMESTERS = [
    {
        "year": "Ingénieur 1", "semester": "S1", "credits": 30,
        "units": [
            ("Optimisation et analyse de données", "Optimisation, probabilités, fonctions électroniques", 6),
            ("Physique appliquée", "Propagation et antennes, transmission optique", 6),
            ("Algorithmes et systèmes d’exploitation", "Algorithmique, langages de programmation, introduction aux systèmes d’exploitation", 5),
            ("Modélisation, bases de données et SI", "Modélisation, bases de données, systèmes d’information", 5),
            ("Management, économie et sciences sociales", "Droit de l’entreprise, économie, gestion de projets", 4),
            ("Langues et communication", "Anglais, communication, culture et citoyenneté", 3),
            ("Développement personnel", "Coaching et conférences", 1),
        ],
    },
    {
        "year": "Ingénieur 1", "semester": "S2", "credits": 30,
        "units": [
            ("Signal et communications", "Théorie du signal, théorie de l’information, réseaux télécoms fixes et mobiles", 6),
            ("Réseaux, services et protocoles", "Routage, performances des réseaux, files d’attente, QoS", 6),
            ("Stage de découverte", "Stage de 2 à 8 semaines", 8),
            ("Projet", "Projet pédagogique", 4),
            ("Langues et communication", "Anglais, communication, culture et citoyenneté", 3),
            ("Développement personnel", "Coaching et conférences", 1),
            ("Développement durable", "Enjeux du développement durable", 2),
        ],
    },
    {
        "year": "Ingénieur 2", "semester": "S3", "credits": 30,
        "units": [
            ("Télécommunications et communication sécurisée", "Physique des télécommunications, communication sécurisée", 6),
            ("Systèmes d’information et multimédia", "Langages, architectures et applications web, acquisition multimédia", 6),
            ("Projet", "Projet pédagogique", 4),
            ("Langues", "Anglais, communication, culture et citoyenneté", 3),
            ("Calculs scientifiques", "Calculs scientifiques", 3),
            ("Évolution des réseaux", "Évolution des réseaux", 2),
            ("Programmation orientée sécurité", "Programmation orientée sécurité", 2),
            ("Apprentissage automatique", "Introduction à l’apprentissage automatique", 2),
            ("Développement personnel", "Sport, coaching ou conférence", 2),
        ],
    },
    {
        "year": "Ingénieur 2", "semester": "S4", "credits": 30,
        "units": [
            ("Génie logiciel et systèmes d’information", "Programmation système et réseau, transformation numérique", 5),
            ("Réseaux, services et protocoles", "Protocoles et réseaux informatiques sans fil", 4),
            ("Apprentissage et data", "Classification automatique, data mining, statistique appliquée", 4),
            ("Projet", "Projet pédagogique", 4),
            ("Stage", "Stage", 8),
            ("Langues", "Anglais, communication, culture et citoyenneté", 3),
            ("Développement personnel", "Sport, coaching ou conférence", 2),
        ],
    },
    {
        "year": "Ingénieur 3", "semester": "S5", "credits": 30,
        "units": [
            ("Intelligence artificielle", "Apprentissage profond et apprentissage par renforcement", 5),
            ("Intégration et déploiement des SI", "Serveurs d’applications, Big Data, cloud computing et déploiement", 5),
            ("Numérique responsable", "Impacts du numérique, droit du numérique, initiation à la RSE", 4),
            ("Projet", "Projet d’application en intelligence artificielle", 4),
            ("Langues", "Anglais, communication, culture et citoyenneté", 3),
            ("IA, éthique et société", "Enjeux éthiques et sociaux de l’IA et des sciences des données", 2),
            ("Traitement d’images", "Vision par ordinateur", 2),
            ("Web sémantique et Big Data", "Web sémantique et infrastructure pour le Big Data", 3),
            ("Développement personnel", "Sport, coaching ou conférence", 2),
        ],
    },
    {
        "year": "Ingénieur 3", "semester": "S6", "credits": 30,
        "units": [("Stage de fin de cycle", "Stage", 30)],
    },
]

@app.route("/")
def accueil():
    return render_template("index.html", active="accueil")

@app.route("/formation")
def formation():
    return render_template("formation.html", active="formation", semesters=SEMESTERS)

@app.route("/vie-etudiante")
def vie_etudiante():
    return render_template("vie_etudiante.html", active="vie-etudiante")

@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
