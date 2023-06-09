#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:

    """Initialise class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    """modify the updated_at attribute"""

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    """return string representation"""

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    """return dict"""

    def to_dict(self):
        obj = dict(self.__dict__)
        obj["__class__"] = self.__class__.__name__
        obj["created_at"] = obj["created_at"].isoformat()
        obj["updated_at"] = obj["updated_at"].isoformat()
        return obj
