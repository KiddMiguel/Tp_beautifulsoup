* instructions d’installation,
* lancement du scraper,
* lancement de l’API,
* description de l’interface HTML (`index.html`),
* exemples d’URLs de test.

---

````markdown
# 📰 Scraper d'Articles + API Flask + Frontend HTML

Ce projet permet de :

- Scraper des articles depuis Blog du Modérateur
- Stocker les données dans MongoDB
- Accéder aux articles via une API Flask avec des filtres
- Afficher et rechercher les articles dans un frontend HTML simple

---

## 🚀 Installation rapide

### 1. Cloner le projet

```bash
git clone [https://github.com/votre-utilisateur/votre-projet.git](https://github.com/KiddMiguel/Tp_beautifulsoup)
cd votre-projet
````

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🗃️ Lancer MongoDB

Assurez-vous que MongoDB est **installé** et **en cours d'exécution** sur `mongodb://localhost:27017`.

---

## 🧹 Lancer le scraper

Tu peux scraper et insérer un article avec :

```bash
python script.py
```

---

## 🌐 Lancer l’API Flask

Dans un terminal :

```bash
python app.py
```

Par défaut, l'API sera disponible sur :
👉 `http://127.0.0.1:5000/articles`

---

## 📦 Endpoints disponibles

| Endpoint    | Méthode | Description                         |
| ----------- | ------- | ----------------------------------- |
| `/articles` | GET     | Récupérer les articles avec filtres |

### 🔎 Paramètres GET disponibles

* `categorie` : filtre par catégorie (ex : "cybersecurite")
* `sous_categorie` : filtre par sous-catégorie (ex : "mots de passe")
* `auteur` : filtre par auteur (ex : "Matthieu Eugène")
* `titre` : recherche partielle dans le titre (ex : "mot de passe")
* `start_date` & `end_date` : filtre entre deux dates (`format ISO 8601` ex : `2024-04-01` à `2024-04-30`)

---

## 📂 Fichier `index.html`

Le fichier HTML simple pour tester l’API est à la racine du projet :

```
/index.html
```

### ▶️ Utilisation

1. Lance l’API Flask avec `python app.py`
2. Ouvre le fichier `index.html` dans un navigateur (double-clique ou clic droit > Ouvrir avec navigateur)
3. Renseigne les filtres de recherche (optionnels)
4. Clique sur "Rechercher"
5. Les résultats s’affichent en bas de la page

> ⚠️ Vérifie que l’API fonctionne bien sur `http://localhost:5000`. Si tu modifies le port dans Flask, n'oublie pas de mettre à jour l'URL dans le `index.html`.

---

## 🔗 Exemples d’URLs de test

| Cas d’usage                            | URL                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Tous les articles                      | `http://localhost:5000/articles`                                                                   |
| Par catégorie                          | `http://localhost:5000/articles?categorie=cybersecurite`                                           |
| Par sous-catégorie                     | `http://localhost:5000/articles?sous_categorie=mots de passe`                                      |
| Par auteur                             | `http://localhost:5000/articles?auteur=Matthieu Eugène`                                            |
| Par mot dans le titre                  | `http://localhost:5000/articles?titre=mot de passe`                                                |
| Par période (2024-04-01 au 2024-04-30) | `http://localhost:5000/articles?start_date=2024-04-01&end_date=2024-04-30`                         |
| Filtres combinés                       | `http://localhost:5000/articles?categorie=cybersecurite&auteur=Matthieu Eugène&titre=mot de passe` |

---

## ✅ Exemple de structure de document MongoDB

```json
{
  "url": "https://...",
  "titre": "Comment créer un mot de passe sécurisé",
  "date": "2024-04-12T09:30:00",
  "auteur": "Matthieu Eugène",
  "categorie": "cybersecurite",
  "sous_categories": ["mots de passe", "protection"],
  "contenu": "Voici comment créer un mot de passe sécurisé..."
}
```
