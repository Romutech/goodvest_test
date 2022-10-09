
           Test Technique Python / Django / DRF

Ce test a pour but d'évaluer tes connaissances de base du langage de programmation
Python et de ses technos associées, ici, le framework Django et Django REST framework.

Le test consiste à créer une API REST ou un utilisateur possèdera un
portefeuille et verra à son portefeuille, des fonds financiers y êtres associés.

Tu dois:
- Créer les modèles Portfolio et Fund
- Generer les migrations
- Créer les vues permettant d'interagir avec les modèles comme précisé plus bas
- Créer le routing permettant de call les vues en questions
- Créer les fonctionnalités demandées plus bas


#################### FONCTIONNALITÉS DEMANDÉES ####################


 Modèle Portfolio:
 Le modèle doit posséder deux attributs :
 - Un attribut qui est une relation avec le modèle User
 - Un attribut "amount" qui aura le type "float" et initialisé à None par
 défaut.
 Infos: un utilisateur ne peut avoir qu'un "Portfolio" et un "Portfolio" ne
 peut être rattaché qu'à un utilisateur.

 Modèle Fonds
 Le modèle "Fund" doit avoir 3 attributs
 - Un attribut qui est une relation avec le modèle Portefeuille, La suppression d'un
 fonds ne doit pas supprimer les fonds associés
 - Un attribut "percentage" qui aura le type "float" et initialisé à None par
 défaut.
  - Un attribut "date" représentant un champ "date" de type datetime.date en
  Python

  Infos : un "Fund" peut être attaché à plusieurs "Portfolio" et un "Portfolio"
  peut avoir plusieurs "Funds".

                Diagramme UML Simplifié


    ┌──────────┐                       ┌──────────┐
    │   User   │                       │Portfolio │
    ├──────────┤1                      ├──────────┤*
    │- id      ├──────────┐           1│- id      ├──────┐
    │...       │          └───────────►│- user_id │      │
    │          │                       │- amount  │      │
    └──────────┘                       └──────────┘      │
                                                         │
                                                         │
                                                         │
                   ┌──────────────┐                      │
                   │     Fund     │                      │
                   ├──────────────┤                      │
                   │- id          │0..n                  │
                   │- portfolio_id│◄─────────────────────┘
                   │- percentage  │
                   │- date        │
                   └──────────────┘


 Nous souhaitons interagir avec Portfolio, avec au minimum, les
 fonctionnalités suivantes :

 - Créer un portefeuille associé à un user.
 Exemple de endpoint :
 [POST] http://127.0.0.1:8000/funds_management/portfolio/
 Exemple de Body :
 {
    "user_id": "42",
    "amount": "42000",
 }

  - Supprimer un portefeuille associé à un user.
 Exemple de endpoint :
 [DELETE] http://127.0.0.1:8000/funds_management/portfolio/{id}/


 Nous souhaitons un CRUD permettant d'interagir avec "Fund" avec
 les fonctionnalités suivantes :

 - Créer un fonds associé à un portefeuille.
 Exemple de endpoint :
 [POST] http://127.0.0.1:8000/funds_management/funds/
 Exemple de Body :
 {
    "portfolio_id": "42",
    "percentage": "0.25",
    "date": "2022-05-01"
 }

 - Modifier un fonds associé à un portefeuille.
 Exemple de endpoint :
 [PATCH] http://127.0.0.1:8000/funds_management/funds/{id}/
 Exemple de Body :
 {
    "percentage": "0.42",
 }

 - Lister tous les fonds.
 Exemple de endpoint :
 [GET] http://127.0.0.1:8000/funds_management/funds/

 - Lister un fonds en question.
 Exemple de endpoint :
 [GET] http://127.0.0.1:8000/funds_management/funds/{id}/

 - Supprimer un fonds en question.
 Exemple de endpoint :
 [DELETE] http://127.0.0.1:8000/funds_management/funds/{id}/

 - Lister les fonds avec une fourchette de date envoyée dans le body - au format de
 dates françaises - avec une date de départ et une date de fin incluses.
 Exemple de endpoint :
 [GET] http://127.0.0.1:8000/funds_management/funds/date_range
 Exemple de body :
 {
    "start_date": "11/03/2021",
    "end_date": "10/06/2022",
 }

  Une fois le projet terminé, tu devras versionner le projet sur Github avec un Repo privé
  auquel tu nous donnera accès.
  Mon Profil GitHub est "Romutech".


Pour tester le fonctionnement du projet de ton côté, tu peux:
 - Créer un environnement virtuel et installer les dépendances renseignées dans
requirements.txt
 - Jouer les migrations
 - lancer le serveur de développement.

 Good Luck! ^^
 
 Robin Muller
