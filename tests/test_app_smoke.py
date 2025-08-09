# tests/test_app_smoke.py
import pytest
from server import app  # adapte si ton fichier principal a un autre nom

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c

def test_home_ok(client):
    resp = client.get("/")
    assert resp.status_code in (200, 302)  # 302 si ta home redirige

def test_create_movie_then_get_it(client):
    payload = {"title": "Inception", "year": 2010}
    r = client.post("/movies", json=payload)
    assert r.status_code in (200, 201)
