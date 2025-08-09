# tests/test_app_smoke.py
import pytest
from server import app, movies_db  # movies_db = MoviesDB('./movies.json')

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:   # client de test Flask
        yield c

def _any_movie_id():
    items = movies_db.list()
    assert items, "Le test suppose qu'il y a au moins un film dans movies.json"
    m = items[0]
    mid = m.get("id") or m.get("ID") or m.get("pk") or 1
    return int(mid)

def test_home_ok(client):
    r = client.get("/")
    assert r.status_code in (200, 302)

def test_movie_details_ok(client):
    mid = _any_movie_id()
    r = client.get(f"/movie-details/{mid}")
    assert r.status_code in (200, 302)

def test_forms_render(client):
    mid = _any_movie_id()
    assert client.get("/add-movie-form").status_code == 200
    assert client.get(f"/edit-movie-form/{mid}").status_code == 200
    assert client.get(f"/delete-movie-form/{mid}").status_code == 200

def test_add_movie_redirects(client):
    # add-movie est un GET avec query string et renvoie redirect('/')
    params = {"title": "T", "year": "2020", "actors": "A", "plot": "P", "poster": ""}
    r = client.get("/add-movie", query_string=params, follow_redirects=False)
    assert r.status_code in (301, 302)
