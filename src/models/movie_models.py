import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


class MovieCreate(BaseModel):
    id: int
    title: str
    overview: str = Field(min_length=15, max_length=80)
    year: int = Field(le=datetime.datetime.now().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'Predestination',
                'overview': 'A temporal agent embarks on a final time-traveling assignment.',
                'year': 2014,
                'rating': 7.5,
                'category': 'Action'
            }
        }
    }


class MovieUpdate(BaseModel):
    title: Optional[str]
    overview: Optional[str]
    year: Optional[int]
    rating: Optional[float]
    category: Optional[str]
