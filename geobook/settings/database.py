from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    MONGO_URI: str
