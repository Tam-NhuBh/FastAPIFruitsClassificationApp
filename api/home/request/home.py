from pydantic import BaseModel, Field


class ImageResuest(BaseModel):
    stringImage : str =  Field(..., description="Fruids Image")