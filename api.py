from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS

from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["scraping_articles"]  # Doit correspondre au nom réel de ta base
collection = db["articles"]

@app.route("/articles", methods=["GET"])
def get_articles():
    query = {}

    # Filtres basés sur la structure insérée : auteur, titre, date, categorie, sous_categories
    categorie = request.args.get("categorie")
    sous_categorie = request.args.get("sous_categorie")
    auteur = request.args.get("auteur")
    titre = request.args.get("titre")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if categorie:
        query["categorie"] = categorie
    if sous_categorie:
        query["sous_categories"] = sous_categorie  # cherche dans la liste
    if auteur:
        query["auteur"] = auteur
    if titre:
        query["titre"] = {"$regex": titre, "$options": "i"}

    # Dates ISO 8601 → filtrage en datetime
    if start_date and end_date:
        try:
            query["date"] = {
                "$gte": start_date,
                "$lte": end_date
            }
        except Exception:
            return jsonify({"error": "Format de date incorrect. Utilisez YYYY-MM-DDTHH:MM:SS"}), 400

    articles = collection.find(query)
    return dumps(articles), 200

if __name__ == "__main__":
    app.run(debug=True)
