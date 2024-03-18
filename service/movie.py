from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, movie_id):
        result = self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()
        return result
    
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self, id: int, data: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        result.title = data.title
        result.overview = data.overview
        result.year = data.year
        result.rating = data.rating
        result.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, movie_id):
        result = self.db.query(MovieModel).filter(MovieModel.id == movie_id).delete()       
        self.db.commit()
        return