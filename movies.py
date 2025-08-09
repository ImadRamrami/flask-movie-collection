import json

class MoviesDB:
  def __init__(self, db_path):
    self.movies = {}
    self.next_id = 0
    self.load(db_path)

  def load(self, db_path):
    with open(db_path, 'r', encoding='utf-8') as fh:
      movies = json.load(fh)
    # convert keys from string to integers
    self.movies = {int(key): movies[key] for key in movies}
    self.next_id = max(self.movies.keys()) + 1

  def save(self, db_path):
    with open(db_path, 'w', encoding='utf-8') as fh:
      json.dump(self.movies, fh, ensure_ascii=False, indent=4)

  def list(self,):
    movie_list = list(self.movies.values())
    movie_list.sort(key=lambda e: e['id'])
    return movie_list

  def create(self, title, year, actors, plot, poster):
    movie = {
      "id": self.next_id,
      "title": title,
      "year": year,
      "actors": actors,
      "plot": plot,
      "poster": poster
    }
    self.movies[movie['id']] = movie
    self.next_id = self.next_id+1
    return movie['id']

  def read(self, id):
    if id in self.movies:
      return self.movies[id]
    else:
      return None

  def update(self, id, title, year, actors, plot, poster):
    if id in self.movies:
      self.movies[id]['title'] = title
      self.movies[id]['year'] = year
      self.movies[id]['actors'] = actors
      self.movies[id]['plot'] = plot
      self.movies[id]['poster'] = poster
      return True
    else:
      return False

  def delete(self, id):
    if id in self.movies:
      del self.movies[id]
      return True
    else:
      return False
