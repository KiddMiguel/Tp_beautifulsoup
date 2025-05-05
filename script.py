import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scraping_articles']
collection = db['articles']

def get_article_details(url):
    print(f"🔄 Chargement de l'article depuis : {url} ...")
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Erreur lors du chargement de la page")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Titre
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.get_text(strip=True) if title_tag else 'Titre non trouvé'

    # Date
    date_tag = soup.find('time')
    date = date_tag.get('datetime') if date_tag else 'Date non trouvée'

    # Auteur
    author_tag = soup.select_one('span.byline a')
    author = author_tag.get_text(strip=True) if author_tag else 'Auteur non trouvé'

    # Contenu principal
    content_div = soup.find('div', class_='entry-content')
    content = content_div.get_text(separator='\n', strip=True) if content_div else 'Contenu non trouvé'

    # Catégorie
    cat_span = soup.select_one('div.cats-list span.cat')
    categorie = cat_span['data-cat'] if cat_span and cat_span.has_attr('data-cat') else 'Catégorie non trouvée'

    # Sous-catégories
    tags_ul = soup.select('ul.tags-list li a')
    sous_categories = [tag.get_text(strip=True) for tag in tags_ul] if tags_ul else []

    print("✅ Article chargé avec succès.")
    return {
        'url': url,
        'titre': title,
        'date': date,
        'auteur': author,
        'categorie': categorie,
        'sous_categories': sous_categories,
        'contenu': content
    }

url = 'https://www.blogdumoderateur.com/comment-creer-mot-de-passe-securise-bonnes-pratiques/'

# Extraire les infos
article = get_article_details(url)

# Enregistrer dans MongoDB
if article:
    collection.insert_one(article)
    print("✅ Article inséré dans MongoDB avec succès.")
else:
    print("⚠️ Aucun article à insérer.")
