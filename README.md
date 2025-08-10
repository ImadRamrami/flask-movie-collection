# Flask Movie Collection

[![tests](https://github.com/ImadRamrami/flask-movie-collection/actions/workflows/tests.yml/badge.svg)](https://github.com/ImadRamrami/flask-movie-collection/actions/workflows/tests.yml)

Mini-application **Flask** pour gérer une petite collection de films (lecture / ajout / édition / suppression) stockée en **JSON**.  
Le dépôt inclut une suite de **tests `pytest`**, une **barrière de couverture ≥ 80%**, et une **CI GitHub Actions**.

---

## ✨ Fonctionnalités

- Liste des films & page de détails
- Formulaires d’ajout, d’édition et de suppression
- Persistance dans `movies.json` **UTF-8**
- Suite de tests (`pytest`) + **coverage** + **CI** (exécutés au push/PR)

---

## 🧱 Stack & Outils

- **Backend** : Python 3.11, Flask
- **Tests** : pytest, pytest-cov (coverage)
- **CI** : GitHub Actions (`.github/workflows/tests.yml`)

---

## 🚀 Démarrage rapide

### 1) Cloner & installer
```bash
git clone https://github.com/ImadRamrami/flask-movie-collection.git
cd flask-movie-collection
# dépendances
pip install -r requirements.txt
