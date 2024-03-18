from pydantic import BaseModel, Field
from typing import Optional



class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15)
    overview: str = Field(max_length=100)
    year: int = Field(le=2025)
    rating: float
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                "year": 2009,
                "rating": 7.8,
                "category": "Acción"
            }
        }