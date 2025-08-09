import pytest
from server import app, movies_db

@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c

def test_home_ok(client, monkeypatch):
    monkeypatch.setattr(movies_db, "list", lambda: [{"id": 1, "title": "T"}])
    r = client.get("/")
    assert r.status_code in (200, 302)

def test_movie_details_ok(client, monkeypatch):
    monkeypatch.setattr(movies_db, "read", lambda mid: {"id": mid, "title": "T"})
    r = client.get("/movie-details/1")
    assert r.status_code in (200, 302)

def test_forms_render(client, monkeypatch):
    monkeypatch.setattr(movies_db, "read", lambda mid: {"id": mid, "title": "T"})
    assert client.get("/add-movie-form").status_code == 200
    assert client.get("/edit-movie-form/1").status_code == 200
    assert client.get("/delete-movie-form/1").status_code == 200

def test_add_movie_redirects(client, monkeypatch):
    called = {}
    def fake_create(title, year, actors, plot, poster):
        called.update(title=title, year=year, actors=actors, plot=plot, poster=poster)
        return {"id": 999}
    monkeypatch.setattr(movies_db, "create", fake_create)
    monkeypatch.setattr(movies_db, "save", lambda path: None)

    r = client.get("/add-movie", query_string={
        "title": "T", "year": "2020", "actors": "A", "plot": "P", "poster": ""
    }, follow_redirects=False)

    assert r.status_code in (301, 302)
    assert called["title"] == "T"

def test_edit_movie_redirects(client, monkeypatch):
    called = {}
    def fake_update(mid, title, year, actors, plot, poster):
        called.update(mid=int(mid), title=title, year=year)
        return True
    monkeypatch.setattr(movies_db, "update", fake_update)
    monkeypatch.setattr(movies_db, "save", lambda path: None)

    r = client.get("/edit-movie/1", query_string={
        "title": "New", "year": "2021", "actors": "A2", "plot": "P2", "poster": ""
    }, follow_redirects=False)

    assert r.status_code in (301, 302)
    assert called["mid"] == 1
    assert called["title"] == "New"
    assert called["year"] == "2021"

def test_delete_movie_redirects(client, monkeypatch):
    called = {}
    monkeypatch.setattr(movies_db, "delete", lambda mid: called.update(mid=int(mid)) or True)
    monkeypatch.setattr(movies_db, "save", lambda path: None)

    r = client.get("/delete-movie/1", follow_redirects=False)

    assert r.status_code in (301, 302)
    assert called["mid"] == 1
