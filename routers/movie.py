from fastapi import APIRouter, HTTPException, Depends
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.movie import MovieService
from schemas.movie import Movie



movie_router = APIRouter()


        
movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]



@movie_router.get("/movies", tags=["movies"], dependencies=[Depends(JWTBearer())])
def get_movies():
    db = Session()
    result = MovieService(db).get_movies()
    
    return JSONResponse(status_code=200, content = jsonable_encoder(result))




@movie_router.get("/movies/{movie_id}", tags=["movies"])
def get_movie(movie_id: int = Path(ge=1, le=2000)):
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    if not result:
       return JSONResponse(status_code=404, content={"message": "Movie not found"})   
    return JSONResponse(status_code=200, content = jsonable_encoder(result))




        
@movie_router.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    return [movie for movie in movies if movie["category"] == category]

@movie_router.post("/movies", tags=["movies"])
def create_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})



   
@movie_router.put("/movies/{id}", tags=["movies"], status_code=200)
def update_movie(id: int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie(id)   
    if not result:
       return JSONResponse(status_code=404, content={"message": "Movie not found"})   
    
    MovieService(db).update_movie(id, movie)    
    return JSONResponse(status_code=200, content = {"message": "Se modificado la pelicula correctamente"})
    
    
    
    
  
@movie_router.delete("/movies/{movie_id}", tags=["movies"])
def delete_movie(movie_id: int):
    db = Session() 
    result = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not result:
         return JSONResponse(status_code=404, content={"message": "Movie not found"})
    MovieService(db).delete_movie(movie_id)
    return JSONResponse(status_code=200, content={"message": "Movie deleted successfully"})