from datetime import datetime

from pydantic import BaseConfig, BaseModel, Field

from .fields.object_id import ObjectId


class MongoModel(BaseModel):
    id: ObjectId = Field(
        default_factory=ObjectId,
        alias='_id')

    @classmethod
    def from_db(cls, data: dict):
        """We must convert _id into "id". """
        if not data:
            return data
        _id = data.pop('_id', None)
        return cls(**dict(data, id=_id))

    def to_db(self, **kwargs):
        exclude_unset = kwargs.pop('exclude_unset', True)
        by_alias = kwargs.pop('by_alias', True)

        parsed = self.dict(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        # Mongo uses `_id` as default key. We should stick to that as well.
        if '_id' not in parsed and 'id' in parsed:
            parsed['_id'] = parsed.pop('id')

        return parsed

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda object_id: str(object_id),
        }
