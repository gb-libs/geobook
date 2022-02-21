from typing import Any

import bson


class ObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> bson.ObjectId:
        if isinstance(v, (bson.ObjectId, cls)):
            return v
        if isinstance(v, str) and bson.ObjectId.is_valid(v):
            return bson.ObjectId(v)
        raise TypeError('invalid ObjectId specified')
