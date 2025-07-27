from flask import Flask, render_template, request, redirect
import movies

app = Flask(__name__)

db_path = './movies.json'
movies_db = movies.MoviesDB(db_path)

@app.route('/')
def movie_list():
  return render_template('movie-list.html',
                         movies=movies_db.list())

@app.route('/movie-details/<id>')
def movie_details(id):
  movie = movies_db.read(int(id))
  return render_template('movie-details.html',
                         movie=movie)

@app.route('/edit-movie-form/<id>')
def edit_movie_form(id):
  movie = movies_db.read(int(id))
  return render_template('edit-movie-form.html',
                         movie=movie)

@app.route('/edit-movie/<id>')
def edit_movie(id):
  d = request.args
  movies_db.update(int(id), d['title'], d['year'],
                   d['actors'], d['plot'], d['poster'])
  movies_db.save(db_path)
  return redirect('/')

@app.route('/add-movie-form')
def add_movie_form():
  return render_template('add-movie-form.html')

@app.get('/add-movie')
def add_movie():
  d = request.args
  movies_db.create(d['title'], d['year'], d['actors'],
                   d['plot'], d['poster'])
  movies_db.save(db_path);
  return redirect('/')

@app.get('/delete-movie-form/<id>')
def delete_movie_form(id):
  movie = movies_db.read(int(id))
  return render_template('delete-movie-form.html',
                         movie=movie)

@app.get('/delete-movie/<id>')
def delete_movie(id):
  movies_db.delete(int(id))
  movies_db.save(db_path)
  return redirect('/')
